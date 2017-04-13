import numpy as np
import cv2

machine = cv2.ml.ANN_MLP_load("machineh.yml")

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
hd = cv2.HOGDescriptor((64,64), (16,16), (8,8), (8,8), 9)

ret, roi_color = cap.read()

lastval = 0

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.2, 3)
	for (x,y,w,h) in faces:
		face = gray[y:y+h, x:x+w]
		face = cv2.resize(face, (64,64))
		descriptors = hd.compute(face)
		descriptors = np.rot90(descriptors, 3)
		retval = machine.predict(descriptors)
		#if retval[0] == 3:
		print retval
		lastval = int(retval[0])
		frame = cv2.putText(frame, str(lastval), (frame.shape[1]/2, frame.shape[0]/2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
		frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		#roi_color = frame[y:y+h, x:x+w]

	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

