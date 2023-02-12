--- ---

<h2>Top Commands</h2>

MACchanger
```
#Change MAC address
-   sudo ifconfig wlan2 down
-   sudo macchanger -r wlan2
-   sudo ifconfig wlan2 up

#Reset Mac address
-   sudo ifconfig wlan2 down
-   sudo macchanger -p wlan2
-   sudo ifconfig wlan2 up
```