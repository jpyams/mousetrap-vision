import numpy as np
import cv2

machine = cv2.ml.SVM_load("svmExpanded.yml")
res = ['center', 'left', 'right']

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
	if len(faces) == 0:
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		continue
	(x,y,w,h) = faces[0]
	if len(faces) > 1:
		largestS = w*h
		largest = 0
		for i in range(1,len(faces)):
			(x,y,w,h) = faces[i]
			if w*h > largestS:
				largest = i
		(x,y,w,h) = faces[largest]
	face = gray[y:y+h, x:x+w]
	face = cv2.resize(face, (64,64))
	descriptors = hd.compute(face)
	#descriptors.reshape((descriptors.size,1))
	#print descriptors
	descriptors = np.rot90(descriptors, 1)
	#print descriptors[0]
	#print descriptors.shape
	retval = machine.predict(descriptors)
#		if retval[1][0] != 1:
		#print retval
	lastval = int(retval[1][0])
	frame = cv2.putText(frame, res[lastval], (frame.shape[1]/2, frame.shape[0]/2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	#roi_color = frame[y:y+h, x:x+w]

	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

