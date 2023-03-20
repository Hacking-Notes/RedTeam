--- ---
<h2>What is DNS</h2>
DNS (Domain Name System) uses port 53 as its default port for communication between DNS clients and DNS servers. When a DNS client, such as a web browser or email client, needs to resolve a domain name into an IP address, it sends a DNS query to a DNS server using UDP or TCP on port 53.

DNS servers typically listen for incoming queries on port 53 and respond with the corresponding IP address or other DNS records, such as MX records for email servers or TXT records for domain verification.

Port 53 is designated by the Internet Assigned Numbers Authority (IANA) as the standard port for DNS, and it is widely used on the internet for DNS communication between clients and servers.

---
<h3>Find DNS Port</h3>
Nmap
```
nmap -sV -SC IP -p53
```

- Possible to find DNS on an other port

---
<h3>Connection</h3>
- Telnet
```Terminal
telnet [ip] 53
```

- Using Nslookup or Dig
```Terminal
dig www.example.com A
nslookup www.example.com A
...
```

- A ---> A record (DNS query we want information on)

--- 
<h3>Attack</h3>
If an attacker is able to access an open port 53 (DNS) on a target system, they may be able to perform a variety of actions, depending on the configuration of the DNS server. Some possible actions an attacker could take include:

1.  Perform DNS spoofing attacks:           ---> Redirect users to fake websites or intercept sensitive data being transmitted over the network.
    
2.  Conduct DNS amplification attacks     ---> (DoS) attack.
    
3.  Enumerate domain names                    ---> DNS zone transfers (List of all the domain names registered on a particular DNS server)

<h4>Check Zone Info</h4>
One way to send a DNS query using `telnet` to converts a DNS query into binary format, such as `dig` or `nslookup`. Here is an example of how you can use `dig` to send a DNS query for an A record for the domain `www.example.com`:

- Searching trought the DNS using DIG
```
dig www.example.com A
dig www.example.com CNAME
```

<h4>DNS Zone Transfer</h4>
To exploit a DNS zone transfer, you will need to know the IP address of the DNS server you want to request the records from and the name of the zone you want to transfer.

Here is an example of how you can use `dig` to request a DNS zone transfer from a DNS server:

- DNS zone transfer
```
dig @[DNS server IP] [zone] axfr
dig axfr [domain] @[DNS server]

host -t ns [domain]
host -l [domain] @[DNS server]
```

Replace `[DNS server IP]` with the IP address of the DNS server and `[zone]` with the name of the zone you want to transfer.

Replace `[domain]` with the domain for which you want to perform the zone transfer, and `[DNS server]` with the IP address or hostname of the DNS server that you want to query.


**TAKE NOTES THAT IT IS NOT POSSIBLE TO MODIFY DNS RECORDS BY ACCESSING AN OPEN PORT 53. PORT 53 IS THE STANDARD PORT USED FOR DNS QUERIES AND RESPONSES, AND IS USED TO COMMUNICATE BETWEEN DNS CLIENTS (SUCH AS WEB BROWSERS) AND DNS SERVERS**