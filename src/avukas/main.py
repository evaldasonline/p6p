from __future__ import division
import time
import Adafruit_PCA9685
from hexapod_class import *


avukas = hexapodas("Avukas")
avukas.info()


print( avukas.koja[0].get_pos() ) 


while 1:
	print('a:')
	a=input()
	
	print('b:')
	b=input()
	
	print('c:')
	c=input()
	
	avukas.move_to_pos(0,a,b,c)

