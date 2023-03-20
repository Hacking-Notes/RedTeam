--- ---

<h2>What is Cross-site request forgery</h2>

Cross-site request forgery (CSRF) is a type of malicious exploit where unauthorized commands are submitted to a website or web application from a user that the web application trusts. This is done by tricking an innocent end user into submitting a web request they did not intend, which can cause actions to be performed on the website such as data leakage, changes to session state, or manipulation of the end user's account. Unlike cross-site scripting (XSS), which exploits a user's trust in a particular site, CSRF exploits the trust a site has in a user's browser.

In a CSRF attack, the attacker can use a victim's own session cookie to perform unauthorized actions on a website they are already logged into. This is done by tricking the victim into visiting a malicious website or clicking a link that contains a specially crafted HTML form.
ㅤ
The form is designed to automatically submit a request to the vulnerable website, using the victim's own session cookie to authenticate the request. The request can perform any action that the victim is authorized to perform on the website, such as making a purchase, changing personal information...


==No CSRF token (Application Account) ---> Vulnerable==


CSRF need some condition to be Vulnerable
	- A Relevant Action (Ex: Change email)
	- Cookie based session
	- No unpredictable request parameters


CSRF token
	CSRF tokens are typically generated when a user first visits a website or web application, and are then included with each subsequent request made by the user's browser. The tokens are unique to the user's session, and cannot be accessed or used by an attacker from another website. When the web application receives a request, it checks the token included in the request against the token it expects from the user's session. If the tokens match, the request is considered legitimate and is processed as normal. If the tokens do not match, the request is considered to be a CSRF attack and is rejected.


- Example of CSRF: 
	A user is logged into a web application, such as an online banking platform. An attacker creates a malicious website that contains a form with hidden fields that mimic a legitimate transaction, such as transferring money from the user's account to the attacker's account. When the user visits the malicious website, the form is automatically submitted, triggering the transaction without the user's knowledge or consent. The user's browser is tricked into sending a request to the online banking platform that appears legitimate, but actually performs an unauthorized action.