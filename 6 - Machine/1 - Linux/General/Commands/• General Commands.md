--- ---

#### - Common & Most Used (Recursive)
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

- |                                   ---> procede to the second command before output
- ;                                   ---> Add a second command in the output

- pwd                                 ---> Print the current working directory.
- mkdir [directory_name]              ---> Create a new directory.
- rmdir [directory_name]              ---> Remove a directory (must be empty).
- touch [file_name]                   ---> Create a new empty file.
- cp [source] [destination]           ---> Copy files or directories.
- mv [source] [destination]           ---> Move or rename files or directories.
- rm [file]                           ---> Remove file. Be cautious,this is irreversible.

- grep [pattern] [file]               ---> Search for a specific pattern in a file.
- chmod [permissions] [file]          ---> Change file permissions.
- chown [user]:[group] [file]         ---> Change file ownership.

- man [command]                       ---> Display the manual page for a command.
- find [directory] -name [filename]   ---> Search for files or directories by name.
- wget [URL]                          ---> Download files from the web.
- curl [URL]                          ---> Transfer data from or to a server.
- grep                                ---> Search for patterns within files.
- awk                                 ---> A powerful text processing tool.

- top                                 ---> Display Linux processes.
- ps                                  ---> Display information about running processes.
- kill [PID]                          ---> Terminate a process by its process ID.

- ssh [user]@[hostname]             ---> Connect to a remote machine using SSH.
- rsync                             ---> Efficiently sync files/directories two locations.
- scp [file] [user]@[hostname]:[destination_path] ---> Securely copy files between machines.

- history                           ---> Display the command history.
- sudo                              ---> Execute a command as the superuser or another user.

- du -sh [directory]                ---> Display the total size of a directory.
- df -h                             ---> Display disk space usage.
- ln -s [target] [link_name]        ---> Create symbolic links.
```


#### - Searching
```Terminal
# General
- pwd                                ---> Print current directory
- whatis X (ex: sudo)                ---> Explain what X do (ex: explain what sudo is)
- whereis X                          ---> Searching where is X in file system (ex: /etc/.../X)
- type COMMAND                       ---> Decompose the ALIAS from command
- cat file.txt                       ---> output the text
- head -n 5 file.txt                 ---> output the first 5 lines of the document
- tail -n 5 file.txt                 ---> output the last 5 lines of the document
- tail -n +2 file.txt                ---> Output everything after the second line

- >                                  ---> Create output
- 2>                                 ---> Output error to somewhere you want
- 2>&1                               ---> Output everything (errors & else) somewhere
- >>                                 ---> Append text to a file
- &                                  ---> Run command in background
- &&                                 ---> Combine commands

- which                              ---> Find the file location (BEST)

- find DIRECTORY -name FILENAME      ---> Search for a file
- find DIRECTORY -name "*.txt"       ---> Find all .TXT file in directory location
- find DIRECTORY - group XYZ         ---> Search for file owner by XYZ group
- find ~/ -perm +rwx                 ---> search for file having permition rwx

- locate                             ---> Locate create DB index all files on system to search
- suo updatedb                       ---> Update database for new files that need to be index
- locate XYZ                         ---> Search instantly for XYZ trought all the drive index


# AWK (Like grep but more advance)
- awk '{print $1, $4}' TEST.txt      ---> Retrieve parameter Num 1 & 4 of each lines
- awk '$4 > 30000' TEST.txt          ---> Retrieve parameter greater then 30K each lines
- awk 'BEGIN {OFS=":"} {print $1, $4}' TEST.txt ---> Retrieve & print Num 1 & 4 separated by ":"


# Grep (GREP IS CASE SENSITIVE)
- grep "Text"                        ---> Check Text (-i=Allcases, -r=All folder file)
- grep -i "ReD"                      ---> Case insensive (Any lower/upper will match)
- grep -r "XYZ" /Path/file           ---> Check All "XYZ" in a folder and sub-folder 
- grep "ap[pe]"                      ---> Match "app" or "ape" (give options or matching)
- grep -e "X|Y|Z"                    ---> Searching for any match for X or Y or Z
Examples
	- grep -e "^1[0-2]|[5-6]\/"      ---> Will search for starting by 1 followed by a number between 0-2 or 5-6 and followed by a / (\/ is to evade the character /)
	- 

