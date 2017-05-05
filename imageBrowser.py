import numpy as np
import cv2
import glob

directory = "../expandedData/rightplus"

imgFiles = glob.glob('data/' + directory + '/*.png')
imgFiles.sort()

cache = []
cache.append(cv2.imread(imgFiles[-4]))
cache.append(cv2.imread(imgFiles[-3]))
cache.append(cv2.imread(imgFiles[-2]))
cache.append(cv2.imread(imgFiles[-1]))
cache.append(cv2.imread(imgFiles[0]))
cache.append(cv2.imread(imgFiles[1]))
cache.append(cv2.imread(imgFiles[2]))
cache.append(cv2.imread(imgFiles[3]))
cache.append(cv2.imread(imgFiles[4]))

pivotFile = 0
index = 4
delta = 0

cv2.imshow('frame', cache[index])

while(True):
	clas = cv2.waitKey(0)
	if clas == ord(' '):
		index+=1
		delta+=1
	elif clas == ord('b'):
		index-=1
		delta-=1
	elif clas == ord('q'):
		break
	index %= len(cache)
	print imgFiles[(pivotFile+delta) % len(imgFiles)]
	cv2.imshow('frame',cache[index])
	if abs(delta) == 3:
		pivotFile = (pivotFile + delta) % len(imgFiles)
		for i in range(3):
			if delta == 3:
				try:
					cache[(index+i+1)%len(cache)] = cv2.imread(imgFiles[(pivotFile+i+1)%len(imgFiles)])
				except:
					print 'error, go for 8 to smooth'
					del imgFiles[(pivotFile+i+1)%len(imgFiles)]
					cache[(index+i+1)%len(cache)] = cv2.imread(imgFiles[0])
			if delta == -3:
				try:
					cache[(index-i-1)%len(cache)] = cv2.imread(imgFiles[(pivotFile-i-1)%len(imgFiles)])
				except:
					print 'error, go for 8 to smooth'
					del imgFiles[(pivotFile-i-1)%len(imgFiles)]
					cache[(index-i-1)%len(cache)] = cv2.imread(imgFiles[0])
		delta = 0

cv2.destroyAllWindows()
