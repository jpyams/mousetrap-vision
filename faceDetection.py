import numpy as np
import cv2

for i in range(39):
	inpu = "capture2/img%05d.png" % i

	face_cascade = cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
	img = cv2.imread(inpu)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

	cv2.imshow('img',img)
	cv2.waitKey(1000)
	cv2.destroyAllWindows()
