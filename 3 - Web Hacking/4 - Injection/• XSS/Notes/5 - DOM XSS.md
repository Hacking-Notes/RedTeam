--- ---

<h2>What is the DOM?</h2>

DOM stands for **D**ocument **O**bject **M**odel and is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style and content. A web page is a document, and this document can be either displayed in the browser window or as the HTML source. A diagram of the HTML DOM is displayed below:

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/24a54ac532b5820bf0ffdddf00ab2247.png)  

If you want to learn more about the DOM and gain a deeper understanding [w3.org](https://www.w3.org/TR/REC-DOM-Level-1/introduction.html) have a great resource.

- Exploiting the DOM

	DOM Based XSS is where the JavaScript execution happens directly in the browser without any new pages being loaded or data submitted to backend code. Execution occurs when the website JavaScript code acts on input or user interaction.  
  
- Example Scenario
  
	The website's JavaScript gets the contents from the `window.location.hash` parameter and then writes that onto the page in the currently being viewed section. The contents of the hash aren't checked for malicious code, allowing an attacker to inject JavaScript of their choosing onto the webpage.  
  
- Potential Impact
  
	Crafted links could be sent to potential victims, redirecting them to another website or steal content from the page or the user's session.

	How to test for Dom Based XSS:

	DOM Based XSS can be challenging to test for and requires a certain amount of knowledge of JavaScript to read the source code. You'd need to look for parts of the code that access certain variables that an attacker can have control over, such as "**window.location.x**" parameters.

	When you've found those bits of code, you'd then need to see how they are handled and whether the values are ever written to the web page's DOM or passed to unsafe JavaScript methods such as **eval()**. 

```Terminal
<img src=x onerror=confirm(ELEMENT)>

#Location sink 
document.domain 

#More examples of location sinks 
document.location 
window.location.replace() 
window.location.assign() 


#Execution Sink 
eval() 
setTimeout() 
setInterval()
Function()


#Common Sources
document.URL 
document.documentURI 
document.URLUnencoded 
document.baseURI location 
document.cookie 
document.referrer 
window.name 
history.pushState 
history.replaceState 
localStorage 
sessionStorage 
```