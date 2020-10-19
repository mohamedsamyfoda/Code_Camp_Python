import cv2
import numpy as np

'''
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

img = cv2.imread("D:\Master\Camp_Python\Python_Project/star.jpg")
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgstak = stackImages(0.5,([img,img,img],[img,grayimg,img]))
#imgHor = np.hstack((img,img))
#imgVer = np.vstack((img,img))

#cv2.imshow("text",imgHor)
#cv2.imshow("textver",imgVer)

cv2.imshow("imagestack",imgstak)
cv2.waitKey(0)

'''
def empty():
    pass


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


path = "D:\Master\Camp_Python\Python_Project/carImg.jpg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",91,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
while True:
    img = cv2.imread(path)
    imgHCV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    H_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    H_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    S_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    S_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    V_min = cv2.getTrackbarPos("Val Min","TrackBars")
    V_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(H_min,H_max,S_min,S_max,V_min,V_max)
    lower = np.array([H_min,S_min,V_min])
    upper = np.array([H_max,S_max,V_max])
    mask = cv2.inRange(imgHCV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)


    #cv2.imshow("testimg",img)
    #cv2.imshow("HCV",imgHCV)
    #cv2.imshow("impose",impose)



    imgstack = stackImages(0.6,([img,imgHCV],[mask,imgResult]))
    cv2.imshow("allimg",imgstack)
    cv2.waitKey(1)