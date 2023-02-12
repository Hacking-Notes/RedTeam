--- ---

<h2>General</h2>

Burp's Platform Authentication feature allows users to configure the software to automatically authenticate with destination web servers. This can be useful for automating tasks and simplifying the process of interacting with servers that require authentication. In this context, the specific authentication type being discussed is Windows Challenge/Response (NTLM), which is a protocol used for authentication on networks and systems running the Windows operating system. The article describes how to configure Burp Suite to work with an application that uses NTLM authentication.

---

<h2>Commands</h2>

NTLM credentials are based on data obtained during the interactive logon process and consist of a domain name, a user name, and a one-way hash of the user's password.

When an application is using NTLM authentication, you will need to configure Burp Suite to automatically carry out the authentication process.

You can configure these settings at User Options > Connections > Platform Authentication.

Use the Add function to configure new credentials.

![[Pasted image 20230105192616.png]]

Select the correct authentication type and add the appropriate credentials.

![[Pasted image 20230105192712.png]]

With the credentials configured correctly, Burp automatically carries out the NTLM authentication, allowing access to the destination application web server.

Video ---> https://d21v5rjx8s17cr.cloudfront.net/support/videos/1080_Using_NTLM.mp4