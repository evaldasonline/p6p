from __future__ import division
import time
import Adafruit_PCA9685

class kojos:
    
    def __init__ (self, pw, chan1, chan2, chan3):
        self.srv = [pw, chan1, chan2, chan3]
        #self.srv.append(pw)
        #self.srv.append(chan1)
        #self.srv.append(chan2)
        #self.srv.append(chan3)
        
        self.pos = [90, 90, 90]
        
        
    def get_pos(self):
        return self.pos
        

        


#############################################################    
class hexapodas:
    # klase
    
    def __init__(self, vardas, pwm1add=0x40, pwm2add=0x41):
        self.name = vardas
        self.pwm = []
        self.koja = []
        self.pwm.append(Adafruit_PCA9685.PCA9685(address=0x40, busnum=1))
        #self.pwm.append(Adafruit_PCA9685.PCA9685(address=0x41, busnum=1))
        self.pwm[0].set_pwm_freq(60)


    def info(self):
        print (self.name + " modulis pakrautas")

    def init_koja(self, pw, chan1, chan2, chan3):
        self.koja.append(kojos(pw, chan1, chan2, chan3))
        
        kojaid = len(self.koja) - 1
        
        print ("koja: " + str(kojaid) + " | plokste: " + str(pw) + " | portai: " + str(chan1) + " " + str(chan2) + " " + str(chan3))
        

    #def move_to_pos( self, a=self.pos[0], b=self.pos[1], c=self.pos[2] ):
    def move_to_pos(self, kk, a,b,c):
        servo_min=150
        servo_max=600
       
        self.pwm[self.koja[kk].srv[0]].set_pwm(self.koja[kk].srv[1], 0, a)
        self.pwm[self.koja[kk].srv[0]].set_pwm(self.koja[kk].srv[2], 0, b)
        self.pwm[self.koja[kk].srv[0]].set_pwm(self.koja[kk].srv[3], 0, c)
        


