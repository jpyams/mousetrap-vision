import numpy as np
import cv2
import screeninfo
import os

filepath = '../../data/johnpeter'
if not os.path.exists(filepath):
	os.makedirs(filepath)
	os.makedirs(filepath+'/left')
	os.makedirs(filepath+'/right')
	os.makedirs(filepath+'/center')

screen = screeninfo.get_monitors()[0]

cap = cv2.VideoCapture('../../dot/dot%04d.jpg')
cam = cv2.VideoCapture(0)
settings = ['Blank face', 'Smile!', 'Pout', 'Open your mouth', 'Stick out your tongue', 'Hold your right eye open']
#limits = [(1,125),(135,280),(300,335),(350,605),(625,655),(675,800)]
center = range(1,126)+range(290,345)+range(612,662)
left = range(130,208)+range(250,281)+range(675,796)
right = range(350,425)+range(451,606)
cv2.namedWindow('frame',cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

for setting in settings:
	blank_image = np.zeros((screen.height,screen.width,3), np.uint8)
	cv2.imshow('frame',cv2.putText(blank_image, setting, (screen.width/2,screen.height/2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA))
	cv2.waitKey(1000)
	i = 1
	if setting == settings[5]:
		break
	ret, frame = cap.read()
	while(ret):
		ret, camframe = cam.read()
		frame = cv2.resize(frame, (screen.width, screen.height))

		if i in center:
			cv2.imwrite(filepath + '/center/' + setting + '%3d.jpg' % i,camframe)
		elif i in left:
			cv2.imwrite(filepath + '/left/' + setting + '%3d.jpg' % i,camframe)
		elif i in right:
			cv2.imwrite(filepath + '/right/' + setting + '%3d.jpg' % i,camframe)

		i += 1
		
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		ret, frame = cap.read()
	cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

cap.release()
cam.release()
cap = cv2.VideoCapture('../../dot1/dot%04d.jpg')
ret, frame = cap.read()
while(ret):
	ret, camframe = cam.read()
	frame = cv2.resize(frame, (screen.width, screen.height))
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	ret, frame = cap.read()


cap.release()
cv2.destroyAllWindows()
