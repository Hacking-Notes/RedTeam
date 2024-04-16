--- ---
<h3>what is Telnet?</h3>
Telnet is a network protocol used to provide remote access to a device over a network connection. It allows a user to connect to and interact with a remote device as if they were physically present at the device's console. Telnet is commonly used for remote management of devices such as routers, switches, and servers.

---
<h3>Common use and commands:</h3>
The most common use of Telnet is to establish a connection to a remote device's command-line interface (CLI). To do so, the user opens a Telnet client application and enters the IP address or hostname of the remote device. Once the connection is established, the user can enter commands as if they were sitting at the device's console.

However, the telnet client, with its simplicity, can be used for other purposes. Knowing that telnet client relies on the TCP protocol, you can use Telnet to connect to any service and grab its banner. Using `telnet MACHINE_IP PORT`, you can connect to any service running on TCP and even exchange a few messages unless it uses encryption.

- example
	Let’s say we want to discover more information about a web server, listening on port 80. We connect to the server at port 80, and then we communicate using the HTTP protocol. You don’t need to dive into the HTTP protocol; you just need to issue `GET / HTTP/1.1`. To specify something other than the default index page, you can issue `GET /page.html HTTP/1.1`, which will request `page.html`. We also specified to the remote web server that we want to use HTTP version 1.1 for communication. To get a valid response, instead of an error, you need to input some value for the host `host: example` and hit enter twice. Executing these steps will provide the requested index page.

	![[Screenshot_2022-09-01_22-13-27.png]]

Telnet
```Terminal
Telnet IP PORT
```

---
<h3>More Information</h3>
For more information on Telnet, including how to configure Telnet clients and troubleshoot Telnet connections, users can refer to the tool's documentation or online resources such as TechTarget or Cisco's website. Additionally, the source code for many Telnet clients and servers is available on GitHub: [https://github.com/topics/telnet](https://github.com/topics/telnet).

<iframe src="https://github.com/topics/telnet" width="100%" height="1300"></iframe>