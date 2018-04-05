import math
import cv2
import numpy as np

x=[]
y=[]

img = np.zeros((512,512,3), np.uint8)

for i in range(100):
    x.append(i)
    y.append(i)

for i in x:
    for j in y:
        r=math.sqrt(math.pow(i-50,2)+math.pow(j-50,2))
        #if r<25:
        #    img[i,j]=0
        #if r>25:
        #    img[i,j]=0
        if r>=24 and r<= 26:
            img[i,j]=255
cv2.imshow('circle',img)

while 1:
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
       break

cv2.destroyAllWindows()


