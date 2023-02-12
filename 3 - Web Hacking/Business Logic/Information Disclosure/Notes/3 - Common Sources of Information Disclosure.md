--- ---

<h2>Common Sources of Information Disclosure</h2>

Common Sources of Information Disclosure

- File for Web Crawlers
	/robots.txt
	/sitemap.xml

- Directory Listings

- Developer Comments

- Error Messages
	Pay attention to any verbose error messages
		§ Template Engine
		§ Database Type
		§ Server being used
		§ Versions
	- Use this to search for documented exploits
	- If open-source, you can study the actual code being used

- Debugging Data
	- Look for the following:
		§ Values for key session variables
		§ Hostnames of creds for back-end components
		§ File and directory names on the server
		§ Keys used to encrypt data

- User Account Pages

- Source Code Disclosure via Backup Files
	- Often include API keys or creds for back-end components

- Version Control History
	- Exposed /.git directories
	- Load on personal machine and browse through it