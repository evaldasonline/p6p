import avukas

k=[]

avukas.kojos.c_koja.info()

k.append(avukas.kojos.koja(1))
k[0].move(1,3,5)

k.append(avukas.kojos.koja(2))

print (k[0].nr)
print (k[1].nr)

print (k[0].get_pos())
print (k[1].pos)
