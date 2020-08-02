import time


def Komanda(eile, avukas):
    
    eile=eile.upper()
    p=list(map(str,eile.split()))
    fja=p[0]
    x=len(p)
    
## -------------------------------------
    if fja == 'LEG' or fja == 'L':
    # LEG -> kojos nr -> klubas -> kelys -> peda
    # pakeicia nurodytos kojos sanariu kampa absoliutiniu dydziu 
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
        
## -------------------------------------
    elif fja == "POS":
    # POS
    # paraso koju padeti
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

## -------------------------------------
    elif fja == "000":
    # sucentruoja viskas kojas i p[radine padeti
        for i in range(6):
            avukas.move_to_pos(i, avukas.K[i].cent )

## -------------------------------------
    elif fja == "375":
    # sucentruoja viskas kojas i p[radine padeti
        for i in range(6):
            avukas.move_to_pos(i, [375,375,375] )

## -------------------------------------
    elif fja == "LGS":
        for i in range(6):
            avukas.move_to_pos(i, [ int(p[1]), int(p[2]), int(p[3]) ] )

## -------------------------------------
    elif fja == 'EMO':
    # EMO emocija
    # issaukia emocijos pastatyma        
        do_emote( avukas, p[1] )

## -------------------------------------
    else:
        print ('bbz')
    
    
    return p

######################################33
####  EMO  padeties pastatymas
def do_emote( avukas, e ):
    e=e.upper()
    #--------------------------------------------------------------------------------------
    if e == 'AGRO':
        avukas.move_step_val( [ avukas.K[0].cent, avukas.K[1].cent, avukas.K[2].cent, \
                                avukas.K[3].cent, avukas.K[4].cent, avukas.K[5].cent ] )
        
        avukas.move_step_val( [ [600, 200, 375], [500, 500, 375], avukas.K[2].cent, \
                                avukas.K[3].cent, [200, 200, 375], [150, 550, 375] ] )
    
    elif e == 'ST1':
        avukas.move_step_val( [ [375, 200, 150], [375, 200, 150], [375, 200, 150], \
                                [375, 500, 600], [375, 500, 600], [375, 500, 600] ] )
                                
        avukas.move_step_val( [ [375, 300, 150], [375, 300, 150], [375, 300, 150], \
                                [375, 400, 600], [375, 400, 600], [375, 400, 600] ] )
        
    #--------------------------------------------------------------------------------------
    elif e == 'WAVE':
        for i in range(6):
            avukas.move_to_pos(i, avukas.K[i].cent )
        for i in range (10):
            avukas.move_spec(k01=50)
            avukas.move_spec(k11=50)
            avukas.move_spec(k21=50)
            avukas.move_spec(k31=50)
            avukas.move_spec(k41=50)
            avukas.move_spec(k51=50)

            avukas.move_spec(k01=-50)
            avukas.move_spec(k11=-50)
            avukas.move_spec(k21=-50)
            avukas.move_spec(k31=-50)
            avukas.move_spec(k41=-50)
            avukas.move_spec(k51=-50)
            
            time.sleep(1)

    #--------------------------------------------------------------------------------------
        
    elif e == 'FWD':
        for i in range(6):
            avukas.move_to_pos(i, avukas.K[i].cent )
            
        #pirma pora pasikelia
        avukas.move_spec(k01=100, k21=100, k41=100)
        for i in range (10):
            
            #pirma permeta pirmyn
            avukas.move_spec(k00=-100, k20=-100, k40=-100)
            #pirma pora nusileidzia
            avukas.move_spec(k01=-100, k21=-100, k41=-100)
            #antra pora pasikelia, kad pirma galetu judinti kuna
            avukas.move_spec(k11=100, k31=100, k51=100)
            #pirma pora juda atgal - stumia kuna pirmyn
            avukas.move_spec(k00=100, k20=100, k40=100)

            #antra pora permeta pirmyn
            avukas.move_spec(k10=-100, k30=-100, k50=-100)
            #antra pora nsileidzia
            avukas.move_spec(k11=-100, k31=-100, k51=-100)
            #pirma pora pasikelia, kad antra galetu judinti kuna
            avukas.move_spec(k01=100, k21=100, k41=100)
            #antra pora juda atgal, stumdama kuna pirmyn
            avukas.move_spec(k10=100, k30=100, k50=100)

            #time.sleep(1)
        #pirma pora nusileidzia
        avukas.move_spec(k01=-100, k21=-100, k41=-100)
        
    #--------------------------------------------------------------------------------------
        
    else:
        print ('bbz')
        
###############################333
        
        
        
        
