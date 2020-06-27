#  pagrindinis failas, startuojantis kaip servisas ir aptarnaujantis uzklausas 
# apie koju valdyma ir sensorius
#
#

#from __future__ import division
#import time
#import Adafruit_PCA9685
from hexapod_class import *
from hexapod_command import *


avukas = hexapodas("Avukas")
avukas.info()


############################################################################3
#esminis ciklas
while 1:
	
	kmd=raw_input('Komanda? ')
	if kmd == '':
		kmd='xxx'
		
	eile = Komanda(kmd,avukas)
	
	#avukas.K[int(eile[1])].get_pos()
	
	#avukas.move_to_pos(k,a,b,c)
	#print( avukas.K[k].get_pos() ) 

