--- ---

<h2>Blind XXE Vulnerabilities</h2>

This means that the application does not return the values of any defined external entities in its responses, and so direct retrieval of server-side files is not possible.

XInclude Attacks
- Server steps
	- Application receives client-submitted data
	- Data is embedded on the server-side into an XML document
	- Document is then parsed

- XInclude
	- Part of the XML specification that allows an XML document to be built from sub-documents
	- Need to reference the XInclude namespace and provide the path to the file that you wish to include

```xml
<foo 
xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text"
href="file:///etc/passwd"/></foo>
```


More info about XML Injection ---> [HERE]([[3 - XML]])