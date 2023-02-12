--- ---

<h2>Attachment</h2>

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