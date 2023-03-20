--- ---
<h2>What is FTP</h2>

File Transfer Protocol (FTP) is, as the name suggests , a protocol used to allow remote transfer of files over a network. It uses a client-server model to do this, and- as we'll come on to later- relays commands and data in a very efficient way.  

- How does FTP work?****

	A typical FTP session operates using two channels:

	-   a command (sometimes called the control) channel
	-   a data channel.

	As their names imply, the command channel is used for transmitting commands as well as replies to those commands, while the data channel is used for transferring data.

	FTP operates using a client-server protocol. The client initiates a connection with the server, the server validates whatever login credentials are provided and then opens the session.

	While the session is open, the client may execute FTP commands on the server.  

- Active vs Passive

	The FTP server may support either Active or Passive connections, or both. 

	-   In an Active FTP connection, the client opens a port and listens. The server is required to actively connect to it. 
	-   In a Passive FTP connection, the server opens a port and listens (passively) and the client connects to it. 

	This separation of command information and data into separate channels is a way of being able to send commands to the server without having to wait for the current data transfer to finish. If both channels were interlinked, you could only enter commands in between data transfers, which wouldn't be efficient for either large file transfers, or slow internet connections.

- **More Details:**

	You can find more details on the technical function, and implementation of, FTP on the Internet Engineering Task Force website: [https://www.ietf.org/rfc/rfc959.txt](https://www.ietf.org/rfc/rfc959.txt). The IETF is one of a number of standards agencies, who define and regulate internet standards.

---
<h3>Find FTP Port</h3>
Nmap
```
nmap -sV -SC IP -p20,21
```

- Possible to find FTP on an other port

---
<h3>Attack</h3>
- Brute Force
```Terminal
hydra -t X -l USERNAME -P WORDLIST -vV IP ftp
```

Let's break it down:

- hydra      --->  Runs the hydra tool  
- -t X         --->  Number of parallel connections per target  
- -l             ---> Points to the user who's account you're trying to compromise  
- -P            ---> Points to the file containing the list of possible passwords  
- -vV          ---> Sets verbose mode to very verbose, shows login + password 
- IP             ---> The IP address of the target machine  
- ftp           --->  Sets the protocol

---
<h3>Connection</h3>
- Connection
```
ftp [options] [IP]
```
