--- ---

<h2>Retrieving Data from Other Database Tables</h2>

In cases where the results of an SQL query are returned within the application's responses, an
attacker can leverage an SQL injection vulnerability to retrieve data from other tables within the
database. This is done using the UNION keyword, which lets you execute an additional SELECT
query and append the results to the original query.

User Query
```
SELECT name, description FROM products WHERE category = 'Gifts'
```

Attacker Query
```
' UNION SELECT username, password FROM users--
```

Cause the application to return all usernames & passwords