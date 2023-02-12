--- ---

<h2>Credentialed Enumeration from Linux</h2>

Requirements for these attacks (one of the following):
- Cleartext password for a user
- NTLM password hash for a user
- SYSTEM access on a domain-joined host

--> **Enumeration with CrackMapExec**

CME - Domain User Enumeration:
```
sudo crackmapexec smb 172.16.5.5 -u forend -p PASSWORD --users
```

CME - Domain Group Enumeration
```
sudo crackmapexec smb 172.16.5.5 -u forend -p PASSWORD --groups
```

- Key Groups:
	- Administrators
	- Domain Admins
	- Executives
	- Backup Operators

CME - Logged On Users
```
sudo crackmapexec smb 172.16.5.130 -u forend -p PASSWORD --loggedon-users
```

Share Enumeration - Domain Controller
```
sudo crackmapexec smb 172.16.5.5 -u forend -p PASSWORD --shares
```

Using Spider_plus to list all readable shares
```
sudo crackmapexec smb 172.16.5.5 -u forend -p PASSWORD -M spider_plus --share 'Department Shares'
```
- Writes the results to a JSON file located at /tmp/cme_spider_plus/`<ip of host>`


Enumeration with SMBMap

SMBMap To Check Access:
```
smbmap -u forend -p PASSWORD -d INLANEFREIGHT.LOCAL -H 172.16.5.5
```

Recursive List Of All Directories:
```
smbmap -u forend -p PASSWORD -d INLANEFREIGHT.LOCAL -H 172.16.5.5 -R 'Department Shares' --dir-only
```


--> **Enumeration with RPCClient**
Initial Unauthenticated Connection:
```
rpcclient -U "" -N 172.16.5.5
```

RPCClient Enumeration -- Understanding RIDs and SIDs:
While looking at users in rpcclient, you may notice a field called rid: beside each user. A Relative Identifier (RID) is a unique identifier (represented in hexadecimal format) utilized by Windows to track and identify objects. To explain how this fits in, let's look at the examples below:
	- The SID for the INLANEFREIGHT.LOCAL domain is: S-1-5-21-3842939050-3880317879-2865463114.
	- When an object is created within a domain, the number above (SID) will be combined with a RID tomake a unique value used to represent the object.
	- So the domain user htb-student with a RID:[0x457] Hex 0x457 would = decimal 1111, will have a full user SID of: S-1-5-21-3842939050-3880317879-2865463114-1111.
	- This is unique to the htb-student object in the INLANEFREIGHT.LOCAL domain and you will never see this paired value tied to another object in this domain or any other.

However, there are accounts that you will notice that have the same RID regardless of what host you are on. Accounts like the built-in Administrator for a domain will have a RID [administrator] rid:[0x1f4], which, when converted to a decimal value, equals 500. The built-in Administrator account will always have the RID value Hex 0x1f4, or 500. This will always be the case. Since this value is unique to an object, we can use it to enumerate further information about it from the domain. Let's give it a try again with rpcclient. We will dig a bit targeting the htb-student user.

RPCClient User Enumeration By RID:
```
rpcclient $> queryuser 0x457
User Name : htb-student
Full Name : Htb Student
Home Drive :
Dir Drive :
Profile Path:
Logon Script:
Description :
Workstations:
Comment :
Remote Dial :
Logon Time : Wed, 02 Mar 2022 15:34:32 EST
Logoff Time : Wed, 31 Dec 1969 19:00:00 EST
Kickoff Time : Wed, 13 Sep 30828 22:48:05 EDT
Password last set Time : Wed, 27 Oct 2021 12:26:52 EDT
Password can change Time : Thu, 28 Oct 2021 12:26:52 EDT
Password must change Time: Wed, 13 Sep 30828 22:48:05 EDT unknown_2[0..31]...
user_rid : 0x457
group_rid: 0x201
acb_info : 0x00000010
fields_present: 0x00ffffff
logon_divs: 168
bad_password_count: 0x00000000
logon_count: 0x0000001d
padding1[0..7]...
logon_hrs[0..21]...
```

Find RIDs Of All Users:
```
rpcclient $>
enumdomusers
user:[administrator]
rid:[0x1f4]
user:[guest] rid:[0x1f5]
user:[krbtgt] rid:[0x1f6]
user:[lab_adm]
rid:[0x3e9]
user:[htb-student]
rid:[0x457]
user:[avazquez]
rid:[0x458]
user:[pfalcon] rid:[0x459]
user:[fanthony]
rid:[0x45a]
user:[wdillard]
rid:[0x45b]
user:[lbradford]
rid:[0x45c]
user:[sgage] rid:[0x45d]
user:[asanchez]
rid:[0x45e]
user:[dbranch]
rid:[0x45f]
user:[ccruz] rid:[0x460]
user:[njohnson]
rid:[0x461]
user:[mholliday]
rid:[0x462]
```


