import cv2
import os

dataset='datasets'
sub_data='myself'

path=os.path.join(dataset,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)

(width,height)=(130,100)
face_cascade = cv2.CascadeClassifier('C:/Users/janan/Pictures/Screenshots/AI masterclass/datasets/myself/haarcascade_frontalface_default.xml')
webcame=cv2.VideoCapture(0)

count=1
while count<31:
    print(count)
    _,im=webcame.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x,y,w,h),(255,0,0),2)
        face=gray[y:y+h,x:x+w]
        face_resize=cv2.resize(face,(width,height))
        cv2.imwrite("%s %s.png"%png (path,count),face_resize)

    count+=1
    cv2.imshow('OpenCV',im)
    key=cv2.waitKey(10)
    if key ==27:
        break
print("dataset obtained successfully")
webcame.release()
cv2.destroyAllWindows()


