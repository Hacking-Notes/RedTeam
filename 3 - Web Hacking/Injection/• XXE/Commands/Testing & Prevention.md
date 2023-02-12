--- ---

<h2>Testing & Prevention</h2>

**How to Find and Test for XXE vulnerabilities**
- Use BurpSuite's Web Vulnerability Scanner
- Manually testing involves the following:
	- Testing for file retrieval by defining an external entity based on a well-known OS file
	- Testing for blind XXE by defining an external entity based on a URL to a system you control
		§ Burp Collaborator Client can be used for this
	- Testing for vulnerab inclusion of user-supplied non-XML data within a server-side XML document by using an XInclude attack

**How to Prevent XXE Vulnerabilities**
- Disable features that allow an application's XML parsing library to support potentially dangerous XML features that the application does not need
- Disable resolution of external entities
- Disable support for XInclude
	- Done via configuration options or programmatically overriding default behavor