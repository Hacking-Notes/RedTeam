--- ---
<h3>what is Netcat?</h3>
Netcat (often abbreviated as "nc") is a powerful networking tool that can be used to read and write data across network connections using TCP or UDP protocols. It is commonly used for troubleshooting network issues, as well as for performing network-related tasks such as port scanning, file transfers, and remote shell access.

---
<h3>Common use and commands:</h3>
First, you can connect to a server, as you did with Telnet, to collect its banner using `nc 10.10.248.159 PORT`, which is quite similar to our previous `telnet 10.10.248.159 PORT`. Note that you might need to press SHIFT+ENTER after the GET line.

- Example
	![[Screenshot_2022-09-01_22-27-07.png]]

	In the terminal shown above, we used netcat to connect to 10.10.248.159 port 80 using `nc 10.10.248.159 80`. Next, we issued a get for the default page using `GET / HTTP/1.1`; we are specifying to the target server that our client supports HTTP version 1.1. Finally, we need to give a name to our host, so we added on a new line, `host: netcat`; you can name your host anything as this has no impact on this exercise.

	Based on the output `Server: nginx/1.6.2` we received, we can tell that on port 80, we have Nginx version 1.6.2 listening for incoming connections.

Netcat
```Terminal
nc IP PORT

GET / HTTP/VERSION (check on website targeted what version they use)
host: netcat
```

---
<h3>More Information</h3>

For more information on Netcat, including additional commands and options, users can refer to the tool's documentation or the GitHub repository: [https://github.com/netcat/netcat](https://github.com/netcat/netcat)

<iframe src="https://github.com/netcat/netcat" width="100%" height="1300"></iframe>
