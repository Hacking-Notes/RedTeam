--- ---

<h2>Classic Authentication Attacks</h2>

Basicly brute forcing accounts with burpsuite or WFUZZ to get account token (Bearer)

With BupSuite
```
Simply run reapeater mode
```

With WFUZZ
```
wfuzz -d '{"email":"email@email.com","password":"FUZZ"}' -H 'Content-Type: application/json' -z file,/PASSWORD.txt -u http://something.com/api/auth/login --hc (IGNORE STATUS (ex: 500))
```

- This might be different between application that you are testing... Best solution is burpsuite pro

---

<h2>API Token Attacks</h2>

<h4>Token Forgerie</h4>

Token predictability is one of the most easy attack vector used by hacker. It allow attacker to create a token forgerie attack

- steps
	- Start burpSuite and go on the login page where the token auth is generated (it is possible to send the request from postman and intercept it on burpsuite also)
	- Authentify and capture the token request (Manualy or via postman)
	- Send the request to sequencer in burpsuite for a live capture request
	- Create the slection and launch the attack
		- example image
			![[Pasted image 20221123191453.png]]
			![[Pasted image 20221123191529.png]]
			![[Pasted image 20221123191538.png]]

	- If the tokens are similar, you can brute force some of the tokens to find valids one


<h4>JWT Attacks</h4>
JWT tokens are base64 encoded. This then allow for us the possibility to decode them and change the value after sending it back

**JWT tokens start with = "ey**

- Steps 
	- Start burpSuite and go on the login page where the token auth is generated (it is possible to send the request from postman and intercept it on burpsuite also)
	- Authentify and capture the token request (Manualy or via postman)
	- Check the token with a tool like https://jwt.io
	- You can try to edit the token and send it back from burp... if this fail that mean that proper signature has been enabled (Signature is part of the token (last dot))

	- You can try to use a tool like jtw_tool to try and see if the jwt token has some vulnerability

	- If there is Data exposure on the token, you can try to use this information to log has an other user. 
	- Example: if the token simply paste the email adress in the request, we can try to find from the data exposure other people email and change the JWT token to output the token of the person email we just enter. From there, we would be able to send API request from some else account
