'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

# img = cv2.imread("Haar_Cascade/image_1.jpg", cv2.IMREAD_GRAYSCALE)
# img = cv2.resize(img, (400,400))
# cv2.imshow("Theimg", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
# Closes all the frames
cv2.destroyAllWindows()

img = cv2.imread(filename='photo.png')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.line(img, (0,0), (150,150), color=(255,0,0), thickness=10)
# cv2.rectangle(img, (0,0), (150, 150), color=(0.255,0), thickness=12)
# cv2.circle(img, (75,75), 25, color=(0,0,255), thickness=20)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, "OpenCV", (170,170), font, 1, (75,75,75), 5)
#ret, mask = cv2.threshold(img, 50, 150, cv2.THRESH_BINARY_INV)
img2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('frame', img)
cv2.imshow('frame1', img1)
cv2.imshow('frame2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('Haar_Cascade\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Haar_Cascade\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (250,0,0), 2)
        roi_gray = gray[y:y+h, x:x+y]
        roi_color = img[y:y+h, x:x+y]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
        
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()