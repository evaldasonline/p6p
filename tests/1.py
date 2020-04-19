print ("labas")
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
time.sleep(3)
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

