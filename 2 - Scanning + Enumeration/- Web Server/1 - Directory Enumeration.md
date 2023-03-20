--- ---

Directory enumeration is the process of obtaining a list of files and directories from a file system. This can be done using various command-line tools such as 'ls' on Linux and macOS, and 'dir' on Windows. 

Enumeration is often used by attackers to gather information about a target system during the reconnaissance phase of a cyber attack. It can also be used by system administrators to identify and manage files and directories on a file system.

Gobuster
```
gobuster dir -u WEBSITE -w WORDLIST -x "html,txt,php,zip,..." -t 25 --timeout Xs  --exclude-length X
```
- -u = URL
- -w = Wordlist
- -x = Append at the end of the directory
- -t = treats
- --timeout = Add some time between respond
- --exclude-lenght = Exclude result that has X bytes of data

---

More Information ---> [[Red Team/2 - Scanning + Enumeration/2 - Enumeration/Directory/• Gobuster]]