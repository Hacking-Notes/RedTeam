--- ---

<h2>Server Side</h2>

- Filtering
1. File Length Filtering (Size of the file, Minimum/Maximum)
2. File Name Filtering (Same name has other on save server + Special/Unicode characters)
3. File Content Filtering (Verify MIME and Magic Number)
4. File Type Filtering (Similar to Extnesion Validation, but more intensive)

- extension

	We can see that the code is filtering out the `.php` and `.phtml` extensions, so if we want to upload a PHP script we're going to have to find another extension. The [wikipedia page](https://en.wikipedia.org/wiki/PHP) for PHP gives us a few common extensions that we can try; however, there are actually a variety of other more rarely used extensions available that webservers may nonetheless still recognise. These include: `.php3`, `.php4`, `.php5`, `.php7`, `.phps`, `.php-s`, `.pht` and `.phar`. 

- Magic Number

	![](https://i.imgur.com/2126EHS.png)  

	As expected, the command tells us that the filetype is PHP. Keep this in mind as we proceed with the explanation.  

	We can see that the magic number we've chosen is four bytes long, so let's open up the reverse shell script and add four random characters on the first line. These characters do not matter, so for this example we'll just use four "A"s:

	![](https://i.imgur.com/oe434wu.png)

	Save the file and exit. Next we're going to reopen the file in `hexeditor` (which comes by default on Kali), or any other tool which allows you to see and edit the shell as hex. In hexeditor the file looks like this:

	![](https://i.imgur.com/otIyN96.png)

	Note the four bytes in the red box: they are all `41`, which is the hex code for a capital "A" -- exactly what we added at the top of the file previously.

	Change this to the magic number we found earlier for JPEG files: `FF D8 FF DB`

	![](https://i.imgur.com/2OlGKdQ.png)  

	Now if we save and exit the file (Ctrl + x), we can use `file` once again, and see that we have successfully spoofed the filetype of our shell:

	![](https://i.imgur.com/ldyt88v.png)  

	Perfect. Now let's try uploading the modified shell and see if it bypasses the filter!