--- ---
<h2>What is VNC</h2>
VNC (Virtual Network Computing) is a graphical desktop sharing system that allows a user to remotely control the desktop of another computer or server. VNC typically uses ports 5900-5906 as its default ports for communication between the VNC client and VNC server.

The exact port number used by VNC depends on the display number of the remote desktop that is being shared. For example, if the remote desktop is being shared on display number 1, then the VNC server will listen on port 5901 (5900 + display number).

In addition to the default VNC ports, some VNC implementations may use other ports for specific purposes. For example, some implementations may use port 5800 or 5801 for web-based VNC sessions, which allow users to access a VNC session through a web browser.

It's important to note that VNC is not typically used over the public internet due to security concerns, as it is a plaintext protocol that can be intercepted and potentially exploited by attackers. Instead, it is often used in local network environments where the connection between the client and server can be secured through other means, such as VPN or SSH tunnels.

---
<h3>Attack</h3>
- Brute Forcing
```
hydra -s 5900/5901 -P PASSWORD.txt -t 4 IP vnc
```

---
<h3>Connection</h3>
- Connection
```
#VNCviewer
vncviewer IP

#Remmina
GUI
```