print "starting"
import numpy as np
import cv2
import glob

classes = 2
def selectArray(clas):
	rv = [0]*classes
	rv[clas] = 1
	return rv


print "begin reading"
for i in range(classes):
<<<<<<< HEAD
	f = np.loadtxt('store/' + str(i+2) + '.txt', dtype='float32')
	if 'train' in locals():
		label = np.concatenate((label, np.array([selectArray(i) for j in range(f.shape[0])], dtype='float32')))
		train = np.vstack([train, f])
	else:
		label = np.array([selectArray(i) for j in range(f.shape[0])], dtype='float32')
		train = f
#	f = open('store/' + str(i+1) + '.txt')
#	line = f.readline()
#	while line:
#		train.append(map(float, line.split()))
#		label.append(i+1)
#	f.close()

print "finish reading"

print label.shape
print train.shape

rand = np.random.randint(1)
np.random.seed(rand)
np.random.shuffle(label)
np.random.seed(rand)
np.random.shuffle(train)


print label.shape
print train.shape

innodes = 1764

machine = cv2.ml.ANN_MLP_create()
machine.setLayerSizes(np.array([innodes, innodes/2, classes]))	#Defines the sizes of the node layers
machine.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM)	#Not sure what this is
machine.setTrainMethod(cv2.ml.ANN_MLP_RPROP)	#I presume this tells it to do reverse propogation

print "ready for setup"

response = np.array(label)
trainData = np.array(train)
print "Training"
machine.train(trainData, cv2.ml.ROW_SAMPLE, response)

machine.save("machineh11.yml")
