#-*-coding:utf-8-*-
import numpy as np
import pylab as pl
from sklearn import svm

#创建40个 不同的点
np.random.seed(0)
X = np.r_[(np.random.randn(20, 2)-[2, 2],np.random.randn(20,2)+[2,2])]
#标记
Y = [0] *20 + [1] *20

#建立模型
clf = svm.SVC(kernel='linear')
clf.fit(X,Y)

#做出分割平面
w = clf.coef_[0]  #取w
a = -w[0]/w[1]
xx = np.linspace(-5,5)
yy = a*xx - (clf.intercept_[0] )/ w[1] #intercept[0] 取baits

#做出另外两条平行线
b = clf.support_vectors_[0]
yy_down = a *xx +(b[1]-a*b[0])
b = clf.support_vectors_[-1]
yy_up = a *xx +(b[1]-a*b[0])
print "w:  ",w
print "a:  ",a
print "xx:  ",xx
print "yy:  ",yy

print "support_vectors:  ",clf.support_vectors_
print "clf.coef:  ",clf.coef_


pl.plot(xx,yy,'k-')
pl.plot(xx,yy_down,'k--')
pl.plot(xx,yy_up,'k--')

#将点圈出
pl.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],s = 80,facecolors = 'none')
pl.scatter(X[:,0],X[:,1],c=Y,cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()

