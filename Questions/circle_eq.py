import numpy as np
import cv2
import math

def draw_circle(r,m,n):
    #m=255
    #n=255
    #r= 40
    img = np.zeros((512,512,3), np.uint8)

    x=[]
    y=[]

    for i in range(m-r,m+r):
        x.append(i)
        if i>m:
            y.append(n+int(math.sqrt(math.pow(float(r),2)-math.pow(float(i-m),2))))
        else:
            y.append(n+int(math.sqrt(math.pow(float(r),2)-math.pow(float(m-i),2))))

    for i in range(m-r,m+r):
        x.append(i)
        if i>m:
            y.append(n-int(math.sqrt(math.pow(float(r),2)-math.pow(float(m-i),2))))
        else:
            y.append(n-int(math.sqrt(math.pow(float(r),2)-math.pow(float(m-i),2))))

    for i in range(n-r,n+r):
        y.append(i)
        if i>n:
            x.append(m+int(math.sqrt(math.pow(float(r),2)-math.pow(float(i-n),2))))
        else:
            x.append(m+int(math.sqrt(math.pow(float(r),2)-math.pow(float(n-i),2))))

    for i in range(n-r,n+r):
        y.append(i)
        if i>n:
            x.append(m-int(math.sqrt(math.pow(float(r),2)-math.pow(float(n-i),2))))
        else:
            x.append(m-int(math.sqrt(math.pow(float(r),2)-math.pow(float(n-i),2))))

    print x
    print y

    for i in range(len(x)):
        img[x[i],y[i]]=[0,0,255]

    return img

img1=draw_circle(60,295,255)
img2=draw_circle(60,215,255)
img3=draw_circle(60,255,335)

#cv2.imshow('circle',img1)
img4=cv2.add(img1,img2)
cv2.imshow('circle',cv2.add(img3,img4))

while 1:
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
       break

cv2.destroyAllWindows()

