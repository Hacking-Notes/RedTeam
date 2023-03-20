--- --- 

It is a common problem that many servers do not adequately check the host element in HTTP requests when processing incoming requests. This can lead to potentially exploitable vulnerabilities, particularly in the context of sensitive operations like password reset.

If you wish to attempt this exploit, you will first need to identify a webpage that allows you to reset your password. You can then use a tool like Burp Suite to intercept the HTTP request being sent to the server.

example:
![[Pasted image 20230316221831.png]]

Once you have intercepted the request, you can modify the host element to potentially exploit vulnerabilities in the server's password reset process. In some cases, the server may include the host element in the password reset link (IN THE EMAIL), making it possible for an attacker to intercept and gain access to the user's account.

Try the following

- Set the Host to your IP, setup netcat (-lvnp 80/443) and check if you have a response
- Setup a web server in burpsuite (Collaborator), Set the host to the collaborator address and wait for response

PS: <font color="Red">Take note that it is not necessary for the user to click on the email in order for this attack to be successful. Many email service providers use bots to automatically click on links and perform verification checks before the email is even delivered to the user's inbox.</font>

- Resole this issue
	Hard code the Host element, not a variable (In the JS)

More information ---> https://www.youtube.com/watch?v=wKcTELVst20