from __future__ import division
import time
import Adafruit_PCA9685

class kojos:
    
#    int velinimas=0
    
    def __init__ (self, pw, chan1, chan2, chan3):
        self.srv = [pw, chan1, chan2, chan3]
        

    def get_pos(self):
        return self.pos
        
    def pradzia(self, kr, c):
        ## c = [klubas, kelys,peda]
        ## kryptis = [klubas, kelys,peda]  - teigiamas ar neigiama
        self.kryptis = kr
        self.cent = c
        self.pos = c
        print self.pos

        
        
        
        


#############################################################    
#############################################################    
#############################################################    
class hexapodas:
    # klase
    
    def __init__(self, vardas, pwm1add=0x40, pwm2add=0x41):
        self.name = vardas
        self.pwm = []
        
        self.pwm.append(Adafruit_PCA9685.PCA9685(address=0x40, busnum=1))
        self.pwm.append(Adafruit_PCA9685.PCA9685(address=0x41, busnum=1))
        self.pwm[0].set_pwm_freq(60)
        self.pwm[1].set_pwm_freq(60)

        self.K = []
        # 0 - desine priekis
        self.K.append(kojos(0, 10, 4, 0))
        self.K[0].pradzia([-1, -1, 0], [375,375,375])

        # 1 - dsine centras
        self.K.append(kojos(0, 8, 7, 6))
        self.K[1].pradzia([-1, -1, 0], [390,375,375])

        # 2 - dsine galas
        self.K.append(kojos(0, 5, 9, 15))
        self.K[2].pradzia([-1, -1, 0], [375,375,375])

        # 3 - kaire galas
        self.K.append(kojos(1, 5, 6, 0))
        self.K[3].pradzia([1, 1, 0], [380,395,375])

        # 4 - kaire centras
        self.K.append(kojos(1, 8, 7, 9))
        self.K[4].pradzia([1, 1, 0], [375,380,375])

        # 5 - kaire priekis
        self.K.append(kojos(1, 11, 10, 15))
        self.K[5].pradzia([1, 1, 0], [390,375,375])
        
        
        
###############################################################################        
    def info(self):
        print (self.name + " modulis pakrautas")
        
        
###############################################################################
    def move_to_pos(self, kk, ps):
        # tokia be rysio funkcija... cia pajudinam absoliutinius dydzius. o reikia pereiti i kojos objekta
        fake=-1  
        
        if ps[0] <> fake:
            self.pwm[self.K[kk].srv[0]].set_pwm(self.K[kk].srv[1], 0, ps[0])
            self.K[kk].pos[0] = ps[0]
        
        if ps[1] <> fake:
            self.pwm[self.K[kk].srv[0]].set_pwm(self.K[kk].srv[2], 0, ps[1])
            self.K[kk].pos[1] = ps[1]
        
        if ps[2] <> fake:
            self.pwm[self.K[kk].srv[0]].set_pwm(self.K[kk].srv[3], 0, ps[2])
            self.K[kk].pos[2] = ps[2]

########################################################
    def apply_K_pos1(self,kuri):
        self.pwm[self.K[kuri].srv[0]].set_pwm(self.K[kuri].srv[1], 0, self.K[kuri].pos[0])
        time.sleep(0.005)
        self.pwm[self.K[kuri].srv[0]].set_pwm(self.K[kuri].srv[2], 0, self.K[kuri].pos[1])
        time.sleep(0.005)
        self.pwm[self.K[kuri].srv[0]].set_pwm(self.K[kuri].srv[3], 0, self.K[kuri].pos[2])
        time.sleep(0.005)
        
############################################################################33
# judina pagal absoliutinius skaicius - pwm
    def move_step_val(self, zingsnis):
        print zingsnis
        for i in range(6):
            self.move_to_pos(i, zingsnis[i])
            
###################################################################################33
# judina visas kojas vienu metu plastishkai
    def move_form_current(self, zingsnis):
        # zingsnis = [ [], [], [], [], [], [] ]
        # i - kojos
        for i in range (6):
            #j - sanarys
            for j in range (3):
                r = self.K[i].kryptis[j]
                # zabs[i][j] = abs(zingsnis[i],[j])
                self.K[i].pos[j] = self.K[i].pos[j] + zingsnis[i][j] * r
            self.apply_K_pos1(i)

###################################################################################33
# judina pasirinktus sanarius pagal kintamuosius
    def move_spec(self, k00=0, k01=0, k02=0,   k10=0, k11=0, k12=0,   k20=0, k21=0, k22=0,  \
    k30=0, k31=0, k32=0,   k40=0, k41=0, k42=0,   k50=0, k51=0, k52=0):
            # perkeliame tik tuos, kuriuos pasirinkome
            self.move_form_current ( [ [k00, k01, k02], [k10, k11, k12], [k20, k21, k22], \
            [k30, k31, k32], [k40, k41, k42], [k50, k51, k52] ] )
