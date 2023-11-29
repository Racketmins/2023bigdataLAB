import numpy as np
import operator

try:
    f = open("datinTestSet.txt")
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
    normDataSet = dataSet - np.tile(minValue, (m,1))
    normDataSet = normDataSet / np.tile(ranges, (m,1))
    return normDataSet

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    distances = sqDiffMat.sum(axis = 1)
    sortedDistance = distances.argsort()
    classCount = {}
    for i in range(k):
        dLabel = labels[sortedDistance[i]]
        clasCount[dLabel] = classCount.get(dLabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0] 


group, labels = createDataSet(datas)
group = autoNorm(group)
answer = input()
answer = answer.split()
print(classify0(answer, group, labels, 10))        
