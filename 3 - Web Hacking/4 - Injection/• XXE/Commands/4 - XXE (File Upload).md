--- ---

<h2>XXE Attacks via File Upload</h2>

- If a server allows the upload of DOCX or SVG, XXE can be embedded in these documents
- When the document is processed by the application, it will trigger the exploit XXE Attack via Modified Content Type

- Normal Request example:
```xml
POST /action HTTP/1.0
Content-Type: application/x-www-form-
urlencoded
Content-Length: 7
foo=bar
```

- If the server tolerates this, you can exploit it
```xml
POST /action HTTP/1.0
Content-Type: text/xml
Content-Length: 52
<?xml version="1.0" encoding="UTF-
8"?><foo>bar</foo>
```