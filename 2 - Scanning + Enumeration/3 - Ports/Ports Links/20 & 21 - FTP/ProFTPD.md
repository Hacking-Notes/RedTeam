--- ---
<h2>ProFTPd</h2>

![](https://i.imgur.com/L54MBzX.png)

ProFtpd is a free and open-source FTP server, compatible with Unix and Windows systems. Its also been vulnerable in the past software versions.

Lets get the version of ProFtpd. Use netcat to connect to the machine on the FTP port.

We can use searchsploit to find exploits for a particular software version.

You should have found an exploit from ProFtpd's [mod_copy module](http://www.proftpd.org/docs/contrib/mod_copy.html). 

The mod_copy module implements **SITE CPFR** and **SITE CPTO** commands, which can be used to copy files/directories from one place to another on the server. Any unauthenticated client can leverage these commands to copy files from any part of the filesystem to a chosen destination.

We know that the FTP service is running as the X user (from the file on the share) and an ssh key is generated for that user. 

We're now going to copy X user private key using SITE CPFR and SITE CPTO commands.

![](https://i.imgur.com/LajBhh2.png)  

We knew that the /var directory was a mount we could see. So we've now moved Kenobi's private key to the /var/tmp directory.

Lets mount the /var/tmp directory to our machine

```Terminal
mkdir /mnt/kenobiNFS  
mount machine_ip:/var /mnt/kenobiNFS  
ls -la /mnt/kenobiNFS
```

![](https://i.imgur.com/v8Ln4fu.png)

We now have a network mount on our deployed machine! We can go to /var/tmp and get the private key then login to Kenobi's account.

![](https://i.imgur.com/Vy4KkEl.png)