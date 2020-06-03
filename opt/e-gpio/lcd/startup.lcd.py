# /opt/e-gpio/lcd/startup.lcd.py
### BEGIN INIT INFO
# Provides:          sample.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO
 
import i2c_lcd2004_driver as lcd_driver
from time import *
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

#########################################################33
lcd = lcd_driver.lcd(0,1)
lcd.backlight(0)
lcd.lcd_clear()
sleep(10)


lcd.backlight(1)
sleep(.2)
x=0

while (x<15):
    x+=1
    ip=get_ip()
    
    iplo=ip.find("127.0.0.1")>-1
    ipno=ip.find("169.254")>-1
    
    if (iplo or ipno):
        for i in range(2,18):
            lcd.lcd_display_string(" *",2,i)
            sleep (.3)
        for i in range(18,2,-1):
            lcd.lcd_display_string("* ",2,i)
            sleep(.3)
    else:
        x=99
    
lcd.lcd_display_string(ip, 1,1)
lcd.lcd_display_string(" " * 18,2,1)            

sleep(3)
lcd.backlight(0)
lcd.lcd_display_string("OK",1,17)            