--> **Impacket Toolkit**
Impacket is a versatile toolkit that provides us with many different ways to enumerate, interact, and exploit Windows protocols and find the information we need using Python. The tool is actively maintained and has many contributors, especially when new attack techniques arise.

Psexec.py
One of the most useful tools in the Impacket suite is psexec.py. Psexec.py is a clone of the Sysinternals psexec executable, but works slightly differently from the original. The tool creates a remote service by uploading a randomly-named executable to the ADMIN$ share on the target host. It then registers the service via RPC and the Windows Service Control Manager. Once established, communication happens over a named pipe, providing an interactive remote shell as SYSTEM on the victim host.

If we have credentials to a user with local admin privileges, this is the syntax:
```
psexec.py inlanefreight.local/wley:'transporter@4'@172.16.5.125
```

Wmiexec.py
Wmiexec.py utilizes a semi-interactive shell where commands are executed through Windows Management Instrumentation. It does not drop any files or executables on the target host and generates fewer logs than other modules. After connecting, it runs as the local admin user we connected with (this can be less obvious to someone hunting for an intrusion than seeing SYSTEM executing many commands).
```
wmiexec.py inlanefreight.local/wley:'transporter@4'@172.16.5.5
```

Windapsearch.py
Windapsearch is another handy Python script we can use to enumerate users, groups, and computers from a Windows domain by utilizing LDAP queries.

Windapsearch - Domain Admins
```
python3 windapsearch.py --dc-ip 172.16.5.5 -u forend@inlanefreight.local -p 
```

PASSWORD --daWindapsearch - Privileged Users
```
python3 windapsearch.py --dc-ip 172.16.5.5 -u forend@inlanefreight.local -p PASSWORD -PU
```

Bloodhound.py
```
sudo bloodhound-python -u 'forend' -p 'PASSWORD' -ns 172.16.5.5 -d
inlanefreight.local -c all
```
- You upload this "loot" into bloodhound after starting neo4j
- Custom query cheat sheet -- BloodHound Cypher Cheatsheet | hausec

---

<h2>Credentialed Enumeration from Windows</h2>

- AD PowerShell Module
	The ActiveDirectory PowerShell module is a group of PowerShell cmdlets for administering an Active Directory environment from the command line. It consists of 147 different cmdlets at the time of writing. We can't cover them all here, but we will look at a few that are particularly useful for enumerating AD environments.

Check If Module is Available:
```
Get-Module
```

If it is not available, install with this command:
```
Import-Module ActiveDirectory
```

Get Domain Information:
```
Get-ADDomain
```

Get-ADUser and Filter for Kerberoastable Accounts
```
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```

Checking for Trust Relationships
```
Get-ADTrust -Filter *
```

Group Enumeration
```
Get-ADGroup -Filter * | select name
```

Detailed Group Info
```
Get-ADGroup -Identity "Backup Operators"
```

Enumerate Group Membership
```
Get-ADGroupMember -Identity "Backup Operators"
```


---> PowerView
PowerView is a tool written in PowerShell to help us gain situational awareness within an AD environment. Much like BloodHound, it provides a way to identify where users are logged in on a network, enumerate domain information such as users, computers, groups, ACLS, trusts, hunt for file shares and passwords, perform Kerberoasting, and more. It is a highly versatile tool that can provide us with great insight into the security posture of our client's domain.

Domain User Enumeration (mmorgan user)
```
Get-DomainUser -Identity mmorgan -Domain inlanefreight.local | Select-Object -Property name,samaccountname,description,memberof,whencreated,pwdlastset,lastlogontimesta mp,accountexpires,admincount,userprincipalname,serviceprincipalname,useraccountcont rol
```

Recursive Group Membership
```
Get-DomainGroupMember -Identity "Domain Admins" -Recurse
```

Trust Enumeration
```
Get-DomainTrustMapping
```

Testing for Local Admin Access
```
Test-AdminAccess -ComputerName <COMPUTERNAME>
```

Finding Users with SPN Set (Kerberoastable)
```
Get-DomainUser -SPN -Properties 
samaccountname,ServicePrincipalName
```


---> Snaffler
Snaffler is a tool that can help us acquire credentials or other sensitive data in an Active Directory environment. Snaffler works by obtaining a list of hosts within the domain and then enumerating those hosts for shares and readable directories. Once that is done, it iterates through any directories readable by our user and hunts for files that could serve
to better our position within the assessment. Snaffler requires that it be run from a domain-joined host or in a domain-user context.

Releases · SnaffCon/Snaffler (github.com)

Syntax:
```
Snaffler.exe -s -d inlanefreight.local -o snaffler.log -v data
```
- -s = print results to console
- -d = specifies the domain to search within
- -o = tells Snaffler to write results to a logfile
- -v = sets the verbosity level (data is best to start with)


---> BloodHound
Bloodhound is an exceptional open-source tool that can identify attack paths within an AD environment by analyzing the relationships between objects. Both penetration testers and blue teamers can benefit from learning to use BloodHound to visualize relationships in the domain. When used correctly and coupled with custom Cipher queries, BloodHound may find high-impact, but difficult to discover, flaws that have been present in the domain for years.

