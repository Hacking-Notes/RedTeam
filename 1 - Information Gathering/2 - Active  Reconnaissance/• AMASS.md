--- ---
<h3>What is Amass?</h3>
Amass is a popular open-source tool used for reconnaissance and enumeration during security assessments. It is designed to discover and map external assets of an organization, including subdomains, IP addresses, and associated metadata.

The tool utilizes a combination of active and passive reconnaissance techniques, including DNS and zone transfers, web scraping, and web archive searching. It also integrates with various third-party data sources, such as Shodan, Censys, and VirusTotal, to enhance the accuracy and completeness of its findings.

Amass can be used to enumerate APIs, identify SSL/TLS certificates, perform DNS reconnaissance, map network routes, scrape web pages, search web archives, and obtain WHOIS information. It is commonly used by security professionals, bug bounty hunters, and penetration testers to gather information about their target organization and identify potential attack vectors.

---
<h4>Common Use and Commands:</h4>
Amass is commonly used by security professionals, bug bounty hunters, and penetration testers to gather information about their target organization and identify potential attack vectors.

The following are some common commands used in Amass:

<h4>Subdomain Enumeration:</h4>
-  Perform a DNS enumeration: `amass enum -d <domain>`
-   To use passive DNS enumeration: `amass enum --passive -d <domain>`
-   To use active DNS enumeration: `amass enum --active -d <domain>`
-   To perform subdomain bruteforcing: `amass enum -d <domain> -brute`

<h4>Directory Enumeration:</h4>
-   To brute-force directories and files: `amass enum -active -d <domain> -w <wordlist>`
-   To brute-force directories with a defined extension: `amass enum -active -d <domain> -w <wordlist> -dirsearch /path/to/extensions`
-   To find URLs with HTTP response code 200: `amass enum -active -d <domain> -w <wordlist> -status-code 200`

<h4>API Discovery:</h4>
-   To discover APIs using passive techniques: `amass intel -d <domain> -api`
-   To discover APIs using active techniques: `amass intel -d <domain> -api -active`
-   To use a custom API key for Shodan: `amass intel -d <domain> -shodan-apikey <API-key>`

Amass supports various options and flags to customize the scan, such as setting the output format, configuring rate limits, and enabling verbose logging.

---
<h3>More Information</h3>
For more information on Amass, including the latest updates and documentation, please visit the project's official Github repository: https://github.com/OWASP/Amass

<iframe src="https://github.com/OWASP/Amass" width="100%" height="1300"></iframe>