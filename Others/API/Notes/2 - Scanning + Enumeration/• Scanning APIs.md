--- ---

<h2>Finding Security Misconfigurations</h2>

ZapProxy (OWASP)
- There is two way of scanning API from ZapProxy

Automated Scanning (Via YML file)
```
- Launch an automated scan and way until completing
- Select the import button and chose your YML file (This should launch a new scan)
- Relaunch a scan to expand the research
```

![[Pasted image 20221123144033.png]]


Manual Scanning (Best Option)
```
- Launch a manual scan (options)
- Once the browser open, select continue to the target
- Now, you can turn attack mode on and create an account
- Once you have an account (Valid token), you can start using spider/active scan options while your visiting each page and testing each options (like in the active reconnaissance step)
- Once done, you should have many request and website on ZAP. You can now select the website and "include in context" to only target this website (in view mode)
```

- Using a manual scan will help you find more vulnerability directly from the ZAP platform

![[Pasted image 20221123144101.png]]