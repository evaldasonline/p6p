
def Komanda(eile, avukas):
    
    eile=eile.upper()
    p=list(map(str,eile.split()))
    fja=p[0]
    x=len(p)
    

    if fja == 'LEG':
        if x < 5:
            print 'nepakanka argumentu'
        else:
            if p[1] not in '012345':
                print 'bloga koja'
            else:
                print 'koja:', p[1], 
                print 'a = ', p[2],
                print 'b = ', p[3],
                print 'c = ', p[4]
                avukas.move_to_pos(int(p[1]), [int(p[2]), int(p[3]), int(p[4]) ] )
                print avukas.K[int(p[1])].get_pos()
        

    elif fja == "POS":
        k5=avukas.K[5].get_pos()
        k5.reverse()
        k4=avukas.K[4].get_pos()
        k4.reverse()
        k3=avukas.K[3].get_pos()
        k3.reverse()
        print '^^^^^^^^^ priekis ^^^^^^^^^'
        print 'isore <<   kunas   >> isore'
        print k5, '  ', avukas.K[0].get_pos()
        print k4, '  ', avukas.K[1].get_pos()
        print k3, '  ', avukas.K[2].get_pos()
        print 'simetriskas atvaizdavimas'

    elif fja == "000":
        for i in range(6):
            avukas.move_to_pos(i, avukas.K[i].cent )

    elif fja == "LGS":
        for i in range(6):
            avukas.move_to_pos(i, [ int(p[1]), int(p[2]), int(p[3]) ] )

    elif fja == 'EMO':
        do_emote( avukas, p[1] )

    else:
        print ('bbz')
    
    
    return p

######################################33
####  bandymas judinti letai
def do_emote( avukas, e ):
    e=e.upper()
    if e == 'AGRO':
        avukas.move_step_val( [ avukas.K[0].cent, avukas.K[1].cent, avukas.K[2].cent, \
                                avukas.K[3].cent, avukas.K[4].cent, avukas.K[5].cent ] )
        
        avukas.move_step_val( [ [600, 200, 375], [500, 500, 375], avukas.K[2].cent, \
                                avukas.K[3].cent, [200, 200, 375], [150, 550, 375] ] )
        
        
        
        
        
