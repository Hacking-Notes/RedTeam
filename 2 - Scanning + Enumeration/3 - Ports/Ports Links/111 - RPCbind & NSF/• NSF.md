--- ---
<h2>What is NSF</h2>
NFS stands for "**Network File System**" and allows a system to share directories and files with others over a network. By using NFS, users and programs can access files on remote systems almost as if they were local files. It does this by mounting all, or a portion of a file system on a server. The portion of the file system that is mounted can be accessed by clients with whatever privileges are assigned to each file.

- **How does NFS work?**

	We don't need to understand the technical exchange in too much detail to be able to exploit NFS effectively- however if this is something that interests you, I would recommend this resource: [https://docs.oracle.com/cd/E19683-01/816-4882/6mb2ipq7l/index.html](https://docs.oracle.com/cd/E19683-01/816-4882/6mb2ipq7l/index.html)

	First, the client will request to mount a directory from a remote host on a local directory just the same way it can mount a physical device. The mount service will then act to connect to the relevant mount daemon using RPC.

	The server checks if the user has permission to mount whatever directory has been requested. It will then return a file handle which uniquely identifies each file and directory that is on the server.

	If someone wants to access a file using NFS, an RPC call is placed to NFSD (the NFS daemon) on the server. This call takes parameters such as:

	-    The file handle
	-    The name of the file to be accessed
	-    The user's, user ID
	-    The user's group ID  

	These are used in determining access rights to the specified file. This is what controls user permissions, I.E read and write of files.  

- **What runs NFS?**

	Using the NFS protocol, you can transfer files between computers running Windows and other non-Windows operating systems, such as Linux, MacOS or UNIX.

	A computer running Windows Server can act as an NFS file server for other non-Windows client computers. Likewise, NFS allows a Windows-based computer running Windows Server to access files stored on a non-Windows NFS server.

- **More Information:**

	Here are some resources that explain the technical implementation, and working of, NFS in more detail than I have covered here.

	[https://www.datto.com/library/what-is-nfs-file-share](https://www.datto.com/library/what-is-nfs-file-share)
	[http://nfs.sourceforge.net/](http://nfs.sourceforge.net/)
	[https://wiki.archlinux.org/index.php/NFS](https://wiki.archlinux.org/index.php/NFS)


---
<h3>Find NSF Port</h3>
Nmap
```
nmap -sV -SC IP -p111
```

- Possible to find NSF on an other port

---
<h3>Attack & Connection</h3>
- Mounting Vulnerable Shared Folder (NSF-COMMON)
```Terminal
sudo mount -t nfs IP:FOLDER /tmp/mount/ -nolock   (Connect to the shared file)

- /usr/sbin/showmount -e [IP]                     (List the NFS shares)
```

- mount             ---> Execute the mount command
- -t nfs               ---> Type of device to mount, then specify that it's NFS
- IP:share           ---> Target server IP and vulnerable share folder
- -nolock            ---> Specifies not to use NLM Locking

More information about NSF-COMMON ---> https://vitux.com/install-nfs-server-and-client-on-ubuntu/

- Exploitation (Set**SUID**)
```Terminal
Download Bash Script
- cp ~/Downloads/bash /DESTINATION FOLDER
- chmod +x bash && chmod +s bash
- ls -la bash (check file permission)
- ./bash -p (Run script with persistence (On SSH low privilege))
```

- More information
	**What is root_squash?**

	By default, on NFS shares- Root Squashing is enabled, and prevents anyone connecting to the NFS share from having root access to the NFS volume. Remote root users are assigned a user “nfsnobody” when connected, which has the least local privileges. Not what we want. However, if this is turned off, it can allow the creation of SUID bit files, allowing a remote user root access to the connected system.

	**SUID**

	So, what are files with the SUID bit set? Essentially, this means that the file or files can be run with the permissions of the file(s) owner/group. In this case, as the super-user. We can leverage this to get a shell with these privileges!

	**Method**

	This sounds complicated, but really- provided you're familiar with how SUID files work, it's fairly easy to understand. We're able to upload files to the NFS share, and control the permissions of these files. We can set the permissions of whatever we upload, in this case a bash shell executable. We can then log in through SSH, as we did in the previous task- and execute this executable to gain a root shell!

	**The Executable**

	Due to compatibility reasons, we'll use a standard Ubuntu Server 18.04 bash executable, the same as the server's- as we know from our nmap scan. You can download it [here](https://github.com/TheRealPoloMints/Blog/blob/master/Security%20Challenge%20Walkthroughs/Networks%202/bash). If you want to download it via the command line, be careful not to download the github page instead of the raw script. You can use `wget https://github.com/polo-sec/writing/raw/master/Security%20Challenge%20Walkthroughs/Networks%202/bash`.  

	**Mapped Out Pathway:**

	If this is still hard to follow, here's a step by step of the actions we're taking, and how they all tie together to allow us to gain a root shell:

	![[Pasted image 20220922212950.png]]

- Reverse Shell ---> https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#bash-tcp

