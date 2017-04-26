import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
cam = cv2.VideoCapture(0)
settings = ['Blank face', 'Smile!', 'Pout', 'Open your mouth', 'Stick out your tongue', 'Hold your right eye open']

for setting in settings:
	while(cap.isOpened()):
		ret, frame = cap.read()
		ret, camframe = cam.read()

		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

cap.release()
cam.release()
cv2.destroyAllWindows()
