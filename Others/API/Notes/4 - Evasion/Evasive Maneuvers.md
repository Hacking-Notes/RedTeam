--- ---

<h2>Introduction</h2>

Many APIs in the wild will not be exploited as easily as the deliberately vulnerable applications that we've been up against in this course. Often times security controls like web applications firewalls (WAFs) and rate-limiting can block your attacks. Security controls may differ from one API provider to the next, but at a high level, they will have some threshold for malicious activity that will trigger a response. WAFs, for example, can be triggered by a wide variety of things, like:

-   Too many requests for resources that do not exist.
-   Too many requests within a certain amount of time
-   Common attack attempts, like SQL injection and XSS attacks
-   Abnormal behavior, like tests for authorization vulnerabilities

Evading security controls is a process of trial and error. Some security controls may not advertise their presence with response headers; instead, they may wait in secret for your misstep. The following measures can be effective at evading or bypassing these restrictions.

---

## String Terminators

Null bytes and other combinations of symbols are often interpreted as string terminators used to end a string. If these symbols are not filtered out, they could terminate the API security control filters that may be in place. When you are able to successfully send a null byte it is interpreted by many back-end programming languages as a signifier to stop processing. If the null byte is processed by a back-end program that validates user input, then the security control could be bypassed because it stops processing the following input. Here is a list of potential string terminators you can use:

```
%00
0x00
//
;
%
!
?
[]
%5B%5D
%09
%0a
%0b
%0c
%0e
```

String terminators can be placed in different parts of the request, like the path or POST body, to attempt to bypass any restrictions in place. For example, in the following injection attack to the user profile endpoint, the null bytes entered into the payload could bypass filtering

```
POST /api/v1/user/profile/update
[…]
{
“uname”: “hapihacker”
“pass”: "%00'OR 1=1"
}
```

In this example, input validation measures might be bypassed due to the null byte placed before the SQL injection attempt.

---

## Case Switching

Sometimes API security controls are pretty easy to beat. If a security control is built around the literal spelling and case of the components within a request, then case switching can be an effective technique to bypass the controls. Case switching is the literal switching of the case of the letters within the URL path or payload. For example, take the following POST requests. Let’s say you were targeting a social media site by attempting an IDOR attack against a uid parameter in the following POST request:  

```
POST /api/myprofile 
[…] 
{uid=§0001§} 
```

 An API may leverage rate-limiting to only allow 100 requests per minute. Based on the length of the uid value, you know that to brute force it you’ll need to send 10,000 requests to exhaust all possibilities. To bypass rate-limiting or other WAF controls you may be able to simply alter the URL path by switching upper- and lower-case letters in the path: 

- POST /api/myProfile 
- POST /api/MyProfile 
- POST /aPi/MypRoFiLe 

Each of these path iterations could cause the API provider to handle the request differently, potentially bypassing the rate limit. In some cases, a control like rate-limiting may disappear completely with a different spelling or the new spelling may have its own renewed rate limit. In the case where rate-limiting is no longer applied, you can just send over as many requests as you need to the endpoint with the casing switched. In the case where rate-limiting is renewed, you could use the BurpSuite Pitchfork attack to pair a certain number of attacks to a certain number of brute-force attempts.

For example:

- POST /api/myprofile paired with uid 001 - 100
- POST /api/Myprofile paired with uid 101 - 200
- POST /api/mYprofile paired with uid 201 - 300

If you were using Burp Suite’s Intruder for this attack, you could set the Attack Type to Pitchfork and use the same value for both payload positions. This tactic allows you to use the smallest number of requests required to brute force the uid.  

--- ---

## Encoding Payloads

To take your WAF-bypassing attempts to the next level, try encoding payloads. Encoded payloads can often trick WAFs while still being processed by the target application or database. Even if the WAF or an input-validation measure blocks certain characters or strings, they might miss encoded versions of those characters. Alternatively, you could also try double encoding your attacks.

Imagine that the API provider has a control in place that provides one round of decoding to requests that are received.

URL Encoded Payload: %27%20%4f%52%20%31%3d%31%3b

API Provider URL Decoder: ' OR 1=1;

WAF Rules detect a fairly obvious SQL Injection attack and block the payload.

Double URL Encoded Payload: %25%32%37%25%32%30%25%34%66%25%35%32%25%32%30%25%33%31%25%33%64%25%33%31%25%33%62

API Provider URL Decoder: %27%20%4f%52%20%31%3d%31%3b

This could perhaps pass by a bad WAF rule to later be decoded and interpreted. Let's check out how we can practically apply evasive techniques to our attacks with Burp Suite and WFuzz.