--- ---

<h2>Commands</h2>

Top Commands
```
evil-winrm -h

evil-winrm -u USER -p PASSWORD -i IP_ADDRESS_HERE
```

- Possible to use metasploit console and meterpreter to create a session

---

<h2>What is Evil Winrm</h2>

Evil Winrm basicly give you a shell to the target machine once you have valid credential

WinRM (Windows Remote Management) is the Microsoft implementation of WS-Management Protocol. A standard SOAP based protocol that allows hardware and operating systems from different vendors to interoperate. Microsoft included it in their Operating Systems in order to make life easier to system administrators.

This program can be used on any Microsoft Windows Servers with this feature enabled (usually at port 5985), of course only if you have credentials and permissions to use it. So we can say that it could be used in a post-exploitation hacking/pentesting phase. The purpose of this program is to provide nice and easy-to-use features for hacking. It can be used with legitimate purposes by system administrators as well but the most of its features are focused on hacking/pentesting stuff.

It is based mainly in the WinRM Ruby library which changed its way to work since its version 2.0. Now instead of using WinRM protocol, it is using PSRP (Powershell Remoting Protocol) for initializing runspace pools as well as creating and processing pipelines.