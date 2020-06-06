import os
import avukas
from avukas.Komanda import Komanda as Kom

avukas.kojos.info()

k = []

k.append(avukas.kojos.koja(0,0,1,2))
k.append(avukas.kojos.koja(1,3,4,5))
k.append(avukas.kojos.koja(2,6,7,8))
k.append(avukas.kojos.koja(3,9,10,11))
k.append(avukas.kojos.koja(4,12,13,14))
k.append(avukas.kojos.koja(5,15,16,17))
for x in range(6):
    k[x].move(x*10,x*11,x*12)

kartoti = 1
while kartoti:
    s = input("Komanda? ")
    if s == "q":
        kartoti=0
    if len(s) > 0:
        Kom(s,k)
    avukas.kojos.show_all(k)
