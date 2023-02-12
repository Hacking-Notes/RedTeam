--- ---

<h2>Reverse Engenire API</h2>

<h4>Capture Request</h4>

- pictures
	![[Screenshot from 2022-11-22 19-44-12.png]]

	![[Pasted image 20221122211214.png]]

Steps
- Select Website
- Select Port
- Use the port in the browser and visit the targeted website
- Make different request everywhere on the website (ex: visiting each pages, managing you account, changing your email & password, ...)
- After collecting the data needed, select all the URL containing API and add them to the collection
- You can then include each categories into a new folder to better organise your request

<h4>SWAGGER FILE ---> MITMproxy (MITMweb)</h4>

Pre-steps
- Launch mitmweb & intercept traffic

Steps
- Use the port in the browser and visit the targeted website
- Make different request everywhere on the website (ex: visiting each pages, managing you account, changing your email & password, ...)
- After collecting the data needed, get back to mitmweb and save the data

Converting File to Swagger
```
sudo mitmproxy2swagger -i ~/Download/FILE-SAVED -o output-file.yml -p WEBSITE -f flow --examples
```
- nano the output file and customize the ignore element (some element might have been mistly ignored ) ---> remove ignore: between anything that could be API related!
	- pictures
		![[Pasted image 20221122211408.png]]
	 ![[Pasted image 20221122211333.png]]
- Change the title if needed and save the file
- run the mitmproxy2swagger again
```
sudo mitmproxy2swagger -i ~/Download/FILE-SAVED -o output-file.yml -p WEBSITE -f flow --examples
```
- Load the swagger file on https://editor.swagger.io (From there, you should start to see if you have access to more information that the API is inteded to give you)... You can also creat cURL links try the API
- Finaly, import the .YML in post man

---

<h2>Using APIs and Excessive Data Exposure</h2>

- API Documentation Convention
	![[Pasted image 20221122212155.png]]

Using the Swagger Editor allows us to have a visual representation of our target's API endpoints. By browsing through and expanding the requests you can see the endpoint, parameters, request body, and example responses.

![[Pasted image 20221122212338.png]]

<h4>Request Permission</h4>

- In postman,  Navigate to the POST login request in your collection and update the values for "email" and "password" to match up with the account you created. If you don't remember, then you will need to go back and register for an account.
	- example image
		- ![[Pasted image 20221122212945.png]]

- Once you have successfully authenticated you should receive a response containing a Bearer token like the one seen above. 
	- example image
		- ![](https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/site/2147573912/products/PPWP8Yq8SqqPdjBEmK4h_UsingAPI13.PNG)
Copy the token found within the quotes and paste that value into the collection editor's authorization tab. Make sure to **SAVE** the update to the collection. Now you should now be able to use the API as an authorized user and make successful requests using Postman.

optional
- Set variables ---> exemple :id {{id}} in each request and in the general file variable



<h4>Excessive Data Exposure</h4>

Excessive Data Exposure occurs when an API provider sends back a full data object, typically depending on the client to filter out the information that they need. From an attacker's perspective, the security issue here isn't that too much information is sent, instead, it is more about the sensitivity of the sent data. This vulnerability can be discovered as soon as you are able to start making requests. API requests of interest include user accounts, forum posts, social media posts, and information about groups (like company profiles).

Ingredients for excessive data exposure:

-   A response that includes more information than what was requested
-   Sensitive Information that can be leveraged in more complex attacks

If an API provider responds with an entire data object, then the first thing that could tip you off to excessive data exposure is simply the size of the response. 

```
**Request**

GET /api/v1/user?=CloudStrife

**Response**

200 OK HTTP 1.1

--snip--

{"id": "5501",

"fname": "Cloud",

"lname": "Strife",

"privilege": "user",

"representative": [

     "name": "Don Coreneo",

     "id": "2203",

     "email": "dcorn@gmail.com",

     "privilege": "admin",

     "MFA": false   
     ]

}
```