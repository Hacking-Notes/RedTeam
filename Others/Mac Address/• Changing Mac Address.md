--- ---


Install Mac Changer tool
```
sudo apt-get install macchanger
```

Find the interface (The interface you will use to spoof the Mac address)
```
ip addr
```

![[word-image-199 1.webp]]

Setup a random Mac Address
```
macchanger -r <interface-name>
```

Setting up a Specific MAC ID
```
macchanger --mac=XX:XX:XX:XX:XX:XX <interface-name>
```

Restore Mac Address
```
macchanger -p <interface-name>
```