- cat x.txt | grep -e "X|Y"          ---> Grep regular expression search for X & Y
- cat x.txt | grep -e "^1[0-2]"      ---> Search lines that start with 1 followed by 0-2
- cat x.txt | grep -e "Day$"         ---> End with Day ($ = end / ^ = start of line)
- cat x.txt | grep -e "D.y"          ---> Find Any caraters between two letters (.)
```


#### - Install packages
```
# APT
- apt-get install PACK1 PACK2 ...     ---> Install packages on machine
- apt search echo (ex)                ---> Search for echo in apt reprository
- apt list m* (ex)                    ---> List all packages starting with m
- apt-get remove APP                  ---> Remove app
- apt-get autoremove                  ---> Remove library not used by packages

# Snap
- snap install PACK1                  ---> Install package
- snap list                           ---> Show packages installed
- snap remove APP                     ---> Remove app

- Wich APP                            ---> Show command location and associated package manager

# Install App from Repositories
- wget REPOSITORY-KEY.asc             ---> Get the repo key
- sudo apt-key add REPOSITORY-KEY.asc ---> Add the key to the trusted key
- sudo nano /etc/apt/sources.list     ---> Add the repo in the repo list for apt-get
	- deb http://download.webmin.com/download/repository sarge contrib
```


#### - Network
```
- nslookup DOMAIN                    ---> Check DNS record (MX, CNAME, ...)
- ip -br addr                        ---> BEST WAY TO CHECK NETWORK ADDRESS & STATUS 
- ip a                               ---> Easiest and fastest way to get IP info
- netstat -tuna                      ---> Show ports and status (Open/Close)
- netstat -natp                      ---> Show ports (a= active, t=TCP, p=program)
- ss -tuna                           ---> Show ports and status (Open/Close) - SAME
- ss -natp                           ---> Show ports (a= active, t=TCP, p=program)
- traceroute www.something.com       ---> See routing
- systemctl restart systemd-networkd ---> Restart network
- systemctl restart systemd-resolved ---> Restart resolved srv (NEEDED AFTER NETWORK)

- nmcli device status                ---> Show available network device and status
- nmcli device show DEVICENAME       ---> More info on device (DEVICE NAME=CONNECTION)
- nmcli connection edit DEVICENAME   ---> Command prompt that enable you to change value
	- set ipv4.whatneedtochange NEW-VALUE ---> Give new value to the device
	- save temporary                      ---> Make it effective until reboot
	- save persistent                     ---> Make it effective now til changed

- cat /etc/hosts                     ---> Show DNS from the machine (IP linked to Nameserver)
- cat /etc/resolv.conf               ---> Show where we will querry the DNS IP

- wget -O - -q https://checkip.amazonaws.com   ---> Find your IP address in terminal
```


#### - Files / File system / Partitions & Volumes
```
# View file
FILE PERMISSION
1 = Execute (x)
2 = Wite (w)
4 = Read (r)

# Removing file
- rm file.txt                        ---> Removing a file
- rmdir folder                       ---> Removing an empty directory
- rm -r ANYTHING                     ---> Removing anything without error


# Destroy/Delete Files
shred FILE     ---> Destoy redability of a file


# Copying files
- cp filename /LOCATION/NEWFILENAME  ---> Copying files
- cp filename NEWFILENAME            ---> Renaming a file 

- sudo dd if=/INPUTFILE/sda(ex) of=~/OUTPUTFILE  --> if=inputfile, of=outpufile, Copy drive
- sudo dd if=/INPUTFILE/sda(ex) bs=1m | gzip -o > ~/OUTPUT-LOCATION ---> Copying and compress the copyed file. bs=Block size, gzip -o > will gzip and output to a location
	- sda ---> First drive
	- sdb ---> Second drive
	- sdc ---> Third drive
	- ...


# Moving files / renaming files
- mv XYZ.txt /something/XYZ.txt     ---> Moving a file
- mv XYZ.txt ZYX.txt                ---> Renaming a file


# Symbolic Links
- ln LOCATION/FILE LINK-LOCATION/SYMBO-NAME     ---> Create hardlink (Better for Same disk)
- ln -s LOCATION/FILE LINK-LOCATION/SYMBO-NAME  ---> Create a softlink


# Creating File
- mkdir                              ---> Create a folder
- touch                              ---> Create a document
- anew                               ---> Create anew document with output
- echo                               ---> Echo text


# Partitions and volumes

- sudo iotop                         ---> Show disk read/bits every seconds
- sudo iotop -a                      ---> Show disk read/bits cumulated time
- sudo iostat                        ---> Show disk utilisation and who use it (System? User?)

