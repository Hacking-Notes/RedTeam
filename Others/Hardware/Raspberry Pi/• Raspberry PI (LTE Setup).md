
- minicom -D /dev/ttyUSB2
	- ATE1
	- AT+CGDCONT=1,"IP","super"
	- AT+COPS?      ----> Output something like = +COPS: 0,0,"Vodafone UK Twilio",7
	- close the window terminal
- sudo pon
- sudo ifconfig wlan0 down