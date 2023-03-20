--- ---

<h2>Top Injections</h2>

Type of vulnerability
- Parameters Injection (directly after the parameter)
- Payload Injection (directly after the URL)
- Combination (Add payload after Parameters)

Type of parameter (List)
```Terminal
dest=      uri=     continue=  window=     redirect=     path=   url=       to= 
out=       view=    dir=       show=       navigation=   open=   file=     val= 
validate=  domain=  callback=  return=     page=         feed=   host= 
port=      next=    data=      reference=  site=         html=   returnurl=  ...
```

Parameters Vulnerability
```Terminal
https://website.com/vulnerable?url=POSSIBLY-VULNERABLE.com/EVIL-PATH
```

Encode URL
Double Encode URL
Use special characters (%E3%80%82%23 or 。# (Decoded))
	https://example.com/x.php?url=EVIL-URL。#WEBSITE-URL

Brute Force List and more special characters
	- https://github.com/ManShum812/VulnerabilityPayload/blob/main/openredirect.txt
	- Search for 301 when brute forcing  ---> Suggest to check them 1 by 1 (Some 200 response has worked before)
