import numpy as np
import cv2
import os
import time as t

imdir='camera/'
flg=0
for r,d,Fs in os.walk('camera/'):
    p=os.path.basename(r).lower()
    if(p==n):
        flg=1

if(flg==0):
    os.mkdir(imdir)

cap = cv2.VideoCapture(0)
while(True):

    ret, frame = cap.read()


    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

tm=int(t.time())
dir_=imdir+str(tm)+".jpg"
cv2.imwrite(dir_, frame)
cap.release()
cv2.destroyAllWindows()
