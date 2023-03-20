--- ---

Subdomain enumeration is the process of identifying all subdomains of a given domain. This can be done using various tools, such as recon-ng, dnsrecon, and Sublist3r. 

Some common methods used in subdomain enumeration include using search engines, brute-force techniques, and scraping website pages. The goal of subdomain enumeration is to identify subdomains that may contain vulnerabilities or sensitive information that can be used in further attacks.

Gobuster
```
gobuster vhost -u <target_url> -w <wordlist_file>
```

ffuf
```
ffuf -H "Host: FUZZ.domain.com" -H "User-Agent: Vhost Finder" -c -w /usr/share/seclists/Discovery/DNScombined_subdomains.txt -u http://domain.com
```