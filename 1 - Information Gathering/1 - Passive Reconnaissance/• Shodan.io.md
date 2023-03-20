--- ---
<h2>What is Shodan</h2>
When you are tasked to run a penetration test against specific targets, as part of the passive reconnaissance phase, a service like [Shodan.io](https://www.shodan.io/) can be helpful to learn various pieces of information about the client’s network, without actively connecting to it. Furthermore, on the defensive side, you can use different services from Shodan.io to learn about connected and exposed devices belonging to your organization.

Shodan.io tries to connect to every device reachable online to build a search engine of connected “things” in contrast with a search engine for web pages. Once it gets a response, it collects all the information related to the service and saves it in the database to make it searchable. Consider the saved record of one of tryhackme.com’s servers.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/a8ac6c22a64b8413ee8d02c2224eddac.png)  

This record shows a web server; however, as mentioned already, Shodan.io collects information related to any device it can find connected online. Searching for `tryhackme.com` on Shodan.io will display at least the record shown in the screenshot above. Via this Shodan.io search result, we can learn several things related to our search, such as:

-   IP address
-   hosting company
-   geographic location
-   server type and version

You may also try searching for the IP addresses you have obtained from DNS lookups. These are, of course, more subject to change. On their [help page](https://help.shodan.io/the-basics/search-query-fundamentals), you can learn about all the search options available at Shodan.io, and you are encouraged to join TryHackMe’s [Shodan.io](https://tryhackme.com/room/shodan).

---
<h2>Website</h2>
```Terminal
- https://www.shodan.io
```
