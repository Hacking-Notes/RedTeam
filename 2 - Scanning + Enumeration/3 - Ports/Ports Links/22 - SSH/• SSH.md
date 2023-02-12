--- ---

<h2>Find SSH Port</h2>

Nmap
```
nmap -sV -SC IP -p20,21
```

- Possible to find SSH on an other port

---

<h2>Attack</h2>

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

<h2>Connection</h2>

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