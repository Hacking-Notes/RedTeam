--- ---

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
...
```