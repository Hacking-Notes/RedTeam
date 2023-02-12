--- ---

<h2>Find Telnet Port</h2>

Nmap
```
nmap -sV -SC IP -p23
```

- Possible to find Telnet on an other port

---

<h2>Connection</h2>

Telnet
```Terminal
telnet [ip] [port]
```

- IP                         ---> Target IP
- PORT                   ---> Port we want to interact with (example -> 110)

Exploit CVE
-   [https://www.cvedetails.com/](https://www.cvedetails.com/)
-   [https://cve.mitre.org/](https://cve.mitre.org/)[](https://cve.mitre.org/)

---

<h2>What is Telnet</h2>

- **What is Telnet?**

	Telnet is an application protocol which allows you, with the use of a telnet client, to connect to and execute commands on a remote machine that's hosting a telnet server.  

	The telnet client will establish a connection with the server. The client will then become a virtual terminal- allowing you to interact with the remote host.  

- **Replacement**  

	Telnet sends all messages in clear text and has no specific security mechanisms. Thus, in many applications and services, Telnet has been replaced by SSH in most implementations.  
   
- **How does Telnet work?**

	The user connects to the server by using the Telnet protocol, which means entering **"telnet"** into a command prompt. The user then executes commands on the server by using specific Telnet commands in the Telnet prompt. You can connect to a telnet server with the following syntax: **"telnet [ip] [port]"**