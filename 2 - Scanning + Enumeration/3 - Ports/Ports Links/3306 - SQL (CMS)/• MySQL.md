--- ---
<h2>What is MySQL</h2>
In its simplest definition, MySQL is a relational database management system (RDBMS) based on Structured Query Language (SQL). Too many acronyms? Let's break it down:

- **Database:**

	A database is simply a persistent, organised collection of structured data

- **RDBMS:**

	A software or service used to create and manage databases based on a relational model. The word "relational" just means that the data stored in the dataset is organised as tables. Every table relates in some way to each other's "primary key" or other "key" factors.  

- **SQL:**

	MYSQL is just a brand name for one of the most popular RDBMS software implementations. As we know, it uses a client-server model. But how do the client and server communicate? They use a language, specifically the Structured Query Language (SQL).  

	Many other products, such as PostgreSQL and Microsoft SQL server, have the word SQL in them. This similarly signifies that this is a product utilising the Structured Query Language syntax.  

- **How does MySQL work?

	MySQL, as an RDBMS, is made up of the server and utility programs that help in the administration of MySQL databases.

	The server handles all database instructions like creating, editing, and accessing data. It takes and manages these requests and communicates using the MySQL protocol. This whole process can be broken down into these stages:  

	1.  MySQL creates a database for storing and manipulating data, defining the relationship of each table.
	2.  Clients make requests by making specific statements in SQL.
	3.  The server will respond to the client with whatever information has been requested.  

- **What runs MySQL?**

	MySQL can run on various platforms, whether it's Linux or windows. It is commonly used as a back end database for many prominent websites and forms an essential component of the LAMP stack, which includes: Linux, Apache, MySQL, and PHP.

- **More Information:**

	Here are some resources that explain the technical implementation, and working of, MySQL in more detail than I have covered here:

	[https://dev.mysql.com/doc/dev/mysql-server/latest/PAGE_SQL_EXECUTION.html](https://dev.mysql.com/doc/dev/mysql-server/latest/PAGE_SQL_EXECUTION.html) 
	[https://www.w3schools.com/php/php_mysql_intro.asp](https://www.w3schools.com/php/php_mysql_intro.asp)

---
<h3>Find MySQL Port</h3>
- Nmap
```Terminal
nmap -sV -sC IP -p3306
```

- Possible to find MySQL on an other port

---
<h3>Attack</h3>
```
- 4 Possible ways to get in MYSQL databse
```Terminal
1. MySQL server credentials                     ---> Brute Froce
2. The version of MySQL running                 ---> Via Nmap Scan
3. The number of Databases, and their names.    ---> Nmap & MSFconsole

4. Post exploitation    ---> Finding Creds in machine (Ex: Server running Wordpress)
```

- Brute Force
```Terminal
hydra -t X –l USERNAME –P WORDLIST IP -vV mysql
```

- hydra      --->  Runs the hydra tool  
- -t X         --->  Number of parallel connections per target  
- -l             ---> Points to the user who's account you're trying to compromise  
- -P            ---> Points to the file containing the list of possible passwords  
- -vV          ---> Sets verbose mode to very verbose, shows login + password 
- IP             ---> The IP address of the target machine  
- mysql       --->  Sets the protocol

- Metasploit
```
- msfconsole ---> mysql_schemadump
- msfconsole ---> mysql_hashdump
```

---
<h3>Connection</h3>
- Manual connection
```Terminal
mysql -u USER -p PASSWORD -h IP
```
