--- ---

<h2>Commands (Powershell)</h2>
Check Machine General Information
```
- systeminfo                   ---> Operating system, version, Hostname, hardware, ...
- systeminfo | findstr Domain  ---> Check if machine is Domain Joinned (AD)
```

- General
```Terminal
- cd
- dir                   ---> List directory (like ls)
- type                  ---> Display text of element (like cat)
- more                  ---> Display text of element (like cat)
- | clip                ---> Copy the result of the command (clipboard)
- | Findstr X           ---> Example tasklist | findstr firefox ---> (like grep linux)
- &&                    ---> Combine Tasks
- cls                   ---> Clear terminal
```

- File Permision
```Terminal
- icacls                ---> Find permision of a file
- cd qc                 ---> Find information application, user, binary path, ...

- assoc                 ---> List what program open what format (ex: MP4 = VLC)
- assoc .FILE-FORMAT=PROGRAM ---> Change the default program open format
```

- User
```Terminal
- whoami                 ---> Check who you are

- net users              ---> Check all local users
- net groups             ---> Check all local groups
```

- Network
```Terminal
- ipconfig             ---> Check ip information
- ipconfig /all        ---> Check ip information ++ (MAC Address, DNS, ...)
- ipcongif /release    ---> Remove old ip address (use renew after)
- ipconfig /renew      ---> Add new ip address
- ipconfig /flushdns   ---> Refresh cache for the DNS

- nslookup DOMAIN      ---> Check DNS record (MX, CNAME, ...)

- getmac /v            ---> Display MAC Address

- tracert (traceroute) ---> Traceroute Network
- ping

- netstat                     ---> Show open ports on the machine
- netstat -af                 ---> Show open ports on the machine (Bluetooth)
```

- Others
```
- ls env:               ---> List all then system variable
- get-help SOFTWARE     ---> Get help message (Like -help in linux)
- taskkill /PID ID /F   ---> Kill PID process
```

---

<h2>Windows GUID Commands</h2>

```Terminal
run ---> lusrmgr.msc (check user, groupes, permissions ...)

**Folder Explorer**
- %windir% ---> Will locate you directly to the windows folder

**Usefull Programes
- System Controle (Services, Tools, ...)
- System Information
- Computer managment (System Tools, Storage, and Services and Applications.)
- Task Scheduler (Create Task)
- Event Viewer (Check events that have occurred on the computer)
- Ressource Monitor
```

--- ---

<h2>Exploit Commands</h2>

```
- whoami /priv                 ---> Check the privilege of the user 
- /SVC                         ---> List all executable running
- systemeinfo (Hotfix's)       ---> Kernel Verion Path (Find id to exploit old kernel)

- net users
- net groups

- assoc                       ---> List what program open what format (ex: MP4 = VLC)
- assoc .FILE-FORMAT=PROGRAM  ---> Change the default program open format

- netsh advfirewall set allprofiles state off  ---> Turn off firewall

- netstat -af                 ---> Show open ports on the machine
```