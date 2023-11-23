import numpy as np
import operator

try:
    f = open("data.txt")
    data = f.read()
    datas = []
    for line in data:
        datas.append(line) 
except FileNotFoundError:
    print("Not file")
finally:
    f.close()

def createDataSet(datas):
    group = []
    labels = []
    for i in datas:
        group.append(datas[i][0], datas[i][1], datas[i][2])
        labels.append(datas[i][3])
    group = np.array(group)
    labels = np.array(labels)
    return group, labels

def autoNorm(dataSet):
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    ranges = maxValue - minValue
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    norm
def classify0(inX, group, labels, k):

