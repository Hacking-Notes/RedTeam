--- ---
<h3>What is SMB</h3>
SMB - Server Message Block Protocol - is a client-server communication protocol used for sharing access to files, printers, serial ports and other resources on a network. [[source](https://searchnetworking.techtarget.com/definition/Server-Message-Block-Protocol)]  

Servers make file systems and other resources (printers, named pipes, APIs) available to clients on the network. Client computers may have their own hard disks, but they also want access to the shared file systems and printers on the servers.

The SMB protocol is known as a response-request protocol, meaning that it transmits multiple messages between the client and server to establish a connection. Clients connect to servers using TCP/IP (actually NetBIOS over TCP/IP as specified in RFC1001 and RFC1002), NetBEUI or IPX/SPX.

- **How does SMB work?**  

	![](https://i.imgur.com/XMnru12.png)

	Once they have established a connection, clients can then send commands (SMBs) to the server that allow them to access shares, open files, read and write files, and generally do all the sort of things that you want to do with a file system. However, in the case of SMB, these things are done over the network.

- **What runs SMB?**

	Microsoft Windows operating systems since Windows 95 have included client and server SMB protocol support. Samba, an open source server that supports the SMB protocol, was released for Unix systems.

- **SMB Ports**

	SMB run on the port 139 and 445

---
<h3>Find SMB Port</h3>
- Nmap
```Terminal
nmap -sV -sC IP -p110
```

- Possible to find SMB on an other port

---
<h3>Connection</h3>
<h4>Linux connection</h4>
- Enumeration (Need to know the share location & name of interesting file)
```Terminal
Enum4Linux          ---> https://github.com/CiscoCXSecurity/enum4linux
```

Enum4Linux Commands

- -U             get userlist  
- -M             get machine list  
- -N             get namelist dump (different from -U and-M)  
- -S             get sharelist  
- -P             get password policy information  
- -G             get group and member list

- -a             all of the above (full basic enumeration)  


- SMBclient
```Terminal
- smbclient -U USER '//[IP]/[SHARE]'                 ---> Connect
- smbclient //<ip>/anonymous`                        ---> Find Files
- smbget -R smb://<ip>/anonymous                     ---> Download all available files
- smbclient -U milesdyson '\\10.10.33.22\milesdyson  ---> Example
```

- -U [name]     ---> Specify the user
- -p [port]        ---> Specify the port  


- SMB Terminal (Important commands)
```Temrinal
-  put              ---> Upload Text
-  get              ---> Download text
-  more             ---> Read text
```

- Exploit
	https://www.cvedetails.com/cve/CVE-2017-7494/


<h4>Windows Connection</h4>
- Crackmapexec (VERY GOOD)
```
crackmapexec smb IP -u '' -p '' -M spider_plus
crackmapexec smb IP -u 'guest' -p '' -M spider_plus
```

Trying no user and guest to see if enable on machine

- -M spider_plus       ---> Module in crackmapexec to map all directory we have read access and return the data in a json file
	- It should return the json file in the /tmp/cme_spider_plus/IP.json
	- You can then run the following command to see the result (cat /tmp/cme_spider_plus/IP.json |jq '. |map_values(keys)')


- SMBmap
```Terminal
smbmap -H IP -d DOMAIN.local -u ''  -p ''
```

- -u [name]     ---> Specify the user (empty = Anonymous)
- -p [port]        ---> Specify the port  (empty = Anonymous)
