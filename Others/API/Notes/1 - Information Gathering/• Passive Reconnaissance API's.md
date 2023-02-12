--- ---

<h2>Website Links</h2>

In general, searching for links containing "api" word in the search page will sometimes bring up interesting links. 

It can also be suitable to inspect network requests in inspector mode and tying to find some API links.

--- 

<h2>Subdomains</h2>

An other way of finding API can be by enumerating some domains. You might find some interecting element. (This can expose some subdomain use for api without containing the specific word "API")

Enumeration ---> [[Red Team/3 - Web Hacking/Brute Force/2 - Fuzz/Gobuster/• Commands]]

---

<h2>Google dorking</h2>

```
intitle:"api" site:"Target.com"
intitle:json site:target.com
```

```
inurl:"/api/v1" site:"Target.com"      ---> Change v1, v2 and v3
```

More information about Google Dorking ---> [[Red Team/Others/OSINT/Dorking/• Google Dorking]]

---

<h2>Git dorking (Github)</h2>

Sometime, entreprise post there code on github. It might be a good thing to search there. To make some relevent search, simply search in the search bar of github "TARGET API"

After taking a look around, you can check the issue tab in github. There might be some issue reported about some keys leaks that are still vulnerable.

![[Pasted image 20221122173136.png]]

Dorking
```
extension:json(OR OTHER EXTENSION) TARGET               ---> In github searchbar

"authorization:Bearer" TARGET                           ---> More information
filename:swagger.json TARGET                            ---> More information
```

---

<h2>Shodan</h2>
To search on shodan, simply search your target name in the searchbar

you can also search by content type
```
"content-type: application/json"   ---> Will give you some application running json

"wp-json"                          ---> Of Target is running wordpress (API)
```

---

<h2>WayBackMachine</h2>
Allow you to check older version of website. This might leak some old links that can give you access to specific elements.


