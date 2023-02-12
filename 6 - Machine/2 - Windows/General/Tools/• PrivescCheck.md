--- ---

<h2>Top Commands</h2>

Powershell
```shell-session
PS C:\> Set-ExecutionPolicy Bypass -Scope process -Force
PS C:\> . .\PrivescCheck.ps1
PS C:\> Invoke-PrivescCheck
```

- Set-ExecutionPolicy...        ---> bypass the execution policy restrictions. To achieve this, you can use the `Set-ExecutionPolicy` cmdlet as shown below.

https://github.com/itm4n/PrivescCheck

---

<h2>What is PrivescCheck</h2>

This script aims to enumerate common Windows configuration issues that can be leveraged for local privilege escalation. It also gathers various information that might be useful for exploitation and/or post-exploitation.