With the HackRF One it is posible to send a fake GPS signal to other devices.

You need the following parts:  
– HackRF One (can also be a Chinese clone)  
– External TCXO (as GPS needs high precision)  
– Antenna (best is a dedicated GPS antenna)  
– GNU Radio and HackRF tools

> sudo apt install gnuradio libhackrf0 hackrf libhackrf-dev

Check if you see 0x01 with (means TXCO is installed):

> hackrf_debug --si5351c -n 0 -r

1. Download the GPS-SDR-SIM software

> mkdir GPS_SDR_SIM

> cd GPS_SDR_SIM

> git clone https://github.com/osqzss/gps-sdr-sim.git

2. Compile it

> make

3. Get the current satellite positions from NASA  
_*New: Updated URL, 03.03.2021* (Thanks for the information Ye-Sheng Kuo)_

Create an account on https://urs.earthdata.nasa.gov/
Make a file called .netrc with the following content:

>    machine urs.earthdata.nasa.gov login actedlinux password Asdfghjkl007
   
3.  Change the file permission with

> sudo chmod 004 .netrc

4. Generate the signal file with the static position (coordinates) you want to send

> ./gps-sdr-sim -b 8 -e YOUR_BRDC_FILE_HERE -l 40.812800,-60.005900,100

5. Send the signal

> sudo hackrf_transfer -t gpssim.bin -f 1575420000 -s 2600000 -a 1 -x 0