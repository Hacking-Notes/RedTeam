**OBDII**

Get access to the internal network of the car

Steps

- Connect the OBDII (Wifi or Bluetooth)
   - If using Bluetooth: `sudo /etc/init.d/bluetooth start`
- Connect to the OBDII
- Find the name of the network ()
- Install (`sudo apt install can-utils -y`)
- `cansniffer -c vcan0` ---> (NAME_OF_NETWORK)
- capture the commands
   - `candump -c -l vcan0`
- Analyse the commands
   -  `more NAME_OF_THE_FILE`
   - `more NAME_OF_THE_FILE | grep COMMAND_NUMBER`
- Replay the command
   - `cansend vcan0 COMMAND_NUMBER#OTHER_NUMBERS`
     
If using bluetooth (close): `sudo /etc/init.d/bluetooth stop`
