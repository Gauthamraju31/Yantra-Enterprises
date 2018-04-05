import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

img1 = np.zeros((512,512,3), np.uint8)
img2 = np.zeros((512,512,3), np.uint8)
img3 = np.zeros((512,512,3), np.uint8)

x=255
y=255

cv2.circle(img1,(x-50,y), 63, (0,0,255), -1)
cv2.circle(img2,(x+50,y), 63, (0,255,0), -1)
cv2.circle(img3,(x,y+70), 63, (255,0,0), -1)

img=cv2.add(img1,img2)
img=cv2.add(img,img3)

cv2.imshow('img',img)

while 1:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
