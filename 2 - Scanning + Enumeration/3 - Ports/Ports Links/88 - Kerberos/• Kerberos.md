--- ---
<h3>What is Kerberos</h3>
Kerberos is a network authentication protocol that is used to securely authenticate users and services on a network. Kerberos uses port 88 as its default port for communication between the Kerberos client and the Kerberos server.

When a user tries to log in to a Kerberos-secured system, the Kerberos client sends a ticket request to the Kerberos server on port 88. The Kerberos server then responds with a ticket granting ticket (TGT), which the Kerberos client can use to request service tickets from the Kerberos server for accessing various network services.

Port 88 is designated by the Internet Assigned Numbers Authority (IANA) as the standard port for Kerberos, and it is used for communication between Kerberos clients and servers on the network. However, it's important to note that Kerberos can also use other ports, such as 464 for password changing and 749 for administration purposes, depending on the configuration of the Kerberos implementation.

---
<h3>Find Kerberos Port</h3>
Nmap
```
nmap -sV -SC IP -p88
```

- Possible to find Kerberos on an other port

---
<h3>Attack Vectors</h3>
Kerberos often mean that this is the Domain Controler

More information ---> [Here]([[Red Team/6 - Machine/3 - Active Directory/Notes/Specific Topics/• Kerberos]])