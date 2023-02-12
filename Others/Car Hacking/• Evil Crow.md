**Signal**

![[Screenshot_2022-08-18_21-23-22.png]]


- First step is to analyse the signal (Frequency and modulation)

- Second, setup the parameters in the Arduino Roll file
	- Frequency
	- Jam Frequency
	- Jam Power
	- ...




**➡️ MORE INFORMATION**


**SD Card Setup**

- Add the HTML file to the micro SD card


**Device Setup (Roll)**

- Install esptool: sudo apt install esptool
- Install pyserial: sudo pip install pyserial
- Download and Install the Arduino IDE: [https://www.arduino.cc/en/main/software](https://www.arduino.cc/en/main/software)
- Download Evil Crow RF V2 repository: git clone [https://github.com/joelsernamoreno/EvilCrowRF-V2.git](https://github.com/joelsernamoreno/EvilCrowRF-V2.git)
- Download the ESPAsyncWebServer library in the Arduino library directory: git clone [https://github.com/me-no-dev/ESPAsyncWebServer.git](https://github.com/me-no-dev/ESPAsyncWebServer.git)
- Download the AsyncElegantOTA library in the Arduino library directory: git clone [https://github.com/ayushsharma82/AsyncElegantOTA.git](https://github.com/ayushsharma82/AsyncElegantOTA.git)
- Download the ESP32-targz library in the Arduino library directory: git clone [https://github.com/tobozo/ESP32-targz.git](https://github.com/tobozo/ESP32-targz.git)
- Download the AsyncTCP library in the Arduino library directory: git clone [https://github.com/me-no-dev/AsyncTCP.git](https://github.com/me-no-dev/AsyncTCP.git)
- Edit AsyncTCP/src/AsyncTCP.h and change the following:
-   #define CONFIG_ASYNC_TCP_USE_WDT 1 to #define CONFIG_ASYNC_TCP_USE_WDT 0
- Open Arduino IDE
- Go to File - Preferences. Locate the field "Additional Board Manager URLs:" Add "[https://dl.espressif.com/dl/package_esp32_index.json](https://dl.espressif.com/dl/package_esp32_index.json)" without quotes. Click "Ok"
- Select Tools - Board - Boards Manager. Search for "esp32". Install "esp32 by Espressif system version 1.0.6". Click "Close".
- Open the EvilCrowRF-V2/firmware/v1.3.1/EvilCrow-RFv2/EvilCrow-RFv2.ino sketch
- Select Tools:
    -   Board - "ESP32 Dev Module".
    -   Flash Size - "4MB (32Mb)".
    -   CPU Frequency - "80MHz (WiFi/BT)".
    -   Flash Frequency - "40MHz"
    -   Flash Mode - "DIO"
- Upload the code to the Evil Crow RF V2 device
- Copy the EvilCrowRF-V2/firmware/v1.3.1/SD/HTML folder to a MicroSD card.
- Copy the EvilCrowRF-V2/firmware/v1.3.1/SD/URH folder to a MicroSD card.  (OPTIONAL)


**WIFI Setting (192.168.4.1)** - (DEPEND ON THE ROLL VERSION, ROLL V.3 DOES NOT SUPPORT)

- Connec to the RollJam WIFI
- Go to 192.168.4.1
- Change the setting to:
   - Set the module to (Module2)
   - Set the Frequency (Depending on the annalyse from URH)
   - Set the RxBW (Default 58)
   - Set the Deviation (Default 8)
   - Set the Data rate (Default 5)


>
>**More Information**
>
>
[![Webpanel](https://github.com/joelsernamoreno/EvilCrowRF-V2/raw/main/images/webpanel.png)](https://github.com/joelsernamoreno/EvilCrowRF-V2/blob/main/images/webpanel.png)
>
**RX Config Example**
>
>-   Module: (1 for first CC1101 module, 2 for second CC1101 module)
>-   Modulation: (example ASK/OOK)
>-   Frequency: (example 433.92)
>-   RxBW bandwidth: (example 58)
>-   Deviation: (example 0)
>-   Data rate: (example 5)
>
[![RX](https://github.com/joelsernamoreno/EvilCrowRF-V2/raw/main/images/rx.png)](https://github.com/joelsernamoreno/EvilCrowRF-V2/blob/main/images/rx.png)
>
>**RX Log Example**
>
[![RXLog](https://github.com/joelsernamoreno/EvilCrowRF-V2/raw/main/images/rx-log.png)](https://github.com/joelsernamoreno/EvilCrowRF-V2/blob/main/images/rx-log.png)
>
>**RAW TX Config Example**
>
>-   Module: (1 for first CC1101 module, 2 for second CC1101 module)
>-   Modulation: (example ASK/OOK)
>-   Transmissions: (number transmissions)
>-   Frequency: (example 433.92)
>-   RAW Data: (raw data or raw data corrected displayed in RX Log)
>-   Deviation: (example 0)
>
[![TXRAW](https://github.com/joelsernamoreno/EvilCrowRF-V2/raw/main/images/txraw.png)](https://github.com/joelsernamoreno/EvilCrowRF-V2/blob/main/images/txraw.png)
>
>**Binary TX Config Example**
>
>-   Module: (1 for first CC1101 module, 2 for second CC1101 module)
>-   Modulation: (example ASK/OOK)
>-   Transmissions: (number transmissions)
>-   Frequency: (example 433.92)
>-   Binary Data: (binary data displayed in RX Log)
>-   Sample Pulse: (samples/symbol displayed in RX Log)
>-   Deviation: (example 0)
>
[![TXBINARY](https://github.com/joelsernamoreno/EvilCrowRF-V2/raw/main/images/txbinary.png)](https://github.com/joelsernamoreno/EvilCrowRF-V2/blob/main/images/txbinary.png)
>
**Pushbuttons Configuration**
>
>-   Button: (1 for first pushbutton, 2 for second pushbutton)
>-   Modulation: (example ASK/OOK)
>-   Transmissions: (number transmissions)
>-   Frequency: (example 433.92)
>-   RAW Data: (raw data or raw data corrected displayed in RX Log)
>-   Deviation: (example 0)
>
[![TXBUTTON](https://github.com/joelsernamoreno/EvilCrowRF-V2/raw/main/images/pushbutton.png)