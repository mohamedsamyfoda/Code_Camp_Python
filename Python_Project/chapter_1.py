import cv2
import numpy as np

'''
width,height = 250,350
img = cv2.imread("D:\Master\Camp_Python\Python_Project/snap.jpg")
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[height,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("test",img)
cv2.imshow("imgoutput",imgoutput)
cv2.waitKey()

'''
'''
img = np.zeros((512,512,3),np.uint8)

#img[:]= 255, 0, 0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,225,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255,0),3)
cv2.circle(img,(450,50),40,(225,225,2),3)
cv2.putText(img,"YaQoP", (300,200),cv2.FONT_HERSHEY_PLAIN,1,(599,0,0),1)


cv2.imshow("img",img)
cv2.waitKey(0)
'''
'''
img_car = cv2.imread("D:\Master\Camp_Python\Python_Project/car.png")

print(img_car.shape)

resize = cv2.resize(img_car,(200,400))
print(resize.shape)
imgCropped = img_car[0:200,0: 300]

cv2.imshow("imshow",img_car)
cv2.imshow("resize",resize)
cv2.imshow("imgCropped",imgCropped)

cv2.waitKey(0)
'''
'''
img = cv2.imread("D:\Master\Camp_Python\Python_Project/pic.png")

kernel = np.ones((5,5),np.uint8)
pic = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
pic1 = cv2.GaussianBlur(pic,(7,7),0)
pic2 = cv2.Canny(img,150,200)
pic3 = cv2.dilate(pic2,kernel,iterations=1)
pic4 = cv2.erode(pic3,kernel,iterations=1)

#cv2.imshow("test",pic)
#cv2.imshow("testpic1",pic1)
cv2.imshow("testpic2",pic2)
cv2.imshow("testpic3",pic3)
cv2.imshow("testpic4",pic4)


cv2.waitKey(0)

'''
'''
img = cv2.imread("D:\Master\Camp_Python\Python_Project/pic.png")
pic = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
pic1 = cv2.GaussianBlur(pic,(7,7),0)
pic2 = cv2.Canny(img,150,200)

cv2.imshow("test",pic)
cv2.imshow("testpic1",pic1)
cv2.imshow("testpic2",pic2)
cv2.imshow("testpic3",pic3)

cv2.waitKey(0)
'''
'''
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
'''
'''
cap = cv2.VideoCapture("D:\Master\Camp_Python\Python_Project/test_video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
'''
'''
img = cv2.imread("D:\Master\Camp_Python\Python_Project/pic.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)
cv2.waitKey(0)
'''
'''
img = cv2.imread("D:\Master\Camp_Python\Python_Project/pic.jpg")
cv2.imshow("test",img)
cv2.waitKey(0)
'''