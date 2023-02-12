--- ---

<h2>Top Injections</h2>

Website
```Terminal
https://website.com/account.php?id=1
```

- Replace or FUZZ element after equal sign


Intercept and change the value of a parameters  (BurpSuite)
```Terminal
< input type="hidden" id="1008" name="cost" value="70.00" >
```

- example, an attacker can modify the "value" information  of a specific item, resulting in lowering it's cost.

---

<h2>IDOR</h2>  

IDOR stands for Insecure Direct Object Reference and is a type of access control vulnerability.  

This type of vulnerability can occur when a web server receives user-supplied input to retrieve objects (files, data, documents), too much trust has been placed on the input data, and it is not validated on the server-side to confirm the requested object belongs to the user requesting it.

- Example

	Imagine you've just signed up for an online service, and you want to change your profile information. The link you click on goes to http://online-service.thm/profile?user_id=1305, and you can see your information.  
  
	Curiosity gets the better of you, and you try changing the user_id value to 1000 instead (http://online-service.thm/profile?user_id=1000), and to your surprise, you can now see another user's information. You've now discovered an IDOR vulnerability! Ideally, there should be a check on the website to confirm that the user information belongs to the user logged requesting it. 

---

<h2>Hiden Page / Bypass</h2>

Always try after parameters index.php (if in php)
```
hacker101.com/my-diary/?template=index.php ---> show index page and possible filtering
```

---
<h2>Parameter Tampering</h2>

The Web Parameter Tampering attack is based on the manipulation of parameters exchanged between client and server in order to modify application data, such as user credentials and permissions, price and quantity of products, etc. Usually, this information is stored in cookies, hidden form fields, or URL Query Strings, and is used to increase application functionality and control.

This attack can be performed by a malicious user who wants to exploit the application for their own benefit, or an attacker who wishes to attack a third-person using a [Man-in-the-middle attack](https://owasp.org/www-community/attacks/Man-in-the-middle_attack "wikilink"). In both cases, tools likes Webscarab and Paros proxy are mostly used.

The attack success depends on integrity and logic validation mechanism errors, and its exploitation can result in other consequences including [XSS](https://owasp.org/www-community/attacks/Cross-site_Scripting_/(XSS/) "wikilink"), [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection), file inclusion, and path disclosure attacks.

- Steps
```Terminal
- Open Burpsuite & open website (target)

- Intercept the request (Proxy) while clicking on an item

- In the proxy tab, search for the parameter that you might be interested to change. (Ex: if an object cost 10.00, I will search the value 10.00 in the intercepted request)

- If the value targeted is not vulnerable, try changing other variable like the quantity, ...

- Follow the sale process (chose item dimention, add to cart, checkout...) to find the output value requested to the payment method

- Once you request to purchase the item, the website will send a request to the payment method and might contain the parameters that your looking to change

- Change the values and foward the request
```

Ressources
- https://www.youtube.com/watch?v=XeeZQEYbM0I
- https://www.youtube.com/watch?v=2hG5FjRsbbc