import numpy as np
import cv2

machine = cv2.ml.ANN_MLP_load("machine2h.yml")

#face_cascade = cv2.CascadeClassifier('../opencv/data/haarcascades/haarcascade_frontalface_alt.xml')

classes = 2
total = [0]*classes
correct = [0]*classes
falsep = [0]*classes
falsen = [0]*classes

for i in range(classes):
	f = np.loadtxt('store/' + str(i+1) + '.txt', dtype='float32')
	for descriptors in f:
		descriptors = np.reshape(descriptors, (-1, 1))
		descriptors = np.rot90(descriptors, 3)
		retval = machine.predict(descriptors)
		total[i]+=1
		if retval[0] == i:
			correct[i]+=1
		else:
			falsen[i] += 1
			falsep[int(retval[0])]+=1

def printFormat(title, ary, divise):
	rv = title + "\t"
	for i in range(len(ary)):
		if type(divise) is int:
			rv += '\t' + str(ary[i])
		else:
			rv += '\t%.2f' % (100.0*ary[i]/divise[i])
	return rv


print printFormat('class', range(1,classes+1), 1)
print printFormat('total', total, 1)
print printFormat('correct', correct, 1)
print printFormat('  %', correct, total)
print printFormat('falsen', falsen, 1)
print printFormat('  %', falsen, total)
print printFormat('falsep', falsep, 1)
