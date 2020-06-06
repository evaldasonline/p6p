
def Komanda(eile,k):
    print('Vykdome: ', eile)
    fja=eile[0]
    p = []
    p.append(eile[0])
    eile=eile[1:].strip()
    t=eile.find(' ')

    while t >= 0:
        p.append(eile[:t])
        eile=eile[t:].strip()
        t=eile.find(' ')

    p.append(eile)

    x=len(p)

    if fja in ('012345'):
        print ('koja:', fja)
        if x<3:
            p.append("-1")
            p.append("-1")

        elif x<4:
            p.append("-1")

        k[int(fja)].move(p[1], p[2], p[3])


    elif fja == "q":
        print ('Pabaiga')
    else:
        print ('bbz')
