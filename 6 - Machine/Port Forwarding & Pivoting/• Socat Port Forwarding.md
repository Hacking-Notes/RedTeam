--- ---

<h2>General</h2>

Port forwarding with socat is a technique that allows the user to forward network traffic from one network to another using the socat tool. Socat is a command-line utility that enables the user to establish network connections and perform various types of network operations, including port forwarding.

---

<h2>Commands</h2>

The basic syntax to perform port forwarding using socat is much simpler. If we wanted to open port 3389 on a host and forward any connection we receive there to port 3389 on host 1.1.1.1, you would have the following command:

Run on the Intermediary Machine
```shell-session
socat TCP4-LISTEN:3389,fork TCP4:1.1.1.1:3389
```

We might need to open the firewall
```shell-session
netsh advfirewall firewall add rule name="Open Port 3389" dir=in action=allow protocol=TCP localport=3389
```

The `fork` option allows socat to fork a new process for each connection received, making it possible to handle multiple connections without closing. If you don't include it, socat will close when the first connection made is finished.