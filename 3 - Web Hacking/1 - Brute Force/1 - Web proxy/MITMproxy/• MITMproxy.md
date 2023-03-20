--- ---
<h2>What is MiTHproxy</h2>

MITMproxy is a free and open-source command-line tool that allows users to intercept, inspect, and modify HTTP and HTTPS traffic in real-time. It can be used as a proxy server or a transparent proxy, and it runs on most operating systems, including Windows, macOS, and Linux.

This tool is mostly used to intercept request made on phone

---
<h2>Steps</h2>
```
# Computer
sudo ./mitmweb --set web_port=8082             ---> Web interface for proxing phone

# Phone
Go to the setting/wifi and change the IP for the ip of the computer and the port set from the mitmweb
Dowload a certificate from mitm.it and set the certificate to be trusted has root (settings)
```
