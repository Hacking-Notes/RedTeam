--- ---
<h3>What is Nslookup?</h3>
Nslookup is a command-line tool used to query the Domain Name System (DNS) to obtain domain name or IP address mapping or other DNS records. It is a utility available on most operating systems, including Windows, macOS, and Linux.

---
<h3>Common uses and Commands</h3>
-   **Lookup IP address of a domain**: To find the IP address of a domain, you can run the following command: `nslookup example.com`. 

-   **Reverse lookup**: You can perform a reverse lookup to find the domain name associated with an IP address. To do this, run the following command: `nslookup -type=PTR IP_address`

-   **Specify a DNS server**: By default, nslookup uses the default DNS server configured on your system. You can specify a different DNS server to use by running the following command: `nslookup example.com DNS_server`

-   **Query a specific DNS record type**: You can query for a specific type of DNS record, such as MX, SOA, or NS, by using the "-type" option. For example, to query for the MX record of a domain, run the following command: `nslookup -type=MX example.com`.
	- More Options       ---> A, AAAA, CNAME, MX, SQA, TXT

---
<h3>More Information</h3>
More information and documentation for NSlookup: [Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup)

<iframe src="https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup" width="100%" height="1300"></iframe>