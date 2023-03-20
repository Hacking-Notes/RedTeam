--- ---

<h2>Overview</h2>

![[Screenshot from 2022-12-02 12-37-32.png]]

- Allows an attacker to execute commands on the web server
- Used to compromise other parts of the hosting infrastructure via pivoting

Example Exploit:
- Website that allows users to view whether and item is in stock:
https://insecure-website.com/stockStatus?productID=381&storeID=29
	- Application calls out a shell command with product & store IDs as arguments
		```
		stockreport.pl
		381 29
		```

- Submit the following in the "productID" parameter
```
stockreport.pl & echo
aiwefwlguh & 29
```

- Useful Commands:
![[Screenshot from 2022-12-02 12-37-18.png]]