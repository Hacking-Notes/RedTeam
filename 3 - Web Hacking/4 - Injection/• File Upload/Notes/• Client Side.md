--- ---

<h2>Client Side</h2>

- Tips
1.  Turn off Javascript in your browser
2.  Intercept and modify the file upload (BurpSuite)
3.  Send the file directly to the upload point
```Terminal
curl -X POST -F "submit:<value>" -F "<file-parameter>:@<path-to-file>" <site>
```

- Filtering
1. File Length Filtering (Size of the file, Minimum/Maximum)
2. File Name Filtering (Same name has other on save server + Special/Unicode characters)
3. File Content Filtering (Verify MIME and Magic Number)
4. File Type Filtering (Similar to Extnesion Validation, but more intensive)


- MIME Example ---> MIME Extension https://quickref.me/mime (PHP = text/x-php)

	<h4>MIME (HERE WHAT TO CHANGE)</h4>
	
	![](https://i.imgur.com/uptWRKW.png)   

	<h4>Here What do do</h4>
	As always, we'll take a look at the source code. Here we see a basic Javascript function checking for the MIME type of uploaded files:

	![](https://i.imgur.com/TrI5jQD.png)
	
	In this instance we can see that the filter is using a _whitelist_ to exclude any MIME type that isn't `image/jpeg`.  

	Our next step is to attempt a file upload -- as expected, if we choose a JPEG, the function accepts it. Anything else and the upload is rejected.

	Having established this, let's start [Burpsuite](https://blog.tryhackme.com/setting-up-burp/) and reload the page. We will see our own request to the site, but what we really want to see is the server's _response_, so right click on the intercepted data, scroll down to "Do Intercept", then select "Response to this request":

	![](https://i.imgur.com/T0RjAry.png)

	When we click the "Forward" button at the top of the window, we will then see the server's response to our request. Here we can delete, comment out, or otherwise break the Javascript function before it has a chance to load:  

	![](https://i.imgur.com/ACgWLpH.png)

	Having deleted the function, we once again click "Forward" until the site has finished loading, and are now free to upload any kind of file to the website:

	![](https://i.imgur.com/5cyqjqa.png)

	It's worth noting here that Burpsuite will not, by default, intercept any external Javascript files that the web page is loading. If you need to edit a script which is not inside the main page being loaded, you'll need to go to the "Options" tab at the top of the Burpsuite window, then under the "Intercept Client Requests" section, edit the condition of the first line to remove `^js$|`:

	![](https://i.imgur.com/95hi6pX.png)  

	We've already bypassed this filter by intercepting and removing it prior to the page being loaded, but let's try doing it by uploading a file with a legitimate extension and MIME type, then intercepting and correcting the upload with Burpsuite.

	Having reloaded the webpage to put the filter back in place, let's take the reverse shell that we used before and rename it to be called "shell.jpg". As the MIME type (based on the file extension) automatically checks out, the Client-Side filter lets our payload through without complaining:

	![](https://i.imgur.com/WNpruFM.png)

	Once again we'll activate our Burpsuite intercept, then click "Upload" and catch the request:

	![](https://i.imgur.com/h2164Li.png)

	Observe that the MIME type of our PHP shell is currently `image/jpeg`. We'll change this to `text/x-php`, and the file extension from `.jpg` to `.php`, then forward the request to the server:

	![](https://i.imgur.com/sqmwssT.png)
