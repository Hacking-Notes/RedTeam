--- ---
<h3>Start with passive reconnaissance</h3>
Gather as much information as possible about the target system using passive methods, such as DNS queries, ping, and WHOIS lookups. This will help you identify potential targets, hosts, and other useful information about the system. Some tools that you can use include:

- DNS: Use tools like `dig`, `dnsdumper`, `nslookup`, `shodan`, and SSL/TLS certificates to gather information about the target's DNS records, SSL/TLS certificates, and other network-related information.

- Ping: Use the `ping` command to identify the IP address of the target system and its time-to-live (TTL) value, which can help you identify the type of operating system and network architecture in use.

- WHOIS: Use the `whois` command to gather information about the domain name, such as registration details, owner information, and contact details.

---
<h3>Active Reconnaissance</h3>
Once you have gathered enough information about the target system, you can move on to active reconnaissance. This involves using tools that actively scan the target network to identify vulnerabilities and potential entry points. Some tools that you can use include:

- AMASS: This tool is used to discover subdomains and gather information about them. You can use it to search for DNS records, IP addresses, and other network-related information.

- Netcat: This tool is used to create TCP/UDP connections between two hosts, and can be used to test for open ports, perform banner grabbing, and other tasks.

- Telnet: This tool is used to connect to remote hosts and execute commands on them. It can be used to test for open ports, brute force passwords, and other tasks.

- Traceroute: This tool is used to trace the path that network packets take from the source to the destination. It can be used to identify routers, firewalls, and other network devices in the path.

---
<h3>Put it all together</h3>
Once you have gathered all the information you need using both passive and active reconnaissance, you can use this information to plan your attack. Use the information you have gathered to identify potential vulnerabilities, entry points, and other weaknesses in the system. You can then use this information to launch targeted attacks and gain access to the system.



















<h2>Global Steps</h2>

Whois Records
```
whois DOMAIN
```

NameServer (From Whois Record)                              ---> Manual Way
```
dig +short @NAME-SERVER A DOMAIN
dig +short @NAME-SERVER MX DOMAIN
dig +short @NAME-SERVER ... DOMAIN
```

NameServer Enumeration (From Whois Record)        ---> Automated Way
```
sudo nmap --dns-servers NAME-SERVER(Without @) --script dns-brute --script-args dns-brute.domain=DOMAIN
```

- Possible to add a specific wordlist

Osint Enumeration
```
# Osint Enumeration
AMASS
DNSdumper
crt.sh
...
```