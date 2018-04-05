import time
import math
import threading
import sqlite3

x=0
y=0
freq=100

def opendb():
	conn = sqlite3.connect('swave.db')
	c=conn.cursor()
	c.execute('delete from swave;')
	conn.commit()
	conn.close()

def swave(ti):
	return math.sin(2*3.14*freq*ti)

def sinwave():
	global x
	global y
	while 1:
		y=swave(x)
		x+=1
		time.sleep(1)
		#print str(x)+" "+str(y)

def writedb():
	i=1
	opendb()
	while 1:
		conn = sqlite3.connect('swave.db')
	        c=conn.cursor()
		print "Inserting "+str(i)+" "+str(x)+" "+str(y)
		data=[i,x,y]
		c.execute('INSERT INTO SWAVE VALUES (?,?,?);',data)
		conn.commit()
		conn.close()
		time.sleep(10)
		i+=1
		

def readdb():
	while 1:
		c.execute('SELECT * FROM SWAVE;')
		print c.fetchall()
		time.sleep(8*5)

if __name__ == "__main__":

	t1 = threading.Thread(target=sinwave)
	t2= threading.Thread(target=writedb)
	print "Starting sinewave"
	t1.start()
	print "Uploading to DB"
	t2.start()
	entr=raw_input("ENTER OP")
	if entr=='q':
		exit()


#writedb()
