--- ---
<h3>What is cURL?</h3>

cURL is a command-line tool and library for transferring data with URLs. It supports various protocols, including HTTP, HTTPS, FTP, and many others. cURL is widely used for interacting with web services, fetching web pages, and transferring files via different protocols.

---
<h3>Common Use and Commands:</h3>

cURL's versatility makes it a valuable tool for developers, sysadmins, and security professionals. Here's how to use cURL, including the `-i` option to retrieve only the headers:

```Terminal
curl [OPTIONS] [URL]
```

Common options include:
- `-i`: Include the HTTP headers in the output.
- `-H`: Specify custom headers.
- `-X`: Specify the request method (e.g., GET, POST).
- `-L`: Follow redirects.
- `-o`: Write output to a file.

Example to retrieve only headers:
```Terminal
curl -i example.com
```

Output may include:
- HTTP headers such as status code, content type, and server information.

---
<h3>More Information:</h3>

For further details on cURL and its advanced usage, users can consult the official documentation or visit the cURL website. Additionally, the source code for cURL is available on GitHub: [https://github.com/curl/curl](https://github.com/curl/curl).