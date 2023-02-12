--- ---

<h2>Commands</h2>

```Terminal
# Passive Subdomain Enumeration using OWASP Amass  
amass enum -brute -d DOMAIN -src -w WORDLIST (opt) -config c.ini -o subdomain.txt
```

- AMASS other Usage
	- amass intel - Discover targets for enumerations
	- amass enum  - Perform enumerations and network mapping
	- amass viz   - Visualize enumeration results
	- amass track - Track differences between enumerations
	- amass db    - Manipulate the Amass graph database

	Simply type amass "MODULE" -h (More information)

https://github.com/OWASP/Amass

---

<h2>What is AMASS</h2>

The OWASP Amass Project performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques.

![[Pasted image 20221118172946.png]]