MBR  --> Master boot record (Up to 4 partitions)
GPT  --> GUID (Globally Unique Identifier) Partition Table (Up to 128 partitions)

- du -sh /FOLDER                     ---> Display amount of space /FOLDER use & sub-folders
- sudo fdisk -l /dev/sdb             ---> Show partitions
- sudo fdisk /dev/sdb                ---> MBR (m)=menu (n)=create (d)=delete (p)=print
	- First sector 2048 = boot record space occupy 2048 (enter)
	- +5G (Add 5 gigabit volume)
	- Last sector (default -> enter)
	- p -> check the new changes
	- w -> write the new changes
- sudo gdisk /dev/sdc                ---> GPT (m)=menu  (n)=create (d)=delete (p)=print
	- Partition Number -> select a number
	- First sector 2048 = boot record space occupy 2048 (enter)
	- +5G (Add 5 gigabit volume)
	- HEX or GUID tables -> Default Enter
	- ... Enter, Enter
	- p -> check the new changes
	- w -> write the new changes
- sudo parted /dev/sdb               ---> Work with MBR & GPT (Not Used by default) 

- gparted                            ---> If GUI, can use this to manage partitions


# Formating Partitions
- lsblk -f                           ---> Show available mounting volumes & formating types
- ls -l /usr/sbin/mk*                ---> Show all possible type of formating on this system
- sudo mkfs -t FORMATING-OPTION /dev/VOLUME-SELECTED ---> Format the volume with the option given


# Mounting Volumes and Files system
- df -h                              ---> Show mounting points of volumes & other info
- lsblk                              ---> Show available mounting volumes
- sudo mount /dev/sdb1 /mnt/FOLDER   ---> Mount sdb1 to mtn/FOLDER
- sudo mount -t ext4 /dev/sdb1 /mnt/FOLDER ---> Specify the format (not obligated)
- sudoedit /etc/fstab                ---> Add entry to mount after every bootup
	- /dev/sdb1 /mnt/FOLDER FILEFORMAT defaults 0 0
	- UUID=THE_UUID /mnt/FOLDER FILEFORMAT defaults 0 0 ---> Use UUID to mount volume
- sudo mount -a                      ---> Launch automaticly the fstab files
- sudo umount /dev/sdb1              ---> Unmount the partition


# LVM (Logical Volume Manager) - Using RAID 0,1,5 / Create virtual volume
LVM -> Physical Volumes (pv) | Group Volumes (vg) | Logical Volumes (lv) (end product)

- sudo pvdisplay                           ---> Show physical volumes
- sudo vgdisplay                           ---> Show volume groups
- sudo lvdisplay                           ---> Show virtual volumes

Mounting logical volumes can be apply the same way has normal volume to make them persistent (sudoedit /etc/fstab)
- lsblk                                    ---> Display volumes
	- /dev/sdb1 /mnt/FOLDER FILEFORMAT defaults 0 0
	- UUID=THE_UUID /mnt/FOLDER FILEFORMAT defaults 0 0 ---> Use UUID 

- sudo apt install lvm2                    ---> Install LVM if not already installed
- sudo pvcreate /dev/VOLUME1 /dev/VOLUME2  ---> Making them part of LVM
- sudo vgcreate vg1 /dev/sdb1 /dev/sdc1    ---> Merge Volumes in group (vg1 name is an example)
- sudo lvcreate -L 12G vg1 -n Virtvolume   ---> Create virtual volume (12G named Virt..)
- sudo vgextend GROUP /dev/NEW-VOLUME      ---> Adding new volume to group (make sure to pvcreate first)
- sudo lvresize -L +5G /dev/vgi/Virtvolume ---> Extend virtual volume size
- sudo resize2fs /dev/vgi/Virtvolume       ---> Extend volume (ext4) NEED DO THIS AFTER
- sudo lvremove /dev/vg1/Virtvolume        ---> Remove volume space (ext4) NEED DO ...
- sudo vgremove /dev/vg1                   ---> Remove volume space (ext4) NEED DO ...
- sudo pvremove /dev/sdb1 /dev/sdc1 /dev/vg1---> Remove volume space (ext4) NEED DO ...
```


##### - Popular Files
```
More info: https://www.pathname.com/fhs/pub/fhs-2.3.html

- /boot                ---> Kernel files
- /etc                 ---> Configuration files
- /lib                 ---> Libraries
- /mnt                 ---> mounting temporary files
- /var/log             ---> Log files
	- dmesg                ---> Show kernel logs
	- journalctl -u cron   ---> Show logs of cron jobs runned on the device

