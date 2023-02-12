--- ---

<h2>Commands</h2>

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

---

<h2>More Information</h2>

More information ---> [Crackmapexec]([[Red Team/6 - Machine/3 - Active Directory/General/Tools/TOP/1 - Crackmapexec]])