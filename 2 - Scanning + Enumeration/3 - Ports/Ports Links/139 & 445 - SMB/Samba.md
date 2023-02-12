--- ---

<h2>General Commands</h2>

- Nmap (SCRIPT)
```Terminal
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse IP    --->  (Enum Users)
```

- SMB
```Terminal
smbclient //<ip>/anonymous               (Find public files)
smbget -R smb://<ip>/anonymous           (Download Files available) or simply `get ELEMENT`
```

---
<h2>What is Samba</h2>

![](https://i.imgur.com/O8S93Kr.png)

Samba is the standard Windows interoperability suite of programs for Linux and Unix. It allows end users to access and use files, printers and other commonly shared resources on a companies intranet or internet. Its often referred to as a network file system.

Samba is based on the common client/server protocol of Server Message Block (SMB). SMB is developed only for Windows, without Samba, other computer platforms would be isolated from Windows machines, even if they were part of the same network.

Using nmap we can enumerate a machine for SMB shares.

SMB has two ports, 445 and 139.

![](https://i.imgur.com/bkgVNy3.png)




