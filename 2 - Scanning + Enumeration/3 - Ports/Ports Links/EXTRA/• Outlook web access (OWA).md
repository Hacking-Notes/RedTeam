--- ---
<h3>What is OWA</h3>
Microsoft Exchange Server mailbox provides a web-based interface that allows users to access their email, calendar, tasks, and other Exchange Server features from anywhere with an internet connection.

OWA is often used in situations where users cannot access their email client on their desktop, such as when they are traveling or working remotely. It is also used in environments where email access is restricted, such as in corporate settings where access to email servers is restricted from outside the corporate network.

OWA provides a similar experience to using the Outlook desktop application, including features such as drag-and-drop functionality, rich formatting options, and the ability to view and edit attachments. It is commonly used in organizations of all sizes, from small businesses to large enterprises.

---
<h3>Find RDP ports</h3>
- Nmap
```Terminal
nmap -sV -sC IP -p443
```

- Possible to find OWA on an other port

---
<h3>Attack</h3>
- Brute Force
	- https://github.com/byt3bl33d3r/SprayingToolkit
	- https://github.com/dafthack/MailSniper