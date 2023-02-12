--- ---

<h2>NMAP</h2>

While searching for API's, Nmap will allow you to find http server that can help you forther more to enumerate and find information about the targeted API

---

<h2>AMASS</h2>

AMASS allow you to gather information from various source to enumerate a website or in this case an API

You can also try to get an API key (from a website/service that offer you one and sync it with amass to find all the possibiliy of this API) and insert it in the command.

```
amass enum -list
amass enum -active -d TARGET | grep api (OPTIONAL)  ---> Will expose API Subdomains
```

More information ---> [[Red Team/1 - Information Gathering/2 - Active  Reconnaissance/• AMASS]]

---

<h2>Directory Brute Force (Gobuster)</h2>

Gobuster allow you to enumerate directory to try to find some API folder

More information ---> [[Red Team/3 - Web Hacking/Brute Force/2 - Fuzz/Gobuster/• Commands]]

---

<h2>Dev Tools (Inspector Mode)</h2>

