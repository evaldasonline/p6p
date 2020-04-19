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

ip="127.0.0.1"
while ip=="127.0.0.1":
    ip=get_ip()
    lcd.lcd_display_string(ip, 1,1)

if (ip.find("169.254") > 0) :
    sleep(15)
    ip=get_ip()
    lcd.lcd_clear()
    lcd.lcd_display_string(ip, 1,1)
    if (ip.find("169.254") > 0) :
        sleep(15)
        lcd.lcd_clear()
        ip=get_ip()
        lcd.lcd_display_string(ip, 1,1)
        if (ip.find("169.254") > 0) :
            lcd.lcd_display_string("DHCP not found", 2,1)
    

sleep(3)
lcd.backlight(0)
lcd.lcd_clear()
lcd.lcd_display_string(ip, 1,1)

sleep(.01)
