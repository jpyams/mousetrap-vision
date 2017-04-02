import numpy as np
import cv2
import glob

train = [[]]
label = []

classes = 5
for i in range(classes):
	f = open('class' + (i+1) + '/data.txt')
	line = f.readline()
	while line:
		train.append(map(float, line.split()))
		label.append(i+1)
	f.close()


innodes = 5

machine = cv2.ml.ANN_MPL_create()
machine.setLayerSizes(np.array([innodes, innodes/2, classes]))	#Defines the sizes of the node layers
machine.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM)	#Not sure what this is
machine.setTrainMethod(cv2.ml.ANN_MLP_RPROP)	#I presume this tells it to do reverse propogation


response = np.array(label)
trainData = np.array(train)
machine.train(trainData, cv2.ml.ROW_SAMPLE, response)

fs = cv2.FileStorage("machine.yml", cv2.FileStorage_WRITE)
machine.write(fs, "machine")
