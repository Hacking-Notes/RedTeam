--- ---

<h2>Manual Enumeration</h2>

- System Enumeration
```
systeminfo
- provides basic system information
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System
Type"

- Pulls down those three pieces of information quickly
wmic qfe

- Pulls down patching information
wmic qfe get Caption,Description,HotFixID,InstalledOn

- Pulls down that specific information on patches - makes it
cleaner

wmic logicaldisk get caption,description,providername
- List out all the drives
```

- User Enumeration
```
whoami /priv
- list of privs we have
- useful for token impersonation

whoami /groups
- list of groups the user is in

net user
- list of users on the machine

net user <username>
- enumerate specific information on a user

net localgroup
- list of local groups

net localgroup <groupname>
- See who is part of a specific group (i.e. administrator group)
```

- Network Enumeration
```
ipconfig /all- See network architecture of the machine
arp -a
- Look to see if there are other IPs or machines we can move to
route print
- Pull down the routing table to see what is communicating
netstat -ano
- See which ports are open and communicating
```

- Password Hunting
```
findstr /si password *.txt
- search for passwords with .txt filename in current directory
- can add others such as .ini and .config

netsh wlan show profile
- See which wireless networks user has connected to

netsh wlan show profile <SSID> key=clear
- Show clear-text password of the wireless networks

AV Enumeration
sc query <AV service>
- Pull down information on the specific service
- i.e. sc query windefend

sc queryex type= service
- Show all services running on the machine

netsh advfirewall firewall dump
- Dump firewall information

netsh firewall show state
- Older way to dump firewall informatoin

netsh firewall configuration
- Look at firwall configuratoinAutomated Enumeration--
```