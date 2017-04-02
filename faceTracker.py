import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_alt.xml')

ret, roi_color = cap.read()

while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.2, 3)
	for (x,y,w,h) in faces:
		frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		#roi_color = frame[y:y+h, x:x+w]

	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
