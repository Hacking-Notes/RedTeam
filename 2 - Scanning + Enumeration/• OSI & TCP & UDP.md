--- ---

<h2>General Information</h2>

- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)

---

<h2>OSI Model</2>

The OSI model consists of seven layers:

![Table showing the OSI layers: Application, Presentation, Session, Transport, Network, Data Link, Physical](https://muirlandoracle.co.uk/wp-content/uploads/2020/02/OSI-Table.png)

There are many mnemonics floating around to help you learn the layers of the OSI model -- search around until you find one that you like.

**P**lease **D**o **N**ot **T**ouch **S**teve's **P**et **A**lligator

- Layer 7 -- Application: (HTTP (GUI))

	The application layer of the OSI model essentially provides networking options to programs running on a computer. It works almost exclusively with applications, providing an interface for them to use in order to transmit data. When data is given to the application layer, it is passed down into the presentation layer.  

- Layer 6 -- Presentation: (Translate, Transform & encrypt data)

	The presentation layer receives data from the application layer. This data tends to be in a format that the application understands, but it's not necessarily in a standardised format that could be understood by the application layer in the _receiving_ computer. The presentation layer translates the data into a standardised format, as well as handling any encryption, compression or other transformations to the data. With this complete, the data is passed down to the session layer.

- Layer 5 -- Session: (Create Sessions, Synchronise, Send parkets (Parts of the data))

	When the session layer receives the correctly formatted data from the presentation layer, it looks to see if it can set up a connection with the other computer across the network. If it can't then it sends back an error and the process goes no further. If a session _can_ be established then it's the job of the session layer to maintain it, as well as co-operate with the session layer of the remote computer in order to synchronise communications. The session layer is particularly important as the session that it creates is unique to the communication in question. This is what allows you to make multiple requests to different endpoints simultaneously without all the data getting mixed up (think about opening two tabs in a web browser at the same time)! When the session layer has successfully logged a connection between the host and remote computer the data is passed down to Layer 4: the transport Layer.

- Layer 4 -- Transport: (TCP, UDP - Receive data (TCP Slow - Accurate + Synchronise) (UDP Fast - No check Up))

	The transport layer is a very interesting layer that serves numerous important functions. Its first purpose is to choose the protocol over which the data is to be transmitted. The two most common protocols in the transport layer are TCP (**T**ransmission **C**ontrol **P**rotocol) and UDP (**U**ser **D**atagram **P**rotocol); with TCP the transmission is _connection-based_ which means that a connection between the computers is established and maintained for the duration of the request. This allows for a reliable transmission, as the connection can be used to ensure that the packets _all_ get to the right place. A TCP connection allows the two computers to remain in constant communication to ensure that the data is sent at an acceptable speed, and that any lost data is re-sent. With UDP, the opposite is true; packets of data are essentially thrown at the receiving computer -- if it can't keep up then that's _its_ problem (this is why a video transmission over something like Skype can be pixelated if the connection is bad). What this means is that TCP would usually be chosen for situations where accuracy is favoured over speed (e.g. file transfer, or loading a webpage), and UDP would be used in situations where speed is more important (e.g. video streaming).

	With a protocol selected, the transport layer then divides the transmission up into bite-sized pieces (over TCP these are called _segments_, over UDP they're called _datagrams_), which makes it easier to transmit the message successfully. 

- Layer 3 -- Network: (Route data to computer via IP (optimal path) & reassemble data)

	The network layer is responsible for locating the destination of your request. For example, the Internet is a huge network; when you want to request information from a webpage, it's the network layer that takes the IP address for the page and figures out the best route to take. At this stage we're working with what is referred to as _Logical_ addressing (i.e. IP addresses) which are still software controlled. Logical addresses are used to provide order to networks, categorising them and allowing us to properly sort them. Currently the most common form of logical addressing is the IPV4 format, which you'll likely already be familiar with (i.e 192.168.1.1 is a common address for a home router).

- Layer 2 -- Data Link: (Receives packet from the network layer (including the IP) and adds in the physical **MAC** address

	The data link layer focuses on the _physical_ addressing of the transmission. It receives a packet from the network layer (that includes the IP address for the remote computer) and adds in the physical (MAC) address of the receiving endpoint. Inside every network enabled computer is a Network Interface Card (NIC) which comes with a unique MAC (Media Access Control) address to identify it.

	MAC addresses are set by the manufacturer and literally burnt into the card; they can't be changed -- although they _can_ be spoofed. When information is sent across a network, it's actually the physical address that is used to identify where exactly to send the information.

	Additionally, it's also the job of the data link layer to present the data in a format suitable for transmission.

	The data link layer also serves an important function when it receives data, as it checks the received information to make sure that it hasn't been corrupted during transmission, which could well happen when the data is transmitted by layer 1: the physical layer.

- Layer 1 -- Physical: (Physical components of the hardware used in networking, Include 0's and 1's)

	The physical layer is right down to the hardware of the computer. This is where the electrical pulses that make up data transfer over a network are sent and received. It's the job of the physical layer to convert the binary data of the transmission into signals and transmit them across the network, as well as receiving incoming signals and converting them back into binary data.

---

<h2>TCP/IP</h2>

The TCP/IP model is, in many ways, very similar to the OSI model. It's a few years older, and serves as the basis for real-world networking. The TCP/IP model consists of four layers: Application, Transport, Internet and Network Interface. Between them, these cover the same range of functions as the seven layers of the OSI Model.

![The layesrs of the TCP/IP model: Application, Transport,Internet, Network Interface](https://muirlandoracle.co.uk/wp-content/uploads/2020/02/image-4.png)

_**Note:** Some recent sources split the TCP/IP model into five layers -- breaking the Network Interface layer into Data Link and Physical layers (as with the OSI model). This is accepted and well-known; however, it is not officially defined (unlike the original four layers which are defined in RFC1122). It's up to you which version you use -- both are generally considered valid._  

You would be justified in asking why we bother with the OSI model if it's not actually used for anything in the real-world. The answer to that question is quite simply that the OSI model (due to being less condensed and more rigid than the TCP/IP model) tends to be easier for learning the initial theory of networking.  

The two models match up something like this:

![Comparison between the TCP/IP and OSI models.](https://muirlandoracle.co.uk/wp-content/uploads/2020/02/image-3.png)

The processes of encapsulation and de-encapsulation work in exactly the same way with the TCP/IP model as they do with the OSI model. At each layer of the TCP/IP model a header is added during encapsulation, and removed during de-encapsulation.

![[Pasted image 20221111195138.png]]

![[Pasted image 20221111195335.png]]

<h3>Handshake</h3>

The TCP (Transmission Control Protocol) handshake is a process that occurs between two devices in a network when they want to establish a connection. It involves exchanging a series of messages between the devices to establish a reliable connection for the exchange of data.

The TCP handshake consists of three steps:

1.  **SYN**: The initiating device sends a SYN (synchronize) message to the receiving device, indicating its intention to establish a connection.
    
2.  **SYN-ACK**: The receiving device responds with a SYN-ACK (synchronize-acknowledge) message, acknowledging the receipt of the SYN message and indicating its own intention to establish a connection.
    
3.  **ACK**: The initiating device sends an ACK (acknowledge) message in response to the SYN-ACK, completing the handshake and establishing the connection.
    

The purpose of the TCP handshake is to ensure that both devices are ready to communicate with each other and that the connection between them is reliable. It also helps to prevent data loss by ensuring that both devices are in sync with each other before transmitting data.

![[Pasted image 20221227193634.png]]

---

<h2>UDP/IP</h2>

The **U**ser **D**atagram **P**rotocol (**UDP**) is another protocol that is used to communicate data between devices.

Unlike its brother TCP, UDP is a **stateless** protocol that doesn't require a constant connection between the two devices for data to be sent. For example, the Three-way handshake does not occur, nor is there any synchronisation between the two devices.

Recall some of the comparisons made about these two protocols in Room 3: "OSI Model". Namely, UDP is used in situations where applications can tolerate data being lost (such as video streaming or voice chat) or in scenarios where an unstable connection is not the end-all. A table comparing the advantages and disadvantages of UDP is located below:

  
As mentioned, no process takes place in setting up a connection between two devices. Meaning that there is no regard for whether or not data is received, and there are no safeguards such as those offered by TCP, such as data integrity.

UDP packets are much simpler than TCP packets and have fewer headers. However, both protocols share some standard headers, which are what is annotated in the table below:

![[Pasted image 20221111195513.png]]

<h3>UDP Handshake</h3>

the UDP (User Datagram Protocol) does not use a handshake process to establish a connection. UDP is a connectionless protocol, which means that it does not establish a connection before sending data and does not expect an acknowledgement of receipt from the receiving device.

Instead, UDP relies on the IP (Internet Protocol) layer to handle the delivery of data packets between devices. When a device sends a UDP packet, it includes the destination IP address and port number, and the packet is sent to the destination device. There is no guarantee that the packet will be received, and there is no mechanism for retransmitting lost packets.

UDP is often used for real-time applications that require low latency and do not need to guarantee the delivery of data. Examples include online gaming, voice over IP (VoIP), and streaming audio and video.