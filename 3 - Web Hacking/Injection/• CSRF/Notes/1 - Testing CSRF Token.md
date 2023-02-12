--- ---

Testing CSRF tokens with Burp Suite: (Possible to combine multiples technique to archive your goals)

-   ==Remove a CSRF token== from a request, you can use the "Intercept" feature in Burp Suite. This allows you to intercept and modify requests before they are sent to the server. Once you have intercepted the request, you can remove the CSRF token from the request and forward it to the server.

-   ==Change the request method==, changing a GET request to a POST request. Once you have modified the request, you can forward it to the server to see how the application handles the different request method.

	-  ==Change the resquest (OVERWRITE)==, It may not be possible to change a POST request to a GET request, but it is sometimes possible to override this by modifying the PoC provided by BurpSuite and forcing the request to be made via a GET request.

- ==Using redirect vulnerability==,The process of changing a user's email address may be hindered by security measures such as the refer header, which requires the user to first visit a page on the website before making changes. However, if a client-side redirect vulnerability is discovered, an attacker may be able to exploit it for a CSRF attack. This is done by crafting a GET request in the redirect, which can then be used to perform malicious actions, such as changing various informations.

- ==Change CSRF token from another user==, this can be done by intercepting a request that includes a CSRF token, extracting the token from the request and using it in another user request, and forwarding the modified request to the server to see if it is still accepted. If the request is accepted using a token of another user, it may indicate that the tokens are not properly linked to the user session and the application may be vulnerable to CSRF attacks.
