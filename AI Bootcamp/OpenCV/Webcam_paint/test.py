import cv2
import numpy as np


def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = frame[y,x,0]
        colorsG = frame[y,x,1]
        colorsR = frame[y,x,2]
        colors = frame[y,x]
        print(frame[y,x])
        # HSVcolors = cv2.cvtColor(colors, cv2.COLOR_BGR2HSV)
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        # print("HSV Format: ",HSVcolors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)


cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

capture = cv2.VideoCapture(0)



while(True):

    ret, frame = capture.read()

    HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    cv2.imshow('mouseRGB', HSV)

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()