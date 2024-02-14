import cv2

file_path = "C:/Users/janan/Downloads/haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(file_path)

if haar_cascade.empty():
    print("Error: Unable to load the cascade classifier XML file.")
    exit()

cam=cv2.VideoCapture(0)

while True:
    _,img=cam.read()

    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face=haar_cascade.detectMultiScale(grayImg,scaleFactor=1.3, minNeighbors=4)

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)
    if key ==27:
        break

cam.release()
cv2.destroyAllwindows()

#import os

#file_path = "haarcascade_frontalface_default.xml"

#if os.path.exists(file_path):
 #   print("File exists at the specified path.")
#else:
 #   print("File does not exist at the specified path.")


