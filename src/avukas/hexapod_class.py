from __future__ import division
import time
import Adafruit_PCA9685

class kojos:
    
    def __init__ (self, pw, chan1, chan2, chan3):
        self.srv = [pw, chan1, chan2, chan3]
        

    def get_pos(self):
        return self.pos
        
    def pradzia(self, kr, c):
        self.kryptis = kr
        self.cent = c
        self.pos = c
        print self.cent
        
        


#############################################################    
#############################################################    
#############################################################    
class hexapodas:
    # klase
    
    def __init__(self, vardas, pwm1add=0x40, pwm2add=0x41):
        self.name = vardas
        self.pwm = []
        
        self.pwm.append(Adafruit_PCA9685.PCA9685(address=0x40, busnum=1))
        #self.pwm.append(Adafruit_PCA9685.PCA9685(address=0x41, busnum=1))
        self.pwm[0].set_pwm_freq(60)

        self.K = []
        # 0 - desine priekis
        self.K.append(kojos(0, 0, 8, 15))
        self.K[0].pradzia([-1, -1, 0], [375,375,375])

        # 1 - dsine centras
        self.K.append(kojos(0, 1, 9, 15))
        self.K[1].pradzia([-1, -1, 0], [390,375,375])

        # 2 - dsine galas
        self.K.append(kojos(0, 2, 10, 15))
        self.K[2].pradzia([-1, -1, 0], [375,375,375])

        # 3 - kaire galas
        self.K.append(kojos(0, 4, 12, 15))
        self.K[3].pradzia([1, 1, 0], [350,375,375])

        # 4 - kaire centras
        self.K.append(kojos(0, 5, 13, 15))
        self.K[4].pradzia([1, 1, 0], [375,375,375])

        # 5 - kaire priekis
        self.K.append(kojos(0, 6, 14, 15))
        self.K[5].pradzia([1, 1, 0], [390,375,375])
        
        
        
###############################################################################        
    def info(self):
        print (self.name + " modulis pakrautas")
        
        
###############################################################################
    def move_to_pos(self, kk, ps):
        fake=-1
        
        if ps[0] <> fake:
            self.pwm[self.K[kk].srv[0]].set_pwm(self.K[kk].srv[1], 0, ps[0])
            self.K[kk].pos[1] = ps[0]
        
        if ps[1] <> fake:
            self.pwm[self.K[kk].srv[0]].set_pwm(self.K[kk].srv[2], 0, ps[1])
            self.K[kk].pos[1] = ps[1]
        
        if ps[2] <> fake:
            self.pwm[self.K[kk].srv[0]].set_pwm(self.K[kk].srv[3], 0, ps[2])
            self.K[kk].pos[2] = ps[2]
        

    def move_step_val(self, zingsnis):
        # judina pagal absoliutinius skaicius - pwm
        print zingsnis
        for i in range(6):
            self.move_to_pos(i, zingsnis[i])
            
            
'''
    def move_step(self. zingsnis):
        #su perskaiciavimu
        # i - kojos
        for i in range (6):
            #j - sanarys
            for j in range (3):
                r = self.K[i].kryptis[j]
                z[i][j] = 375 + zingsnis[i][j] * r

'''
