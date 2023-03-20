--- ---
<h3>What is Wfuzz</h3>
WFUZZ is an open-source web application security testing tool used for brute-forcing and fuzzing HTTP/HTTPS web applications. The tool is designed to identify vulnerabilities in web applications by discovering hidden or undiscovered content such as files, directories, and parameters.

WFUZZ supports various HTTP methods such as GET, POST, PUT, DELETE, and many more. It can also be used for SSL and proxy connections. The tool can perform complex attacks by combining multiple parameters and testing different combinations.

---
<h3>Common uses and commands</h3>
Wfuzz can be used for various purposes such as directory and file discovery, parameter brute-forcing, and vulnerability discovery. Some of the common commands that can be used with Wfuzz  include:

Website Login
```
wfuzz -zfile,wordlists/passwords.txt --hs 'Invalid-HTML-STATMENT' -d 'username=access&password=FUZZ' https://DOMAIN/login
```

---
<h3>More Information</h3>
Wfuzz  can be downloaded from its GitHub page at [https://github.com/xmendez/wfuzz](https://github.com/xmendez/wfuzz). The tool is compatible with Windows, Linux, and macOS. WFUZZ has extensive documentation available on its GitHub page, including examples, tutorials, and user guides.

<iframe src="https://github.com/xmendez/wfuzz" width="100%" height="1300"></iframe>