--- ---
<h3>What is Hydra</h3>
Hydra is a parallelized, fast and flexible login cracker. If you don't have Hydra installed or need a Linux machine to use it, you can deploy a powerful [Kali Linux machine](https://tryhackme.com/room/kali) and control it in your browser!

Brute-forcing can be trying every combination of a password. Dictionary-attack's are also a type of brute-forcing, where we iterating through a wordlist to obtain the password.

---
<h3>Common uses and commands</h3>
Hydra can be used for various purposes such as password brute-forcing, account takeover, and network authentication testing. Some of the common commands that can be used with Hydra include:

Website
```Terminal 
hydra -l USERNAME -P PASSWORD.txt IP http-POST|GET-form "/PATH-URL/something.php:username=^USER^&password=^PASS^:INVALID-STATEMENT-HTML" -VV -T X


hydra -l phillips -P /home/ubuntu/Downloads/list.txt 10.10.206.120 http-get-form "/login-get  
/index.php:username=^USER^&password=^PASS^:S=logout.php" -f
```

- http-post-form = Request                                                             --->  <font color="Red">CHANGE POST OR GET</font>
- PATH = URL Path (From Website or BurpSuite)
- ^USER^ = Keyword to define the FUZZ of username
- ^PASS^ = Keyword to define the FUZZ of password.txt
- -t = Speed
- -VV = Verbose Enable
- Login trigger
	- S=             ---> Element on the other page (After login)
	- HTML       ---> HTML login fail element
- Tips
	- If there is no ?something=  ---> Simply add : after the URL (/account-login.php:BURP-STUFF-HERE)  
- Example
	- ![[Pasted image 20221010211610.png]]
	- ![[Pasted image 20221010211700.png]]

SSH
```Terminal 
hydra -l USERNAME -P WORDLIST.txt MACHINE_IP -t X ssh
hydra -L USERNAME.txt -P PASSWORD MACHINE_IP -t X ssh
```
- ssh = Service

FTP
```Terminal 
hydra -l user -P passlist.txt ftp://MACHINE_IP
```
- ftp:// = FTP server

SMTP
```
hydra -l email@company.xyz -P /path/to/wordlist.txt smtp://10.10.x.x -v
```

---
<h3>More Information</h3>
Hydra can be downloaded from its GitHub page at [https://github.com/vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra). The tool is compatible with Windows, Linux, and macOS. Hydra has extensive documentation available on its GitHub page, including examples, tutorials, and user guides.

<iframe src="https://www.kali.org/tools/hydra/" width="100%" height="1300"></iframe>