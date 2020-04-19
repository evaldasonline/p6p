class koja:
    kiekKoju=0
    
    def __init__(self, eilnr):
        koja.kiekKoju += 1
        self.nr=eilnr
        self.pos=[0,0,0]
        
    def get_pos(self):
        return self.pos
    
    def move(self,a=0,b=0,c=0):
        self.pos=[a,b,c]
        

def info():
    print ("c_koja modulis pakrautas")
    