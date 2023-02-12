--- ---

<h2>Testing for Information Disclosure</h2>

Fuzzing
1. Identify interesting parameters in the web application
2. Submit unexpected data types or specially crafted fuzz strings to see the response
3. Automate this process with Burp Intruder
	a. Add payload positions to parameters and use pre-built wordlists of fuzz strings
	b. Easily identify differences in responses by comparing HTTP status code, response times, etc.
	c. Use grep matching rules to identify occurrences of keywords

Burp Scanner
1. Run a Burp Scan to get the following:
	a. Live scanning features while browsing the website
	b. Schedule automated scans to crawl and target the target site on your behalf
	c. Automatically flag information disclosure vulns for you

Burpsuite Engagement Tools
1. Right click any HTTP message and select "Engagement tools"
2. Search
	a. Look for any expression within the selected item
3. Find Comments
	a. Extract any developer comments found in a selected item
4. Discover Content
	a. Identify additional content and functionality not linked in visible website