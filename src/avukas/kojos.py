import os
class koja:

    def __init__(self, eilnr, petys_gpio, alkune_gpio, riesas_gpio):
        self.nr=eilnr
        self.pos=[0,0,0]
        #servo_init

    def get_pos(self):
        return self.pos

    def move(self,a=90,b=90,c=90):
        self.oldpos=self.pos
        if a=="-1": a=self.pos[0]
        if b=="-1": b=self.pos[1]
        if c=="-1": c=self.pos[2]

        self.pos=[a,b,c]


def info():
    print ("kojos modulis pakrautas")

def show_all(k):
    #os.system('cls' if os.name == 'nt' else 'clear')
    for x in range(3):
        print(k[x].get_pos(), k[5-x].get_pos())
