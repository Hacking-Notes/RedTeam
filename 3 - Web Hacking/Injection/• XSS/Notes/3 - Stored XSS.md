--- ---

<h2>Stored XSS</h2>

As the name infers, the XSS payload is stored on the web application (in a database, for example) and then gets run when other users visit the site or web page.  
  
- **Potential Impact:**  
  
	The malicious JavaScript could redirect users to another site, steal the user's session cookie, or perform other website actions while acting as the visiting user.

	**How to test for Stored XSS:**  

	You'll need to test every possible point of entry where it seems data is stored and then shown back in areas that other users have access to; a small example of these could be:  

	-   Comments on a blog
	-   User profile information  
	-   Website Listings  
	-   Button (Bypass filter that dont allow code) `<button onclick=alert(‘xss’)>click</button>`
    
	Sometimes developers think limiting input values on the client-side is good enough protection, so changing values to something the web application wouldn't be expecting is a good source of discovering stored XSS, for example, an age field that is expecting an integer from a dropdown menu, but instead, you manually send the request rather than using the form allowing you to try malicious payloads. 

	Once you've found some data which is being stored in the web application,  you'll then need to confirm that you can successfully run your JavaScript payload; your payload will be dependent on where in the application your code is reflected

- **Example Scenario:**  
  
	A blog website that allows users to post comments. Unfortunately, these comments aren't checked for whether they contain JavaScript or filter out any malicious code. If we now post a comment containing JavaScript, this will be stored in the database, and every other user now visiting the article will have the JavaScript run in their browser.

	![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/cc2566d297f7328d91bc8552f902210e.png)  








