--- ---
<h3>What is Gobuster?</h3>

Gobuster is an open-source command-line tool used for directory and DNS subdomain brute-forcing. It allows users to discover hidden files and directories on a web server, and find subdomains on a given domain.

The tool works by sending HTTP/HTTPS requests to the web server or DNS queries to the domain name server, and analyzes the responses to determine if there are any hidden files, directories or subdomains.

---
<h4>Common Use and Commands:</h4>
Gobuster is commonly used by security researchers, penetration testers and system administrators to identify potential security vulnerabilities and weaknesses in web applications.

The following are some common commands used in Gobuster:

Scan for directories: 
```
gobuster dir -u <url> -w <wordlist>
```

Scan for subdomains:
```
gobuster dns -d <domain> -w <wordlist>
```

Gobuster supports multiple options and flags to customize the scan, such as setting the user-agent, specifying the proxy, setting the timeout and enabling recursion.

---
<h3>More Information</h3>

For more information on Gobuster, including the latest updates and documentation, please visit the project's official Github repository: https://github.com/OJ/gobuster

<iframe src="https://github.com/OJ/gobuster" width="100%" height="1300"></iframe>