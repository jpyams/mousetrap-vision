print "starting"
import numpy as np
import cv2
import glob
import time

C = 1
gamma = 0.5
classes = 3
def selectArray(clas):
	rv = [0]*classes
	rv[clas] = 1
	return rv


print "begin reading"
for i in range(classes):
	f = np.loadtxt('store/test2/' + str(i+1) + '.txt', dtype='float32')
	if 'train' in locals():
		label = label + [i]*f.shape[0]
		train = np.vstack([train, f])
	else:
		label = [i]*f.shape[0]
		train = f
#	f = open('store/' + str(i+1) + '.txt')
#	line = f.readline()
#	while line:
#		train.append(map(float, line.split()))
#		label.append(i+1)
#	f.close()

print "finish reading"

response = np.array(label)
trainData = np.array(train)

rand = int(time.time())
np.random.seed(rand)
np.random.shuffle(response)
np.random.seed(rand)
np.random.shuffle(trainData)


print trainData.shape
print response.shape

innodes = 1764

#machine = cv2.ml.ANN_MLP_create()
#machine.setLayerSizes(np.array([innodes, innodes*2, classes]))	#Defines the sizes of the node layers
#machine.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM)	#Not sure what this is
#machine.setTrainMethod(cv2.ml.ANN_MLP_RPROP)	#I presume this tells it to do reverse propogation

print "ready for setup"

print "Training"
#machine.train(trainData, cv2.ml.ROW_SAMPLE, response)

machine = cv2.ml.SVM_create()
machine.setType(cv2.ml.SVM_C_SVC)
machine.setKernel(cv2.ml.SVM_RBF)
machine.setC(C)
machine.setGamma(gamma)
machine.train(trainData, cv2.ml.ROW_SAMPLE, response)


machine.save("svm3.yml")
