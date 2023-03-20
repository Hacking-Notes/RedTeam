--- ---

<h2>Blind SSRF</h2>

- Cannot see the back-end request
- Harder to exploit but can lead to full RCE

Finding the Hidden Attack Surface
- Partial URLs in Requests
- URLs within data formats
	- Example is the XML data format
	- If an application parses XML data it might be vulnerable to an XXE injection
- SSRF via the Referer Header
	- Can exploit server-side analytic software that tracks visitors
	- Analytic software will often visit any 3rd party URL that appears in the Referer header
	- Can exploit the application by editing the referer header for a malicious site or code