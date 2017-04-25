import numpy as np
import time
import cv2
import thread

finished = False

def capture():
	global finished
	cap = cv2.VideoCapture(0)
	i = 0
	while not finished:
		ret, frame = cap.read()
		worked = cv2.imwrite('test3/hand/img%05d.png' % i, frame)
		print worked
		i += 1
		time.sleep(0.1)
	cap.release()

thread.start_new_thread(capture, ())

while not finished:
	res = raw_input('q for quit')
	if res == 'q':
		finished = True
