--- ---

<h2>General</h2>

SSH (Secure Shell) port forwarding, also known as SSH tunneling, is a technique that allows the user to securely forward traffic from one network to another through an SSH connection. This can be useful for securely accessing a network that is behind a firewall or for accessing network resources that are not directly reachable from the user's location.

There are several types of SSH port forwarding, including local, remote, and dynamic forwarding.

Local forwarding allows the user to forward traffic from their local machine to a remote network or resource through the SSH connection. This can be useful for accessing a database or web application that is running on a remote server that is not directly reachable from the user's location.

Remote forwarding allows the user to forward traffic from a remote machine to their local machine through the SSH connection. This can be useful for accessing resources on the user's local network, such as a home network, while they are away from home.

Dynamic forwarding allows the user to forward all traffic from their local machine through the SSH connection to a SOCKS proxy server. This can be useful for securely accessing networks that are behind a firewall or for accessing resources that are not directly reachable from the user's location.

![[Pasted image 20221011114851.png]]

---
<h2>Commands</h2>

### SSH Remote Port Forwarding

SSH Remote Port Forwarding is a feature of SSH that allows you to forward a remote port on a server to a local port on your computer. This means that any traffic sent to the remote port on the server is forwarded to the local port on your computer, and any responses from the local port are sent back to the remote port.

Command (From the intermediary machine)
```Terminal
# Connect to the Machine via SSH (For example)  --> Za stand for subdomain
`ssh za\\<AD Username>@MACHINE_DOMAIN_NAME

# Reverse SHH tunnelling
ssh -R [remote_port]:[local_host]:[local_port] -N [user]@[remote_host]
```
- The "Local Port" forwarding is done trough the intermediary and the target host your trying to connect. The remote connection is made from the intermediary trought your pc



### SSH Local Port Forwarding

SSH Local Port Forwarding is a feature of SSH that allows a user to forward a local port on their computer to a remote server. This allows the user to access a service running on the remote server, as if it were running on their local machine, while also encrypting the traffic between the local and remote machines for added security. It is done by specifying the local port, remote host and remote port on the syntax to establish the connection.

Command (Attacking Machine)
```
ssh -L [local_port]:[remote_host]:[remote_port] -N [user]@[remote_host]
```
- The "Local Port" in SSH Local Port Forwarding refers to the port on the user's local machine that will be used as an entry point to access the target port on the remote host. It acts as a bridge between the local machine and the target machine allowing the user to reach the desired destination.
- The "Remote Host" and "Remote Port" in SSH Local Port Forwarding refer to the final destination machine and the specific port on that machine that the user wants to access. This internal port on the remote host is the target of the connection established by the user using the specified syntax.



### SOCKS Dynamic Port Forwarding

SOCKS Dynamic Port Forwarding is a feature of the SOCKS (Socket Secure) protocol that allows a user to forward incoming connections from a local port on their computer to a remote server, and then forward the response back to the original client. This allows the user to access a service on the remote server, while masking their IP address and encrypting the connection.

Command (Attacking Machine)
```
# Setup Proxychain
sudo nano /etc/proxychains.conf
    # socks4  127.0.0.1 9050

# Run SSH on the target port select in the proxychain config
ssh -D 9050 [user]@[remote_host]

# Run proxychain before your commands to use the traffic of the intermediary machine
proxychain nmap ...
```
