--- ---
<h3>What is FFUF</h3>
FFUF is an open-source web fuzzing tool that stands for "Fuzz Faster U Fool". It is designed to help web developers and security professionals discover hidden or undiscovered files, directories, and subdomains by brute-forcing or fuzzing URLs.

FFUF supports various HTTP methods such as GET, POST, PUT, DELETE, HEAD, and many more. It also allows the use of custom headers and cookies. The tool can perform content discovery and web content monitoring.

---
<h3>Common uses and commands</h3>
FFUF can be used for various purposes such as directory and file discovery, virtual host discovery, parameter brute-forcing, and many more. Some of the common commands that can be used with FFUF include:

Website Enumeration
```Terminal 
ffuf -u WEBISTE/FUZZ -w WORDLIST -fs NUMBER -fc STATUS -t NUMBER_TREATH
```
- -u       ---> Website (Include the FUZZ word were you want to Fuzz) 
- -w      ---> Wordlist to be select
-  -fs      ---> Default response number (bytes) to ignore
- -fc      ---> Response status to ignore (example 404,402, ...)

---
<h3>More Information</h3>
FFUF can be downloaded from its GitHub page at [https://github.com/ffuf/ffuf](https://github.com/ffuf/ffuf). The tool is compatible with Windows, Linux, and macOS. FFUF has extensive documentation available on its GitHub page, including examples, tutorials, and user guides.

<iframe src="https://github.com/ffuf/ffuf" width="100%" height="1300"></iframe>