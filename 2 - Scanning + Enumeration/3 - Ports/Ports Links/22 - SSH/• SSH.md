--- ---
<h2>What is SSH</h2>
SSH (Secure Shell) is a network protocol that is used to securely connect to remote systems over an unsecured network, such as the internet. SSH provides a secure encrypted connection between a client and a server, allowing users to remotely access and control systems and services.

SSH works by creating a secure channel between the client and the server using encryption algorithms to secure the connection. This secure channel can be used to run various network services and applications, such as a command shell, file transfer protocol, or remote desktop application.

---
<h3>Find SSH Port</h3>
Nmap
```
nmap -sV -SC IP -p20,21
```

- Possible to find SSH on an other port

---
<h3>Attack</h3>
- Brute Force
```Terminal
hydra -t X -l USERNAME -P WORDLIST -vV IP ssh
```

Let's break it down:

- hydra      --->  Runs the hydra tool  
- -t X         --->  Number of parallel connections per target  
- -l             ---> Points to the user who's account you're trying to compromise  
- -P            ---> Points to the file containing the list of possible passwords  
- -vV          ---> Sets verbose mode to very verbose, shows login + password 
- IP             ---> The IP address of the target machine  
- ssh           --->  Sets the protocol

---
<h3>Connection</h3>
<h4>Linux Connection</h4>
- Command
```Terminal
ssh USER@IP
ssh -i id_rsa USER@IP
```

- id_rsa                ---> Private
- id_rsa.pub         ---> Public (Contain Username)

<h4>Windows Connection</h4>
- Option
```Terminal
Remmina (tool)
```

<h4>Active Directory Connection</h4>
- Options
```Terminal
- Remmina (tool)

or

- ssh AD-DOMAIN\\<AD Username>@URL/IP/AD-ADDRESS        ---> From Linux terminal
```