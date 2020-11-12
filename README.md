# Rock64-I2C-LCD-Stats
This is a project to create a python script that will work with infomration from RPi-Monitor to display the real time stats to a I2C LCD screen connected to a Rock64. This is currently being used with a 16x2 I2C LCD.

## Stats and Metrics that can be displayed
The following list is of all the stats that RPi-Monitor collects for the Rock64. These stats are part of the python script that can be configured to display then accordingly. 

* Coming Soon
* Coming Soon

## Setup Instructions
Follow the below sections to learn how to setup a I2C 16x2 LCD display on the Rock64 to display system stats. 

### Hardware
* Rock64 (This includes the power supply, SD card, and OS)
* I2C LCD
* [Optional] Case

### Prerequiests
* Rock64 with an OS installed and booted and updated.
* Installed packages ()
  * RPi-Monitor

### Install
Follow the below instruction to clone this repo and install
 
> cd /opt/
>
> git clone https://github.com/kdjstudios/Rock64-I2C-LCD-Stats
>
> cd Rock64-I2C-LCD-Stats

### Start
Follow the below instruction to start the script
 
> cd /opt/Rock64-I2C-LCD-Stats
>
> sudo python stats.py

### Setup Auto Run at Boot
Follow the below instructions to setup a Cronjob to auto start this at boot. Note we will have it on a delay start since we need to wait until RPi-Monitor to also start running too.

# Issues
Check out the wiki [] to see about troubleshooting. 

