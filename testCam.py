import cv2 as cv
import numpy as np

sizeH = 600
SizeW = 600
center = int(sizeH / 2)
dimensionDrop = 20
leftframe = 295
rightframe = 305

cam = cv.VideoCapture(1)

while True:
    ret, frame = cam.read()
    frame = cv.resize(frame, dsize = (sizeH,SizeW))

    cv.line(frame,(center,sizeH),(center,0),(0,255,0),1)
    cv.rectangle(frame,(rightframe,sizeH) , (leftframe, 0), (0,0,255),1)
    cv.rectangle(frame,(0,270) , (600, 330), (15,255,255),2)
    cv.line(frame,(0,300),(600,300),(0,255,0),1)

    cv.imshow("test", frame)
    if cv.waitKey(2) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()