Running SharpHound.exe From Windows Attack Host
```
.\SharpHound.exe -c All --zipfilename ILFREIGHT
```

Transfer the loot to attack machine and load it into BloodHound

Queries To Look At:
```
Find Computers with Unsupported Operating Systems
```

These systems are relatively common to find within enterprise networks (especially older environments), as they often run some product that cannot be updated or replaced as of yet. Keeping these hosts around may save money, but they also can add unnecessary vulnerabilities to the network. Older hosts may be susceptible to older remote code execution vulnerabilities like MS08-067.

```
Find Computers where Domain Users are Local Admin
```

We will often see users with local admin rights on their host (perhaps temporarily to install a piece of software, and the rights were never removed), or they occupy a high enough role in the organization to demand these rights (whether they require them or not). Other times we'll see excessive local admin rights handed out across the organization, such as multiple groups in the IT department with local admin over groups of servers or even the entire Domain Users group with local admin over one or more hosts.

---

<h2>Living Off the Land</h2>

Earlier in the module, we practiced several tools and techniques (both credentialed and uncredentialed) to enumerate the AD environment. These methods required us to upload or pull the tool onto the foothold host or have an attack host inside the environment. This section will discuss several techniques for utilizing native Windows tools to perform our enumeration and then practice them from our Windows attack host.

![[Pasted image 20221225205147.png]]

![[Pasted image 20221225210620.png]]


---> Downgrade Powershell To Evade Logging
Many defenders are unaware that several versions of PowerShell often exist on a host. If not uninstalled, they can still be used. Powershell event logging was introduced as a feature with Powershell 3.0 and forward. With that in mind, we can attempt to call Powershell version 2.0 or older. If successful, our actions from the shell will not be logged in Event Viewer. This is a great way for us to remain under the defenders' radar while still utilizing resources built into the hosts to our advantage. Below is an example of downgrading Powershell.

![[Pasted image 20221225210807.png]]


---> Checking Defenses
Firewall Checks (from Powershell) 
```
netsh advfirewall show allprofiles
```

Windows Defender Check (from CMD.exe)
```
sc query windefend
```

Check Windows Defender Settings (Powershell)
```
Get-MpComputerStatus
```
Knowing what revision our AV settings are at and what settings are enabled/disabled can greatly benefit us. We can tell how often scans are run, if the on-demand threat alerting is active, and more. This is also great info for reporting. Often defenders may think that certain settings are enabled or scans are scheduled to run at certainintervals. If that's not the case, these findings can help them remediate those issues.


--->More Enumeration
Check if anyone else is logged into the machine
```
qwinst a
```

![[Pasted image 20221225211656.png]]

Using arp -a and route print will not only benefit in enumerating AD environments, but will also assist us in identifying opportunities to pivot to different network segments in any environment. These are commands we should consider using on each engagement to assist our clients in understanding where an attacker may attempt to go following initial compromise.


---> Windows Management Instrumentation (WMI)

Windows Management Instrumentation (WMI) is a scripting engine that is widely used within Windows enterprise environments to retrieve information and run administrative tasks on local and remote hosts.

Cheat sheet -- https://gist.github.com/xorrior/67ee741af08cb1fc86511047550cdaf4

![[Pasted image 20221225211952.png]]

Example from the course to query host and domain info using wmic:
```
wmic ntdomain get Caption,Description,DnsForestName,DomainName,DomainControllerAddress
```

![[Pasted image 20221225212031.png]]


---> Net Commands
Net commands can be beneficial to us when attempting to enumerate information from the domain. These commands can be used to query the local host and remote hosts, much like the capabilities provided by WMI.

![[Pasted image 20221225212117.png]]

Trick to evade defenders
If you believe the network defenders are actively logging/looking for any commands out of the normal, you can try this workaround to using net commands. Typing net1 instead of net will execute the same functions without the potential trigger from the net string.


---> Dsquery
Dsquery is a helpful command-line tool that can be utilized to find Active Directory objects. The queries we run with this tool can be easily replicated with tools like BloodHound and PowerView, but we may not always have those tools at our disposal, as discussed at the beginning of the section. But, it is a likely tool that domain sysadmins are utilizing in their environment. With that in mind, dsquery will exist on any host with the Active Directory Domain Services Role installed, and the dsquery DLL exists on all modern Windows systems by default now and can be found at C:\Windows\System32\dsquery.dll.

![[Pasted image 20221225212419.png]]

![[Pasted image 20221225212437.png]]

![[Pasted image 20221225212459.png]]

Users with Specific Attributes Set (PASSWD_NOTREQD)
```
dsquery * -filter "(&(objectCategory=person)(objectClass=user (userAccountControl:1.2.840.113556.1.4.803:=32))" -attr distinguishedName userAccountControl
```

Searching for Domain Controllers
```
dsquery * -filter  "(userAccountControl:1.2.840.113556.1.4.803:=8192)" -limit 5 - attr sAMAccountName
```