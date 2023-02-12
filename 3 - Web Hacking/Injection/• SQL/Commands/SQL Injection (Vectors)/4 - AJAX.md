--- ---

<h2>AJAX SQL Injection</h2>

How do check if AJAx request are vulnerables

```Terminal
- Go in Inspector mode and intercept the request (network)
- Copy the request has has Curl and convert it into python
- Add the python code in a code editor (edit the cookies and value STRING --> Value)
- Add a IF statment ---> if response.status_code = 500
                                               print(response.text)
- Run the request and try to find some 500 erros (normaly mean a sql error)
```

Usefull video        ---> https://www.youtube.com/watch?v=IVHX9jDrI0o
Usefull tool           ---> https://curlconverter.com/

Cheat Sheet          ---> https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/