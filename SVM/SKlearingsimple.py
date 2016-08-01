#-*-coding:utf-8-*-
from sklearn import svm

#二维空间定义三个点
x = [[2,0],[1,1],[2,3]]
#对应的归类标记
y = [0,0,1]

#调用SVC函数 kernel方法
clf = svm.SVC(kernel= 'linear')
clf.fit(x,y)

print clf

#获取支持向量
print clf.support_vectors_

#那些点属于支持向量 index
print clf.support_

#类里分别取出支持向量的个数
print clf.n_support_

print clf.predict([2,0])
