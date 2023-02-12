--- ---

<h2>Subdomain TakeOver</h2>

Use some subdomain enumeration technique to find more subdomain
- [[Red Team/2 - Scanning + Enumeration/2 - Enumeration/Subdomain/• Gobuster]]
- [[Red Team/2 - Scanning + Enumeration/2 - Enumeration/Subdomain/• Google Dorking]]
- [[Red Team/2 - Scanning + Enumeration/2 - Enumeration/Subdomain/• AMASS]]

Merge all subdomain found in one document
```
# Merging subdomains into one file  
cat google_subs.txt amass_passive_subs.txt gobuster_subs.txt | anew subdomains.txt
```

Use httpx (https://github.com/projectdiscovery/httpx) to search the CNAME
```
httpx -l subdomains.txt -cname cnames.txt
```

Check for live server (this will tell you witch subdomain are not active anymore)
```
httpx -l subdomains.txt -p 80,443,8080,3000 -status-code -title -o servers_details.txt
```

Analyse the output and search for domain that point to general platform
More information ---> https://infosecwriteups.com/fastly-subdomain-takeover-2000-217bb180730f

---

<h2>Automated Way (Less Reliable)</h2>

**Tool** ---> https://github.com/0xKaran/sub-domain-takeover

```
$ python3 takeover.py -d www.domain.com -v 
$ python3 takeover.py -d www.domain.com -v -t 30
$ python3 takeover.py -d www.domain.com -p http://127.0.0.1:8080 -v 
$ python3 takeover.py -d www.domain.com -o <output.txt> or <output.json> -v 
$ python3 takeover.py -l uber-sub-domains.txt -o output.txt -p http://xxx.xxx.xxx.xxx:8080 -v 
$ python3 takeover.py -d uber-sub-domains.txt -o output.txt -T 3 -v 
```


**Exemple**
Shopify Vulnerability subdomain take over

- Find domain using the service (shopify)
- Search for its subdomains with virustotal or crt.sh
- Search for 404 status (https://httpstatus.io)
- Check canaical name ---> nslookup (terminal)
- Create an account on the service (shopify) and register the subdomain

---

<h2>What is Subdomain takeover</h2>

Sub-domain takeover vulnerability occur when a sub-domain (**subdomain.example.com**) is pointing to a service (e.g: **GitHub**, **AWS/S3**,..) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that sub-domain. For example, if **subdomain.example.com** was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a **CNAME** file containing **subdomain.example.com**, and claim **subdomain.example.com**. For more information: [here](https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/)
