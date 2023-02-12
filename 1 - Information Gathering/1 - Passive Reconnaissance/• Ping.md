--- ---

<h2>Top commands</h2>

Ping
```Terminal
ping -c X IP
```

- -c                    ---> Number of ping sent

TTL response from the ping might give some infromation about the operating system
- Linux                       ---> 64 or less
- Windows                 ---> 128
- Cisco                       ---> 128 - 256

---

<h2>What is Ping</h2>

The ping command is used when we want to test whether a connection to a remote resource is possible. Usually this will be a website on the internet, but it could also be for a computer on your home network if you want to check if it's configured correctly. Ping works using the ICMP protocol, which is one of the slightly less well-known TCP/IP protocols that were mentioned earlier. The ICMP protocol works on the Network layer of the OSI Model, and thus the Internet layer of the TCP/IP model. The basic syntax for ping is `ping <target>`. In this example we are using ping to test whether a network connection to Google is possible:

![Pinging Google -- it is possible](https://muirlandoracle.co.uk/wp-content/uploads/2020/03/image-14.png)

Notice that the ping command actually returned the IP address for the Google server that it connected to, rather than the URL that was requested. This is a handy secondary application for ping, as it can be used to determine the IP address of the server hosting a website. One of the big advantages of ping is that it's pretty much ubiquitous to any network enabled device. All operating systems support it out of the box, and even most embedded devices can use ping!  

Have a go at the following questions. Any questions about syntax can be answered using the man page for ping (`man ping` on Linux).