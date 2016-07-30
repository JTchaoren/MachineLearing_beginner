#-*- coding:utf-8 -*-
from sklearn import neighbors           #导入sklearn KNN包
from sklearn import datasets            #导入python自带的数据集

knn = neighbors.KNeighborsClassifier()   #调用自带的分类器

iris = datasets.load_iris()

print iris

knn.fit(iris.data,iris.target)        #传统算法 都有一个建模函数fit

predictedLabel = knn.predict([[0.1,0.2,0.3,0.4]])

print predictedLabel  #[0]