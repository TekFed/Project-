import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread(r'C:\Users\dell\Pictures\Camera Roll\WIN_20220509_22_02_32_Pro.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x + w, y + h), (225, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitkey()

cv2.imwrite("Face detected.jpg", img)