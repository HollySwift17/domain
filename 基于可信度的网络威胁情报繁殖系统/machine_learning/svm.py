from sklearn import svm
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import os
from Venn_abers import *

print("——————SVM——————")
basepath=os.path.abspath(os.path.dirname(__file__))

path1=basepath+"/train_data.csv"

f1=open(path1)
a=pd.read_csv(f1).values
A=np.mat(a)
row=A.shape[0]
col=A.shape[1]

train=A[:,1:col-1]
label=A[:,col-1]
    
clf = svm.SVC()
clf.fit(train,label) 
joblib.dump(clf, "svm.model")


basepath=os.path.abspath(os.path.dirname(__file__))
data = pd.read_csv(basepath+'/test_data.csv')
row=data.shape[0]
col=data.shape[1]
features=data.iloc[:,1:col-1]
labels=data.iloc[:,col-1]
print("test_svm_vennabers")
     
clf = joblib.load("svm.model")
        
pred=clf.predict(features)
l1=[]
correct=0
for i in range(labels.shape[0]):
    if abs(labels[i]-pred[i])<0.000000001:
        correct+=1
    temp=(labels[i],pred[i])
    l1.append(temp)

l2=list(pred)

p0,p1=ScoresToMultiProbs(l1,l2)


print(correct/labels.shape[0])
print(p0)
print(p1)
df=pd.DataFrame()

df['label']=labels
df['pred']=pred
df.to_csv(basepath+'/pred_result/svm_result.csv')
