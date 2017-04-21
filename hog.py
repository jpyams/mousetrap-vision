import numpy as np
import cv2
import glob

face_cascade = cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_alt.xml')

hd = cv2.HOGDescriptor((64,64), (16,16), (8,8), (8,8), 9)

imgFiles = glob.glob("class3expanded/*.png")
imgFiles.sort()

store = open("store/3.txt", "w")
errors = 0

for imgFile in imgFiles:
	img = cv2.imread(imgFile)
	faces = face_cascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.3, 5)
	if len(faces) == 0:
		print "error: " + imgFile + ": no face found"
		errors += 1
		continue
	(x,y,w,h) = faces[0]
	rect = img[y:y+h, x:x+w]
	rect = cv2.resize(rect, (64,64))
	rect = cv2.cvtColor(rect, cv2.COLOR_RGB2GRAY)
	cv2.imshow('HOGging', rect)
	cv2.waitKey(5)
	descriptors = hd.compute(rect)
	store.write(" ".join([str(i[0]) for i in descriptors]) + "\n")

store.close()

print "%d failed out of %d" % (errors, len(imgFiles))
