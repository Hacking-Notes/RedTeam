--- ---
<h3>what is ping?</h3>
Ping is a network diagnostic tool that sends packets of data to a target host and measures the time it takes for the packets to be transmitted and received. The tool is used to test the connectivity of a network and to determine the round-trip time (RTT) for data packets to travel between two devices.

---
<h3>Common use and commands:</h3>
The most common use of ping is to test whether a host is reachable over the network. To use ping, simply open a command prompt or terminal and type "ping" followed by the target host's IP address or domain name. The tool will send a series of ICMP packets to the target host and report the results, including the RTT and any packet loss.

Ping
```Terminal
ping -c X IP
```

- -c                            ---> Number of ping sent

TTL response from the ping might give some infromation about the operating system
- Linux                       ---> 64 or less
- Windows                 ---> 128
- Cisco                       ---> 128 - 256