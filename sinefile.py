import time
import math

freq=100
f= open("sinwav.txt","w+")
#fila= open("sinwav2.txt","w+")

def swave(ti):
	return math.sin(2*3.14*freq*ti)
t=0
while 1:
	
	f.write(str(t)+" "+str(swave(t)))
	t=t+1
	time.sleep(1)