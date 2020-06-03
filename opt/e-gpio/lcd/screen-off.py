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
lcd = lcd_driver.lcd(0,1)
lcd.backlight(0)
lcd.lcd_clear()
