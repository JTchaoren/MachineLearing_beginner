#-*-coding:utf-8 -*-
import csv
import random
import math
import  operator

#加载数据 split(分割trainingSet和testSet的界限 )
def loadDataset(filename,split,trainingSet=[],testSet=[]):
    with open(filename,"rb") as csvfile:
        line = csv.reader(csvfile)
        dataset = list(line)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random()< split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

#距离计算
def euclideanDistance(instance1,instance2,length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]),2)
    return math.sqrt(distance)

#返回最近K个邻居
def getNeighbors(trainingSet,testInstance,k):
    distances = []
    length = len(testInstance) -1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance,trainingSet[x],length)#计算训练集中的每一个实例到测试实例的距离
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))#排序
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

#得到最邻近点距离并排序 少数服从多数投票法则
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response]=1
    sortedVotes = sorted(classVotes.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0] #得到最多的那个分类

#测算准确率
def getAccuracy(testSet,predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct +=1
    return (correct/float(len(testSet)))*100.0

def main():
    #prepare data
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset('iris.data.csv',split,trainingSet,testSet)
    print "Train set:" + repr(len(trainingSet))
    print "Test set:" + repr(len(testSet))
    #generate prediction
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet,testSet[x],k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted ='+ repr(result)+ ',actual = '+ repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet,predictions)
    print ('Accuracy:'+ repr(accuracy) +'%')


main()
