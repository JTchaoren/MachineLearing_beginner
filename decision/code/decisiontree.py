from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO


dataFile =  open(r'../2.csv','rb')
reader = csv.reader(dataFile)
headers = reader.next()        #first line

print(headers)
featureList = []               #tezhen
labelList = []                 #class
for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1, len(row) - 1):
        print(row[i])
        rowDict[headers[i]] = row[i]
        print("rowDict:", rowDict)
    featureList.append(rowDict)

print(featureList)

#Vectortize features
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()

print("dummyX:" + str(dummyX))
print(vec.get_feature_names())

print("labellist:" + str(labelList))

#Vectortize CLASS LABELS
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:" + str(dummyY))

#using decision tree for classification
#clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion= 'entropy') #infogain cha
clf = clf.fit(dummyX,dummyY)              #set model
print("clf:" + str(clf))



#visual model
#with open("decisiontree.dot",'w') as f:
with open("decisiontree.dot",'w') as f:
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)

oneRowX = dummyX[0,:]
# print("oneRowX:" +str(oneRowX))
newRowX = oneRowX

newRowX[0]=1
newRowX[2]=0
# print ("newrowX:" +str(newRowX))

predictedY = clf.predict(newRowX)

print("predictedY:" +str(predictedY))













