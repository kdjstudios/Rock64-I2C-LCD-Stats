#!/usr/bin/env python
import httplib, time, os, sys, json
#import pcd8544.lcd as lcd
import lcddriver
lcd = lcddriver.lcd()

# class Process dedicated to process data get from Client
# and send information to LCD and console
class Process:
  # Process constructor
  def __init__(self):
    # Initialize LCD
    lcd.lcd_clear()

  def run(self, jsonString):
    # Parse data as json
    data = json.loads( jsonString )
    # Try to get data from json or return default value
    try:
      rpi_temperature = data['soctemp']
    except:
      rpi_temperature="--.---"

    try:
      rpi_cpu_frequency = data['cpu_frequency']
    except:
      rpi_cpu_frequency = "--"
      
    try:
      rpi_uptime = data['uptime']
    except:
      rpi_uptime = "--:--:--"
      
    try:
      rpi_load1 = data['load1']
    except:
      rpi_load1 = "-.--"
      
    try:
      rpi_load5 = data['load5']
    except:
      rpi_load5 = "-.--"
      
    try:
      rpi_load15 = data['load15']
    except:
      rpi_load15 = "-.--"
      
    try:
      rpi_upgrade = data['upgrade']
    except:
      rpi_upgrade = "--"
      
    try:
      rpi_sdcard_root_used = data['sdcard_root_used']
    except:
      rpi_sdcard_root_used = "----.--"
      
    try:
      rpi_swap_used = data['swap_used']
    except:
      rpi_swap_used = "----.--"
      
    try:
      rpi_memory_available = data['memory_available']
    except:
      rpi_memory_available = "-.--"
      
    try:
      rpi_localtime = data['localtime']
    except:
      rpi_localtime = "-.--"
      
    try:
      rpi_memory_free = data['memory_free']
    except:
      rpi_memory_free = "-.--"
      
    try:
      rpi_cpu_count = data['cpu_count']
    except:
      rpi_cpu_count = "-.--"

    # Construct string to be displayed on screens
    temperature = "TEMP: %s C" % (float(rpi_temperature)/1000)
    cpu_frequency = "CPU: %s GHz" % rpi_cpu_frequency
    uptime = "UPTIME: %s Hours" % (int((float(rpi_uptime)/60)/60))
    load1 = "1 MIN: %s" % rpi_load1
    load5 = "5 MIN: %s" % rpi_load5
    load15 = "15 MIN: %s" % rpi_load15
    upgrade = "%s" % rpi_upgrade
    sdcard_root_used = "SD USED: %s MB" % (int(rpi_sdcard_root_used))
    swap_used = "SWAP USED: %s MB" % rpi_swap_used
    memory_free = "MEM FREE: %s MB" % (int(rpi_memory_free))
    memory_available = "MEM AVAIL: %s MB" % (int(rpi_memory_available))
    cpu_count = "CPU COUNT: %s" % rpi_cpu_count
    localtime = "TIME: %s" % rpi_localtime
    
    # Uncomment below lines to print in console
    #os.system("clear")
    #print " RPi-Monitor "
    #print
    #print uptime
    #print temperature    
    #print cpu_frequency
    #print cpu_count
    #print load1
    #print load5
    #print load15
    #print upgrade    
    #print sdcard_root_used
    #print swap_used    
    #print memory_available
    #print memory_free
    #print localtime
    #print
    
    # Print out on LCD
    lcd.lcd_clear()
    lcd.lcd_display_string(temperature,1)
    lcd.lcd_display_string(uptime,2)
    time.sleep(10)
    lcd.lcd_clear()
    lcd.lcd_display_string(cpu_count,1)
    lcd.lcd_display_string(cpu_frequency,2)
    time.sleep(10)
    lcd.lcd_clear()
    lcd.lcd_display_string(load1,1)
    lcd.lcd_display_string(load5,2)
    time.sleep(10)
    lcd.lcd_clear()
    lcd.lcd_display_string(load15,1)
    lcd.lcd_display_string(upgrade,2)
    time.sleep(10)
    lcd.lcd_clear()
    lcd.lcd_display_string(sdcard_root_used,1)
    lcd.lcd_display_string(swap_used,2)
    time.sleep(10)
    lcd.lcd_clear()
    lcd.lcd_display_string(memory_available,1)
    lcd.lcd_display_string(memory_free,2)
    time.sleep(10)

# Class client design to work as web client and get information
# from RPi-Monitor embedded web server
class Client:
  # Client constructor
  def __init__(self):
    # Create a Process object
    self.process = Process()

  def run(self):
    # Infinite loop
    while True:
      try:
        # Initiate a connection to RPi-Monitor embedded server
        connection = httplib.HTTPConnection("192.168.1.61", 8888)
        # Get the file dynamic.json
        connection.request("GET","/dynamic.json")
        # Get the server response
        response = connection.getresponse()
        # Get the file static.json
        static_connection.request("GET","/static.json")
        # Get the server response
        static_response = static_connection.getresponse()
        if ( response.status == 200) && (static_response.status == 200 ):
          # If response is OK, read data
          data = response.read()
          static_data = static_response.read()
          # Run process object on extracted data
          self.process.run(data)
          # self.process.run(data,static_data)
          
          # Close the connection to RPi-Monitor embedded server
          connection.close()
        else
          #Report an Error
          lcd.lcd_display_string("Connection Error",1)
          print "Connection Error"
          print
      finally:
        # Clear the LCD
        lcd.lcd_clear()

# Main function
def main():
  try:
    # Create a Client object
    client = Client()
    # Run it
    client.run()
  except KeyboardInterrupt:
    # if Ctrl+C has been pressed
    lcd.lcd_clear()
    # exit from the program
    sys.exit(0)

# Execute main if the script is directly called
if __name__ == "__main__":
    main()
