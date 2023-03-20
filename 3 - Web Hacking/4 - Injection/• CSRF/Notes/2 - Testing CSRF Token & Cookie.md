--- ---

Testing CSRF tokens and Cookie with Burp Suite:

- ==Change CSRF token and key from another user==, observe if the application's security can be bypassed by using a CSRF token and key (cookie) from another user. This can be done by intercepting a request that includes a CSRF token and key, extracting the token and key from the request and using them in another user request, and forwarding the modified request to the server to see if it is still accepted. If the request is accepted using a token and key of another user, it may indicate that the tokens and keys are not properly linked to the user session and the application may be vulnerable to CSRF attacks. (URL need to be able to include/append HTTP header)

- ==Change CSRF token and key where token is duplicated in cookie==, utilizing cookies and tokens obtained from another account to perform unauthorized actions on the targeted website. This can be done by providing a set of cookies and tokens to the website, which will allow the attacker to act as the legitimate user. The actions that can be performed are diverse, it can include unauthorized purchases, modification of account information and even deletion of data.