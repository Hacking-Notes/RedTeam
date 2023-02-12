--- ---

<h2>Importing API Steps</h2>

- Find a API (Via Inspector Mode (JSON Data))
- Copy the request via cURL command
- Create a new collection
- Import the request in Postman (Import button)

---

<h2>Capture Request</h2>

![[Screenshot from 2022-11-22 19-44-12.png]]

![[Pasted image 20221122211202.png]]

Steps
- Select Website
- Select Port
- Use the port in the browser and visit the targeted website
- Make different request everywhere on the website (ex: visiting each pages, managing you account, changing your email & password, ...)
- After collecting the data needed, select all the URL containing API and add them to the collection
- You can then include each categories into a new folder to better organise your request

---

<h2>SWAGGER FILE ---> MITMproxy (MITMweb)</h2>

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
- Change the title if needed and save the file
- run the mitmproxy2swagger again
```
sudo mitmproxy2swagger -i ~/Download/FILE-SAVED -o output-file.yml -p WEBSITE -f flow --examples
```
- Load the swagger file on https://editor.swagger.io (From there, you should start to see if you have access to more information that the API is inteded to give you)... You can also creat cURL links try the API
- Finaly, import the .YML in post man

---

<h2>Authentification (TO Review)</h2>

Bearer token --->

---
<h2>Collections / Environnements / Cathegories and Variables (To Review)</h2>

Find and replace

Variables

collections

Environnemnts

cathegories


---

<h2>Exploitation</h2>

- [[API Authentication Attacks]]
- [[Exploiting API Authorization]]
- [[Improper Assets Management]]

- Proxy to BurpSuite