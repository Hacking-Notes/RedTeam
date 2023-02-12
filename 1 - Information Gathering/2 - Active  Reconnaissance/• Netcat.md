--- ---

<h2>Top commands</h2>

Ping
```Terminal
nc IP PORT

GET / HTTP/VERSION (check on website targeted what version they use)
host: netcat
```

---

<h2>Netcat</h2>

Netcat or simply `nc` has different applications that can be of great value to a pentester. Netcat supports both TCP and UDP protocols. It can function as a client that connects to a listening port; alternatively, it can act as a server that listens on a port of your choice. Hence, it is a convenient tool that you can use as a simple client or server over TCP or UDP.

First, you can connect to a server, as you did with Telnet, to collect its banner using `nc 10.10.248.159 PORT`, which is quite similar to our previous `telnet 10.10.248.159 PORT`. Note that you might need to press SHIFT+ENTER after the GET line.

- Example
	![[Screenshot_2022-09-01_22-27-07.png]]

	In the terminal shown above, we used netcat to connect to 10.10.248.159 port 80 using `nc 10.10.248.159 80`. Next, we issued a get for the default page using `GET / HTTP/1.1`; we are specifying to the target server that our client supports HTTP version 1.1. Finally, we need to give a name to our host, so we added on a new line, `host: netcat`; you can name your host anything as this has no impact on this exercise.

	Based on the output `Server: nginx/1.6.2` we received, we can tell that on port 80, we have Nginx version 1.6.2 listening for incoming connections.