- usr/local/bin        ---> Locally compiled programs
- usr/local/etc        ---> Locally compiled programs

- /bin                 ---> Needed for system rescue
- /usr/bin             ---> Location of most user binary
- /sbin /usr/sbin      ---> Location of most system binary
- /usr                 ---> User storage
- /usr/share/bin       ---> Program other then apps, example: stuff appache migh use

- /proc                ---> Folder that contain the process that can be found in the command ps
- /sys                 ---> Kernel and boot stuff
- /dev                 ---> Device nodes, provide an interface through which software can interact with hardware devices. Ex: dev/sda = SATA hard drive, dev/ttyS0 = first serial port...
```


#### - User Management / Permissions / Groups / Password
```
- whoami                             ---> Print User
- id                                 ---> Print id, group, ... of current user
- id USER                            ---> Show id, group, ... of selected user
- chown [user]:[group] [file]        ---> Change file ownership.
- last                               ---> Show the last loggin in the current system
- who                                ---> Check who is currently loggin in the system
- w                                  ---> Show what current logged user are doing

- sudo cat /etc/passwd               ---> Show user information (groups, UID, Shell, ...)
- sudo cat /etc/shadow               ---> Show user password
- sudo cat /etc/gshadow              ---> Show group password
- sudo cat /etc/group                ---> Show user associated with groups


# Create Users / Delete users
- sudo useradd USER -c "USER X" -s /bin/sh -e 2023/12/31  ---> Create user, add name, add shell type, add expiration date (auto delete)
- sudo useradd USER -d /home/USERNAME -m -G sudo,adm USERNAME ---> Create user, create directory, -m = create home, -G = add to the suplementary groups sudo & adm
- sudo useradd "USER-NAME" USERNAME -p PASSWORD ---> Create user with name, username & password
- sudo usermod -l USER NEW-USERNAME    ---> Change user setting (ex: name, expiration..)
- sudo usermod -L USER                 ---> Lock User account (L=Lock)

- sudo userdel USERNAME                ---> Delete user but keep directory
- sudo userdel -rf USERNAME            ---> Delete user & all its directory (f=force, r=remove)
- sudo /etc/skel FILEX.XYZ             ---> Create file here will give file to every new users

- su USER                              ---> Switch User
- sudo passwd USER                     ---> Set password for a new user

- sudo chage -l USER                   ---> Show password age for the user (man chage --> More info)
- sudo chage -m 1 USER                 ---> User change passwd min 24h
- sudo chage -M 1 USER                 ---> USER change passwd max 24H (Change -M 1 to X after)
- sudoedit /etc/login.defs             ---> Set password policies for all users (easier management)
- sudoedit /etc/security/faillock.conf ---> Login faillure and lockout policies

- sudo chsh -s /bin/nolgin USER/SERVICE ---> Remove interactive shell


# Create Groups / Delete Groups
- sudo groupadd NAME               ---> Create a group
- less etc/group                   ---> Show all groups created
- groups                           ---> Show all the groups of the current user
- groups USER_X                    ---> Show all groups for USER_X
- sudo usermod -aG USERNAME        ---> Add group to user (-a=append / not remove other groups)
- sudo groupmod -n NEWNAME OLDNAME ---> Change group name

- newgrp GROUP                     ---> Will set the following action from this group

- sudo gpasswd -a USER GROUP       ---> Add USER to Group
- sudo gpasswd -d USER GROUP       ---> Remove USER from Group
- sudo gpasswd -a USER GROUP ; sudo gpasswd -A USER GROUP ---> Make a user admin of it's group (give him edit permission inside the group)

- ls -l                            ---> Files/permissions (First=User,S=Group,T=Other)
- drwxr-xr-x (Example)             ---> d=directory / User=read,write,execute / ...
- 4=Read 2=Write 1=Execute         ---> Permission set via number ex: 7=All perms
- chmod 740 file.txt (Example)     ---> User=All perms / Group=Read / Other=No perms
- chmod +r file.txt                ---> User=read and groups & other nothing
- chmod -r file.txt                ---> Remove read access to current user
- chmod u=rwx,g=rw,o=r file.txt    ---> Set permissions via letters
- chmod g-w file.txt (Example)     ---> Remove write to groupe (ex)
- less ~/.profile                  ---> Chamge default permission given on new file
	- #umask 022                   ---> U=0->ALL perms, G=2->R&E (7 - number (WEIRD))


