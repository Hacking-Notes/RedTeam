--- ---
<h2>What is MSRPC</h2>
Microsoft Remote Procedure Call, also known as a function call or a subroutine call, is [a protocol](http://searchmicroservices.techtarget.com/definition/Remote-Procedure-Call-RPC) that uses the client-server model that enables one program to request a service from a program on another computer, without having to understand the details of that computer's network.

---
<h3>Find MSRPC Port</h3>
Nmap
```
nmap -sV -SC IP -p135
```

- Possible to find MSRPC on an other port

---
<h3>Attack</h3>
- User Enumeration
```Terminal
Enum4Linux          ---> https://github.com/CiscoCXSecurity/enum4linux
```

Enum4Linux Commands

- -U             get userlist  
- -M             get machine list  
- -N             get namelist dump (different from -U and-M)  
- -S             get sharelist  
- -P             get password policy information  
- -G             get group and member list

- -a             all of the above (full basic enumeration)  


- Enumeration PC Element
```Terminal
IOXIDResolver ---> https://github.com/mubix/IOXIDResolver) 
```

- Extra 
	- In some case, you might found some IPV6 address. Most of the IPV6 address are not setup for firewall since people mostly focus on IPV4