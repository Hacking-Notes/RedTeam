--- ---

<h2>Top Injection</h2>

Detect the vulnerability

Basic entity test, when the XML parser parses the external entities the result should contain "John" in `firstName` and "Doe" in `lastName`. Entities are defined inside the `DOCTYPE` element.

```Terminal
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY example "Doe"> ]>
 <userInfo>
  <firstName>John</firstName>
  <lastName>&example;</lastName>
 </userInfo>
```

Types of XXE Attacks:
- Exploiting XXE to retrieves files                                                       ---> [Commands]([[1 - XXE Retrieve Files]])
- Exploiting XXE to perform SSRF attacks                                         ---> [Comamnds]([[2 - XXE SSRF attacks]])
- Exploiting blind XXE to exfiltrate data out-of-band                       ---> [SQL]([[1 - Database]]) & [XML]([[3 - XXE (Blind)]])
- Exploiting blind XXE to retrieve data via error messages              ---> [SQL]([[1 - Database]]) & [XML]([[3 - XXE (Blind)]])
