--- ---

<h2>UNION Attacks</h2>

When an application is vulnerable to SQL injection and the results of the query are returned within the application's responses, the UNION keyword can be used to retrieve data from other tables within the database. This results in an SQL injection UNION attack.

Example Code:
```
SELECT a, b FROM table1 UNION SELECT c, d FROM table2
```

- Returns a single result with two columns, containing values from columns a and b in table1 and c and d in table2

Requirements for UNION query to work:
- Individual queries must return the same number of columns
- Data types in each column must be compatible between the individual queries

<h4>Determine the number of columns required in an SQL Injection UNION attack</h4>

Method #1 -- Inject a series of ORDER BY clauses and increment the specified column index until an error occurs
![[Pasted image 20221210163720.png]]
- Will eventually get an error code such as this one:
```
The ORDER BY position number 3 is out of range of the number of items in the select list.
```
- Error code might be returned in its HTTP response

Method #2 -- Submit a series of UNION SELECT payloads specifying a different number of null values
![[Pasted image 20221210163851.png]]
- If the number of "nulls" does not match the number of columns, you will get an error such as:
```
All queries combined using a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists.
```
- Might also be just a generic error or a different response


<h3>Finding Columns with a useful data type in an SQL Injection UNION attack</h3>

The reason for performing an SQL injection UNION attack is to be able to retrieve the results from an injected query.
Generally, the interesting data that you want to retrieve will be in string form, so you need to find one or more columns in the original query results whose data type is, or is compatible with, string data.

1. Probe each column to test whether it can hold string data -- example if the query returns four columns:
```
' UNION SELECT
'a',NULL,NULL,NULL--
' UNION SELECT
NULL,'a',NULL,NULL--
' UNION SELECT
NULL,NULL,'a',NULL--
' UNION SELECT
NULL,NULL,NULL,'a'--
```
- If it's not compatible, it will throw an error


<h3>Using an SQL Injection UNION Attack to Retrieve Interesting Data</h3>

When you have determined the number of columns returned by the original query and found which columns can hold string data, you are in a position to retrieve interesting data.

Scenario:
- Original query returns 2 columns, both hold string data
- Injection point is a quoted string within the WHERE clause
- The database contains a table called users with the columns username and password
- Get the contents of users with this input
```
' UNION SELECT username, password FROM users--
```

---

<h2>Retrieving Multiple Values within a Single Column</h2>

You can easily retrieve multiple values together within this single column by concatenating the values together, ideally including a suitable separator to let you distinguish the combined values. 

For example, on Oracle you could submit theinput:
```
' UNION SELECT username || '~' || password FROM users--
```
- The double-pipe sequence is a string concatenation operator in Oracle
- Allows you to read all usernames and passwords