# Sudo Permission
- ls -n                              ---> Enable you to see the user id and group id of a file
- sudo su -                          ---> Root shell with user password
- sudo nano sudoers (IN /etc)        ---> Change sudo permission for users
- sudo visudo       (IN /etc)        ---> Change sudo permission for users | Special shell that test the code before in save it (make sure there is nothing that will be broken)
	- Ex: Asavard ALL=(ALL) ALL
	- Ex: Asavard ALL=(Wmartin) /usr/bin/apt install, /usr/bin/apt upgrade... (Binary Location)
	- Ex: %GROUP-NAME ALL=(ALL) ALL
	-  USER/GROUP -> Connection host= -> (USER-HE-CAN-IMPERSONATE) -> COMMAND HE CAN RUN
- POLICY KIT ??? ---> urs/share/polkit-1 ???


#  Standard Linux permissions typically restrict file access beyond the first user listed. To grant access to additional users, you'd usually create a new group, add users to it, and assign file permissions accordingly. Handling access for multiple groups can be cumbersome, but there's a simpler solution.

If (+) is showed when performing ls -l, this mean that it contain other type of attribut
--- --- ---+ (EX: rwxr-xr-x+)        ---> Attributes can be seen by running getfacl FILENAME

- getfacl                            ---> check if ACL permission list is present
- getfacl FILE.txt                   ---> Show permission for this file (Normal + ACL perms)
- setfacl -m u:USER:rw FILE.txt      ---> Add User to the permission with rw 
- setfacl -x u:USER:rw FILE.txt      ---> Remove User to the permission with rW
- setfacl -m g:GROUP:rw FILE.txt     ---> Add Group to the permission with rw 
- setfacl -m d:u:USER:rw FILE.txt    ---> Set permission to a directory (Can be done to group)
```


#### - Process / System / Alias / Environement Variable
```
# Process
- ps -ef                             ---> List process ongoing
- top                                ---> Show task management
	- press m                        ---> List by (%) memorie
	NI --> Priority of process (Lower numbers will be prioritized for execution)
	- sudo nice -10 COMMAND          ---> Set initial NI for process priorisation
	- sudo renice 11 PID -u USER     ---> Change NI during run to 11 (ex), include PID and user
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
- Wich COMMAND                 ---> Show command location and associated package manager
- env                          ---> Show all environement variable for bash
- X=Something                  ---> Create environement var (echo $X = Some...)
- export X=Y                   ---> Let you export env var (Remind it to terminal)


# Alias
- alias NAME='PATH/ACTION'     ---> Create Alias
- unalias your_alias_name      ---> Remove Alias
- sudo nano ~/.bashrc          ---> Permanent Alias (Edit the file & add the alias)


# ???
- echo "export PATH=$PATH:~/go/bin" >> ~/.bashrc
```


#### - Binary (Compilling)
```
- Download the File
- tar -xvzf file.tar.gz     ---> Decompile the file
- cd file/src               ---> Go in the file where you have all the Makefile/C code/References
- make                      ---> Give you options of compiling depending of your system
- make clean OPTION         ---> Will compile the file in the run folder
```


#### - History & Record Commands
```
# History
- history                     ---> Show History of commands
- history clear               ---> Clear History of commands


