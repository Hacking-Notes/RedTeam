--- ---

Email analysis is the process of extracting the email header information to expose the email file details. The email header contains the technical details of the email like sender, recipient, path, return address and attachments. Usually, these details are enough to determine if there is something suspicious/abnormal in the email and decide on further actions on the email, like filtering/quarantining or delivering. This process can be done manually and with the help of tools.

Email Structure
![[Pasted image 20221207181229.png]]

Element from Header Section
![[Pasted image 20221207181319.png]]

---

<h2>Emails & EML Format</h2>

Depending on the carriers, different steps will apply

Gmail          ---> https://www.youtube.com/watch?v=DsiMTlkyV-M
Outlook       ---> https://www.youtube.com/watch?v=kOqpYqwm94c
...


Open the .EML format in sublime text and  select the following option
![[Pasted image 20221207181926.png]]

---

<h2>Emails Analysis Tools</h2>

emlAnalyser
```
emlAnalyzer -i Urgent\:.eml --header --html -u --text --extract-all
```

**-i**                     ---> File to analyse (-i /path-to-file/filename)
**--header**        ---> Show header
**-u**                    ---> Show URLs
**--text**              ---> Show cleartext data
**--extract-all**   ---> Extract all attachments

Response
```
 ==============
 ||  Header  ||
 ==============
X-Pm-Content-Encryption.....end-to-end
X-Pm-Origin.................internal
Subject.....................Urgent: Blue section is down. Switch to the load share plan!
From........................[REDACTED]
Date........................[REDACTED]
Mime-Version................[REDACTED]
Content-Type................[REDACTED]
To..........................[REDACTED]
X-Attached..................[REDACTED]
Message-Id..................[REDACTED]
X-Pm-Spamscore..............[REDACTED]
Received....................[REDACTED]
X-Original-To...............[REDACTED]
Return-Path.................[REDACTED]
Delivered-To................[REDACTED]
 =========================
 ||  URLs in HTML part  ||
 =========================
[+] No URLs found in the html
 =================
 ||  Plaintext  ||
 =================
[+] Email contains no plaintext
 ============
 ||  HTML  ||
 ============
Dear Elves,.......
 =============================
 ||  Attachment Extracting  ||
 =============================
[+] Attachment [1] "Division_of_........
```


Additionally, you can use some Open Source Intelligence (OSINT) tools to check email reputation and enrich the findings. Visit the given site below and do a reputation check on the sender address and the address found in the return path.

-   `https://emailrep.io/`

---

<h2>Attachments</h2>

You can compute the value of the file to conduct file-based reputation checks and further your analysis. As shown below, you can use the sha256sum tool/utility to calculate the file's hash value. 

**Note:** Remember to navigate to the file's location before attempting to calculate the file's hash value.  

```shell-session
user@ubuntu$ sha256sum file.something
0827bb9a.... 
```

![VirusTotal](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/c2c773b4d53b467950632c80649553f7.png)

Once you get the sum of the file, you can go for further analysis using the **VirusTotal**.  

-   Tool: `https://www.virustotal.com/gui/home/upload`

Now, visit the tool website and use the `SEARCH` option to conduct hash-based file reputation analysis. After receiving the results, you will have multiple sections to discover more about the hash and associated file. Sections are shown below.

![Virustotal sections](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/d71085a61113f7bf87b31dcd0e40570c.png)

-   Search the hash value
-   Click on the `BEHAVIOR` tab.
-   Analyse the details.

After that, continue on reputation check on **InQuest** to enrich the gathered data.

-   **Tool:** `https://labs.inquest.net/`

Now visit the tool website and use the `INDICATOR LOOKUP` option to conduct hash-based analysis.

-   Search the hash value
-   Click on the SHA256 hash value highlighted with yellow to view the detailed report.
-   Analyse the file details.

![InQuest](https://tryhackme-images.s3.amazonaws.com/user-uploads/6131132af49360005df01ae3/room-content/f7a0ebef6bbe5b127fe4787a5caf9811.png)