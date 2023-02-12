--- ---

<h2>General</h2>

LDAP (Lightweight Directory Access Protocol) is a protocol for accessing and maintaining distributed directory information services over an Internet Protocol (IP) network. It is used to access and manage directory information that is organized in a hierarchical manner, similar to a file system. LDAP directories are commonly used to store information such as user names, passwords, and email addresses, as well as other types of information such as security certificates and encryption keys.

LDAP is based on the X.500 standard and can be used to authenticate users and to provide access to resources on a network. When a client application needs to authenticate a user or retrieve information from the directory, it sends a request to the LDAP server using the LDAP protocol. The LDAP server processes the request and returns the requested information to the client if the request is valid.

LDAP servers provide a centralized location for storing and managing directory information, and client applications can use LDAP to query the directory and retrieve the information they need. LDAP is often used in conjunction with other protocols, such as Kerberos, to provide secure authentication and authorization services for a network.

To protect the confidentiality of the information being transmitted over the network, LDAP can be configured to use Secure Sockets Layer (SSL) or Transport Layer Security (TLS) to encrypt the connection between the client and the server. This ensures that the information is not visible to any third parties who might be able to intercept the network traffic.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/6093e17fa004d20049b6933e/room-content/d2f78ae2b44ef76453a80144dac86b4e.png)  

LDAP authentication is a popular mechanism with third-party (non-Microsoft) applications that integrate with AD. These include applications and systems such as:

-   Gitlab
-   Jenkins
-   Custom-developed web applications
-   Printers
-   VPNs
  
  ===If you could gain a foothold on the correct host, such as a Gitlab server, it might be as simple as reading the configuration files to recover these AD credentials. These credentials are often stored in plain text in configuration files since the security model relies on keeping the location and storage configuration file secure rather than its contents.===

- Example
	Imagine that you have a bunch of cards, each with a different person's name on it. You also have a bunch of folders, each with a different topic written on it. You want to keep track of which people know about which topics, so you put the cards with the names of the people who know about a particular topic into the folder with the same topic written on it.
	
	Now, let's say that your friend comes over and wants to know who knows about a certain topic. You could go through all of the folders one by one and look at the cards inside to see which people know about that topic. But that would be very time-consuming and not very efficient.
	
	Instead, you can use LDAP to help you find the information faster. LDAP is like a special set of rules that you can use to search for the information you need in a more organized way. For example, you can use LDAP to search for all the cards in the "math" folder by typing "math" into a search bar. LDAP will then go through all of the folders and find the "math" folder for you. You can also use LDAP to search for specific people by name, or to find out which topics a particular person knows about.
	
	In this example, the cards with the names on them would be like the pieces of information stored in an LDAP directory, and the folders with the topics written on them would be like the different categories or "organizational units" in the directory. The LDAP protocol would be like the set of rules you use to search for the information you need.