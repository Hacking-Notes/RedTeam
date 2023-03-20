--- ---
<h2>What is SMTP</h2>
SMTP stands for "Simple Mail Transfer Protocol". It is utilised to handle the sending of emails. In order to support email services, a protocol pair is required, comprising of SMTP and POP/IMAP. Together they allow the user to send outgoing mail and retrieve incoming mail, respectively.

The SMTP server performs three basic functions:

-    It verifies who is sending emails through the SMTP server.
-    It sends the outgoing mail
-    If the outgoing mail can't be delivered it sends the message back to the sender

Most people will have encountered SMTP when configuring a new email address on some third-party email clients, such as Thunderbird; as when you configure a new email client, you will need to configure the SMTP server configuration in order to send outgoing emails.

- **POP and IMAP**

	POP, or "Post Office Protocol" and IMAP, "Internet Message Access Protocol" are both email protocols who are responsible for the transfer of email between a client and a mail server. The main differences is in POP's more simplistic approach of downloading the inbox from the mail server, to the client. Where IMAP will synchronise the current inbox, with new mail on the server, downloading anything new. This means that changes to the inbox made on one computer, over IMAP, will persist if you then synchronise the inbox from another computer. The POP/IMAP server is responsible for fulfiling this process.  

- **How does SMTP work?**

	Email delivery functions much the same as the physical mail delivery system. The user will supply the email (a letter) and a service (the postal delivery service), and through a series of steps- will deliver it to the recipients inbox (postbox). The role of the SMTP server in this service, is to act as the sorting office, the email (letter) is picked up and sent to this server, which then directs it to the recipient.

	We can map the journey of an email from your computer to the recipient’s like this:

	![](https://github.com/TheRealPoloMints/Blog/blob/master/Security%20Challenge%20Walkthroughs/Networks%202/untitled.png?raw=true)

	1. The mail user agent, which is either your email client or an external program. connects to the SMTP server of your domain, e.g. smtp.google.com. This initiates the SMTP handshake. This connection works over the SMTP port- which is usually 25. Once these connections have been made and validated, the SMTP session starts.  
	
	2. The process of sending mail can now begin. The client first submits the sender, and recipient's email address- the body of the email and any attachments, to the server.  
	
	3. The SMTP server then checks whether the domain name of the recipient and the sender is the same.
	
	4. The SMTP server of the sender will make a connection to the recipient's SMTP server before relaying the email. If the recipient's server can't be accessed, or is not available- the Email gets put into an SMTP queue.  
	
	5. Then, the recipient's SMTP server will verify the incoming email. It does this by checking if the domain and user name have been recognised. The server will then forward the email to the POP or IMAP server, as shown in the diagram above.  
	
	6. The E-Mail will then show up in the recipient's inbox.

	This is a very simplified version of the process, and there are a lot of sub-protocols, communications and details that haven't been included. If you're looking to learn more about this topic, this is a really friendly to read breakdown of the finer technical details- I actually used it to write this breakdown:
	
	[https://computer.howstuffworks.com/e-mail-messaging/email3.htm](https://computer.howstuffworks.com/e-mail-messaging/email3.htm)

- **What runs SMTP?**

	SMTP Server software is readily available on Windows server platforms, with many other variants of SMTP being available to run on Linux.  

- **More Information:**

	Here is a resource that explain the technical implementation, and working of, SMTP in more detail than I have covered here.

	[https://www.afternerd.com/blog/smtp/](https://www.afternerd.com/blog/smtp/)

---
<h3>Find SMTP Port</h3>
Nmap
```
nmap -sV -SC IP -p25,587
```

- Possible to find SMTP on an other port

---
<h3>Attack</h3>
Two Possible ways to exploit SMPT
	- A user account name                                                                    ---> Enumeration & Metasploit
	- The type of SMTP server and Operating System running.         ---> Nmap and Metasploit

- Metasploit (BEST)
```
- msfconsole module ---> smtp_version
- msfconsole module ---> smtp_enum
```

- Enumeration
```Terminal
smtp-user-enum --help
smtp-user-enum -U /usr/share/wordlists/metasploit/unix_users.txt mail.example.tld 25
```

- smtp-user-enum       --->  Runs the tool  
- -U                               --->  Users List
- mail.example.tld        ---> SMTP Mail to attack 
- 25                               ---> Port

---
<h3>Connection</h3>
Telnet
```
telnet [ip] 25
```