# Register Command
- command | tee >> FILE.TXT
```


#### - Others
```Terminal
# Remote access (SSH)
- sudo apt install ssh
- sudo systemctl enable -now ssh ---> Enable SSH
- sudoedit /var/tmp/sshd_config  ---> Change SSH config (EX: port#, Hostkey, Certificate autotification and no password...)
- shh USER@IP                    ---> Connect to SSH


# File transfer
- Filezilla               ---> Good option if GUI available
- wget URL                ---> Download any pointing url
- curl URL                ---> Download urls/services/mails/.. (WGET on steroids)
- curl URL --output X.txt ---> Download urls/services/mails/.. to a X.txt

- rsync -azurP /FOLDER-SYNC /PATH-DESTINATION                  ---> LOCAL COPY
- NEED TO SSH IN OTHER MACHINE
- ... -azurP -e shh /FOLDER-SYNC USER@COMPUTER:/FULL-PATH-DEST ---> REMOTE COPY
- ... ... -e shh --exclude="*.mp3" --include=".*"...(Example)  ---> Exclude MP3
- ... ... -e shh --include=".*" --exclude="*.mp3"...(Example)  ---> Just MP3
- ... ... ... ... ... --dry-run ---> Enable to visualise changes before syncing
- -e shh= Using ssh for communication, a=archive, z=zip during transfer, u=update(not overwrite, r=recursive, P=outpout verbose


# Docker.io (Containers)
- sudo dockerd                      ---> Start docker
- sudo usermod -aG docker USERNAME  ---> Ading user to docker group, enable user to run docker stuff without beeing root (-a = Primary group | -G = Secondary group) - REBOOT
- docker ps                         ---> Show the docker process
- docker ps -a                      ---> Show all the docker process (Show history)
- docker images                     ---> Show a list of all the docker installed
- docker search ubuntu (EX)         ---> Search for docker images
- docker pull NAMEOFIMAGE           ---> Download the image to the computer
- https://hub.docker.com/           ---> Docker images (Best way to start)
- docker run --name helloworld      ---> Download and run helloworld
- docker run --name helloworld -it  ---> Run helloworld container and make it interactive
	- CTRL P & CTRL Q               ---> Process in background and quit
- docker attach NAME                ---> Connect back to the container 
- docker stop NAME                  ---> Stop container
- docker rm NAME                    ---> Remove the container


# Automate Docker container (Very powerfull)
- sudo apt install docker.io docker-compose
- nano docker-compose.yaml          ---> create docker configuration file to manage containers
	#CHECK CONTAINER DOCUMENTATION
	version: '3.7'
	services:
	  portainer:
	    container_name: DOCKERNAME
	    image: DOCKERFILENAME:VERSION (VERSION IS OPTIONAL DEPENDING WHAT YOU WANT TO INSTALL)
	    restart: 'always'           ---> Make it restart by default
	    ports:
	      - target: 'PORT1'
	        published: 'PORT1'
	        protocol: tcp
	      - target: 'PORT2'
	        published: 'PORT2'
	        protocol: tcp
	    volumes:                    ---> Provide Persistent storage
	      - type: bind
	        source: /var/run/docker.sock
	        target: /var/run/docker.sock
	      - type: bin
	        source: /srv/DOCKERNAME
	        target: /data/

- sudo mkdir /srv/DOCKERNMAE        ---> Create the directory to host the persistence data
- docker-compose up --datach        ---> Launch the configuration file in background


# Combine files together
- cat file1.txt file2.txt file3.txt > combined_list.txt


# Sort and remove duplicate
- sort combined_list.txt | uniq -u > cleaned_combined_list.txt


# Archive and Zipping
- tar -cf NEWFILECREATED.tar ./DIRECTORY-TO-TAR ---> Package files together & Archive them
- tar -czf Newfile.tgz *                        ---> Archive & gzip in current folder (* = All)
- tar -xzf file.tgz                             ---> Ungzip tar file


# Firewall Rules (Orders are important!!!)
- sudo ufw status                      ---> See firewall rules in place
- sudo ufw allow ssh                   ---> Allow SSH (22) trought the firewall
- sudo ufw deny ...                    ---> Deny ports
- sudo ufw prepend deny ...            ---> Add the Deny or Allow rule at the begiging
- sudo ufw numbered                    ---> Give you a list and number to insert rules at right spot
- sudo ufw insert NUMBER deny ...      ---> Add rules between two rules numbers
- sudo ufw allow 80/tcp comment "HTTP" ---> Allow HTTP (80) trought the firewall & add comment
- sudo ufw allow 20,21/tcp comment "FTP" ---> Services that need more then 1 port open
- sudo ufw allow 30000:40000/UDP ...     ---> Open range of ports
- sudo ufw allow 80,443,2000:3000/TCP ...---> Open range + specific ports

- sudo ufx prepend allow proto tcp from 192.168.0.0/24 to any port 22 ---> Allow any local computer trafic to ssh

# Time/Region/Localisation/keybord
- localectl              ---> Display information about the localisation, language, ...
- locale                 ---> Display saved variable
- locale currency_symbol ---> Display currency symbol
- date                   ---> Show the current date (What computer think it's)
- timedatectl set-ntp on ---> Set network time protocol ON (If not on by default)
- timedatectl list-timezones ---> Show all time zones (Chose Continent/city closer)
- sudo timedatectl set-timezone EXACT-NAME-&-CITY ---> Change dates to the region
- localectl list-locales              ---> Display possible settings for your machine
- localectl set-locale LAN=fr_FR.utf8 ---> Local set utf8/FR keyboard (Reboot after)

```
