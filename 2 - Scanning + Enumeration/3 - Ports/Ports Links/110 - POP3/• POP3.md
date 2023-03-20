--- ---

<h2>What is POP3</h2>

Post Office Protocol version 3 (POP3) is a protocol used to download the email messages from a Mail Delivery Agent (MDA) server, as shown in the figure below. The mail client connects to the POP3 server, authenticates, downloads the new email messages before (optionally) deleting them.

- More Information
	![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/ed910ad418376edc846846fc2a0dd3f6.png)
	
	The example below shows what a POP3 session would look like if conducted via a Telnet client. First, the user connects to the POP3 server at the POP3 default port 110. Authentication is required to access the email messages; the user authenticates by providing his username `USER frank` and password `PASS D2xc9CgD`. Using the command `STAT`, we get the reply `+OK 1 179`; based on [RFC 1939](https://datatracker.ietf.org/doc/html/rfc1939), a positive response to `STAT` has the format `+OK nn mm`, where _nn_ is the number of email messages in the inbox, and _mm_ is the size of the inbox in octets (byte). The command `LIST` provided a list of new messages on the server, and `RETR 1` retrieved the first message in the list. We don’t need to concern ourselves with memorizing these commands; however, it is helpful to strengthen our understanding of such protocol.
	
	Pentester Terminal
	
	```shell-session
	pentester@TryHackMe$ telnet 10.10.142.15 110
	Trying 10.10.142.15...
	Connected to MACHINE_IP.
	Escape character is '^]'.
	+OK MACHINE_IP Mail Server POP3 Wed, 15 Sep 2021 11:05:34 +0300 
	USER frank
	+OK frank
	PASS D2xc9CgD
	+OK 1 messages (179) octets
	STAT
	+OK 1 179
	LIST
	+OK 1 messages (179) octets
	1 179
	.
	RETR 1
	+OK
	From: Mail Server 
	To: Frank 
	subject: Sending email with Telnet
	Hello Frank,
	I am just writing to say hi!
	.
	QUIT
	+OK MACHINE_IP closing connection
	Connection closed by foreign host.
	```
	
	The example above shows that the commands are sent in cleartext. Using Telnet was enough to authenticate and retrieve an email message. As the username and password are sent in cleartext, any third party watching the network traffic can steal the login credentials.

---
<h3>Find POP3 Port</h3>
Nmap
```
nmap -sV -SC IP -p110
```

- Possible to find POP3 on an other port

---
<h3>Connection</h3>
- Telnet
```Terminal
telnet [ip] 110
```

- POP3 Commands
```Terminal
USER frank
+OK frank                             #Machine Response
PASS D2xc9CgD
+OK 1 messages (179) octets           #Machine Response
STAT
+OK 1 179                             #Machine Response
LIST
+OK 1 messages (179) octets           #Machine Response
1 179
.
RETR 1
+OK                                   #Machine Response
From: Mail Server 
To: Frank 
subject: Sending email with Telnet
Hello Frank,
I am just writing to say hi!
.
QUIT
+OK MACHINE_IP closing connection     #Machine Response
Connection closed by foreign host.
```
