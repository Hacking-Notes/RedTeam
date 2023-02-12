--- ---

<h2>Sharphound</h2>

- Sharphound
	Sharphound is the enumeration tool of Bloodhound. It is used to enumerate the AD information that can then be visually displayed in Bloodhound.
	ㅤ
	There are three different Sharphound collectors:
		-   **Sharphound.ps1** - PowerShell script for running Sharphound. However, the latest release of Sharphound has stopped releasing the Powershell script version. This version is good to use with RATs since the script can be loaded directly into memory, evading on-disk AV scans.  
		-   **Sharphound.exe** - A Windows executable version for running Sharphound.
		-   **AzureHound.ps1** - PowerShell script for running Sharphound for Azure (Microsoft Cloud Computing Services) instances. Bloodhound can ingest data enumerated from Azure to find attack paths related to the configuration of Azure Identity and Access Management.

Commands (command to launch on the target machine to gather information)
```
Sharphound.exe --CollectionMethods all --Domain DOMAIN_NAME --ExcludeDCs
```


<h2>Bloodhound</h2>

Launch Neo4j (If not installed check here [Here](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-neo4j-on-ubuntu-20-04))
```
sudo systemctl start neo4j       ---> Start Service
sudo neo4j start                 ---> Start Neo4j

sudo neo4j stop                  ---> Stop Neo4j
sudo systemctl stop neo4j        ---> Stop Service
```

Launch Bloodhound
```
./Bloodhound

# credential ---> User: Neo4j Pass: bloodhound
```

Attack Paths
- Database Information    ---> General Information of the data imported
- Node Information           ---> Display information about a node selected (User, Group,...)
	- **Overview** - Provides summaries information such as the number of active sessions the account has and if it can reach high-value targets.  
	-   **Node Properties** - Shows information regarding the AD account, such as the display name and the title.  
	-   **Extra Properties** - Provides more detailed AD information such as the distinguished name and when the account was created.  
	-   **Group Membership** - Shows information regarding the groups that the account is a member of.  
	-   **Local Admin Rights** - Provides information on domain-joined hosts where the account has administrative privileges.  
	-   **Execution Rights** - Provides information on special privileges such as the ability to RDP into a machine.  
	-   **Outbound Control Rights** - Shows information regarding AD objects where this account has permissions to modify their attributes.  
	-   **Inbound Control Rights** -  Provides information regarding AD objects that can modify the attributes of this account.
- Analysis                          ---> Get analysis of paths (Like shorter to X, ...)

![[Pasted image 20230110193410.png]]
- Example of attack path (Searching from user you have creds --> Get to the Domain Admin (T1))
	1.  Use our AD credentials to RDP into **THMJMP1**.
	2.  Look for a privilege escalation vector on the host that would provide us with Administrative access.
	3.  Using Administrative access, we can use credential harvesting techniques and tools such as Mimikatz.
	4.  Since the T1 Admin has an active session on **THMJMP1**, our credential harvesting would provide us with the NTLM hash of the associated account.

---

Benefits

-   Provides a GUI for AD enumeration.
-   Has the ability to show attack paths for the enumerated AD information.
-   Provides more profound insights into AD objects that usually require several manual queries to recover.

Drawbacks

-   Requires the execution of Sharphound, which is noisy and can often be detected by AV or EDR solutions.