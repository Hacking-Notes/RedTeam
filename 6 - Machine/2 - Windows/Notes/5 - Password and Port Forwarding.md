--- ---

<h2>Searching for password</h2>

- In Registry
```
# VNC reg query "HKCU\Software\ORL\WinVNC3\Password"
# Windows autologin reg query
"HKLM\SOFTWARE\Microsoft\Windows
NT\Currentversion\Winlogon"
# SNMP Paramters reg query
"HKLM\SYSTEM\Current\ControlSet\Services\SNMP"
# Putty reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"
# Search for password in registry reg query HKLM /f password /t
REG_SZ /s reg query HKCU /f password /t REG_SZ /s
```

---

<h2>Port Forwarding</h2>

1. Use netstat -ano to see which ports are open
![[image.BY7GW1.png]]

2. Download the latest version of plink.exe for the correct
architecture
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

3. Host it on attack machine, download with certutil on victim
machine to a writeable folder (/temp/ or the user folder)

4. gedit /etc/ssh/sshd_config and set PermitRootLogin to Yes
![[image.1R0DW1.png]]

5. Restart and start SSH service
![[image.LN8OW1.png]]

6. Use the plink syntax for port forwarding
![[image.5B6BW1.png]]

7. Should bring us to "root" on our box - then we know it was
successful
![[image.ZN1NW1.png]]

8. Use winexe to get access to the machine again as
administrator
- Hit enter a few times until you get a shell9. 
![[image.D7YRW1.png]]

9. You are now root/system!
![[image.GJOFW1.png]]