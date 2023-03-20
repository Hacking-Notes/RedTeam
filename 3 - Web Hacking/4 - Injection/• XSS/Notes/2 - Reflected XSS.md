--- ---

<h2>Reflected XSS</h2>

Reflected XSS happens when user-supplied data in an HTTP request is included in the webpage source without any validation.

- **Potential Impact:**  
  
	The attacker could send links or embed them into an iframe on another website containing a JavaScript payload to potential victims getting them to execute code on their browser, potentially revealing session or customer information.

- **How to test for Reflected XSS:**  

	You'll need to test every possible point of entry; these include:

	-   `Parameters in the URL Query String`
	-   `URL File Path`
	-   `Sometimes HTTP Headers (although unlikely exploitable in practice)`
	-   `Title name of a website post` ---> 
		- example
			![[Pasted image 20221129102249.png]] 

   
	Once you've found some data which is being reflected in the web application, you'll then need to confirm that you can successfully run your JavaScript payload; your payload will be dependent on where in the application your code is reflected

- **Example Scenario:**  
  
	A website where if you enter incorrect input, an error message is displayed. The content of the error message gets taken from the **error** parameter in the query string and is built directly into the page source.

	![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/a5b0dbc4d2f1f69988f82f2c5d53f6ed.png)  

	![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/7f90b73106d655b07874943f93533f7b.png)  

	The application doesn't check the contents of the **error** parameter, which allows the attacker to insert malicious code.

	![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/66743e9fa50b4c5793f070eb505f72d1.png)  

	![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/24e50d95cecfc3783bd1a3a4fecbf310.png)  

	The vulnerability can be used as per the scenario in the image below:


	![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/8e3bffe500771c03366de569c3565058.png)  
