--- ---

LDAP (Lightweight Directory Access Protocol) is a hierarchical database structure used to store and manage information about users, computers, and other resources in a network environment. Similar to BloodHound, PowerShell can be used to interact with an LDAP hierarchy and explore its contents.

In PowerShell, you can use the `Get-ADObject` cmdlet to retrieve information from an LDAP hierarchy. This cmdlet allows you to specify a search base (the root of the hierarchy) and a filter to restrict the results to specific objects.

---

The following PowerShell command is to get all active directory user accounts. Note that we need to use  -Filter argument.

PowerShell
```shell-session
PS C:\Users\thm> Get-ADUser  -Filter *
DistinguishedName : CN=Administrator,CN=Users,DC=thmredteam,DC=com
Enabled           : True
GivenName         :
Name              : Administrator
ObjectClass       : user
ObjectGUID        : 4094d220-fb71-4de1-b5b2-ba18f6583c65
SamAccountName    : Administrator
SID               : S-1-5-21-1966530601-3185510712-10604624-500
Surname           :
UserPrincipalName :
PS C:\Users\thm>
```

We can also use the [LDAP hierarchical tree structure](http://www.ietf.org/rfc/rfc2253.txt) to find a user within the AD environment. The Distinguished Name (DN) is a collection of comma-separated key and value pairs used to identify unique records within the directory. The DN consists of Domain Component (DC), OrganizationalUnitName (OU), Common Name (CN), and others. The following "CN=User1,CN=Users,DC=thmredteam,DC=com" is an example of DN, which can be visualized as follow:  

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d617515c8cd8348d0b4e68f/room-content/764c72d40ec3d823b05d6473702e00f5.png)

Using the SearchBase option, we specify a specific Common-Name CN in the active directory. For example, we can specify to list any user(s) that part of Users.  

PowerShell
```shell-session
PS C:\Users\thm> Get-ADUser -Filter * -SearchBase "CN=Users,DC=THMREDTEAM,DC=COM"


DistinguishedName : CN=Administrator,CN=Users,DC=thmredteam,DC=com
Enabled           : True
GivenName         :
Name              : Administrator
ObjectClass       : user
ObjectGUID        : 4094d220-fb71-4de1-b5b2-ba18f6583c65
SamAccountName    : Administrator
SID               : S-1-5-21-1966530601-3185510712-10604624-500
Surname           :
UserPrincipalName :
```

```
Get-ADUser -Filter * -SearchBase "OU=THM,DC=THMREDTEAM,DC=COM" | Select-Object -Property NAME
```
