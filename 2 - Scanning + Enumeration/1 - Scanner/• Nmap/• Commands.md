--- ---
<h3>What is Nmap?</h3>
Nmap (Network Mapper) is a popular open-source tool used for network exploration and security auditing. It is designed to scan large networks and identify potential vulnerabilities and security risks.

Nmap works by sending packets to target hosts and analyzing the responses to determine which ports are open, which services are running, and which operating systems are being used. It can also perform various advanced scans, such as OS detection, version detection, and service fingerprinting.

---
<h4>Common Use and Commands:</h4>
Nmap is commonly used by security professionals, system administrators, and penetration testers to scan networks and identify potential vulnerabilities and security issues.

The following are some common commands used in Nmap:

Usual Commands
```
#First Scan
nmap -ip

#Second Scan (Normal)
nmap -sC -sV -A IP -p (PORT FOUND) --min-rate=9856

#Second Scan (Hidding)
nmap -sC -sV -A -f IP -p (PORT FOUND) --min-rate=9856 --data-length 25
```

Additional Commands
```
-sT                         ---> TCP
-sU                         ---> UDP

-sC                         ---> Scan Script (Run default script)
-sV                         ---> Find port version
-sS                         ---> 
-sA                         ---> Check Firewall filter
-iL                         ---> Scan from list.txt IP
-O                          ---> OS Dectection
-A                          ---> Enable OS detection, version detection...

-f                          ---> Fragment parkets
--min-rate=9856             ---> Send packets at the rate of 9956 per second
--data-length 25            ---> add garbage data to packets (Avoid IPS/IDS signature)
-sn                         ---> Send null package (HIDING)
-Pn                         ---> Dont ping
--spoof-mac                 ---> Try to spoof address (Work localy)

-oN, -oG, -oX               ---> Export Format

/24                         ---> Check all 10.0.1.HERE
/16                         ---> Check all 10.0.HERE.HERE
```

- Options
	- Timing                                  ---> T0-T5 (0=Paranoid and 5=Insane Fast)
	- Parelel                                  ---> Use --source-port 80 (Will act like http request)
	- Random Scanning               ---> Use nmap IP/24 --randomize-hosts
	- MAC Adress Spoofing         ---> Nmap IP --spoof-mac (X)
	- Send Bad Checksums         ---> Nmap IP --badsum

Nmap supports various options and flags that can be used to customize the scan and generate detailed reports, such as setting the output format, enabling verbose logging, and excluding certain hosts or ports.

---
<h3>More Information</h3>
For more information on Nmap, including the latest updates and documentation, please visit the project's official website: https://nmap.org/

<iframe src="https://nmap.org/" width="100%" height="1300"></iframe>