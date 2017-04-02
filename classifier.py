import numpy as np
import cv2
import glob

files = glob.glob("left/capture/img*.png")
face_cascade = cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_alt.xml')

classes = {}
for clasDirs in glob.iglob("class*"):
	classes[clasDirs] = len(glob.glob(clasDirs + '/*.png'))


def directives(img):
	font = cv2.FONT_HERSHEY_SIMPLEX
	img = cv2.putText(img, '1', (img.shape[1]/2, img.shape[0]/2), font, 1, (255,255,255), 2, cv2.LINE_AA)
	img = cv2.putText(img, '2', (0, img.shape[0]/2), font, 1, (255,255,255), 2, cv2.LINE_AA)
	img = cv2.putText(img, '3', (img.shape[1]-20, img.shape[0]/2), font, 1, (255,255,255), 2, cv2.LINE_AA)
	img = cv2.putText(img, '4', (img.shape[1]/2, 20), font, 1, (255,255,255), 2, cv2.LINE_AA)
	img = cv2.putText(img, '5', (img.shape[1]/2, img.shape[0]), font, 1, (255,255,255), 2, cv2.LINE_AA)
	return img


for imgfile in files:
	img = cv2.imread(imgfile)
	faces = face_cascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.3, 5)
	if len(faces) > 0:
		(x,y,w,h) = faces[0]
		img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
		img = directives(img)
		#roi_color = img[y:y+h, x:x+w]
		cv2.imshow('Classifying', img)	#roi_color)
		clas = cv2.waitKey(0)
		if clas & 0xFF == ord(' '):
			continue
		clasDir = 'class' + str(chr(clas & 0xFF))
		cv2.imwrite(clasDir + "/" + str(chr(clas & 0xFF)) + "_%05d.png" % classes[clasDir], img)
		classes[clasDir] += 1

cv2.destroyAllWindows()
