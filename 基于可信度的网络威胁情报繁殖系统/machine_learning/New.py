
# plot feature importance manually

from numpy import loadtxt

from xgboost import XGBClassifier

from matplotlib import pyplot

import pandas as pd

import os





# load data
basepath=os.path.abspath(os.path.dirname(__file__))

path1=basepath+"/train_data.csv"

f1=open(path1)
dataset = pd.read_csv(f1).values

# split data into X and y
row=dataset.shape[0]

col=dataset.shape[1]
    
X = dataset[:,1:col-1]

y = dataset[:,col-1]

# fit model no training data

model = XGBClassifier()

model.fit(X, y)

# feature importance

print(model.feature_importances_)

# plot

pyplot.bar(range(len(model.feature_importances_)), model.feature_importances_)

pyplot.show()


basepath=os.path.abspath(os.path.dirname(__file__))
data = pd.read_csv(basepath+'/test_data.csv')
row=data.shape[0]
col=data.shape[1]
features=data.iloc[:,1:col-1].values[:]
labels=data.iloc[:,col-1].values[:]
ypred=model.predict(features)
y_pred = (ypred >= 0.5)*1
from sklearn import metrics
print('AUC: %.4f' % metrics.roc_auc_score(labels,ypred))
print('ACC: %.4f' % metrics.accuracy_score(labels,y_pred))
print('Recall: %.4f' % metrics.recall_score(labels,y_pred))
print('F1-score: %.4f' %metrics.f1_score(labels,y_pred))
print('Precesion: %.4f' %metrics.precision_score(labels,y_pred))
metrics.confusion_matrix(labels,y_pred)



l1=list(labels.shape[0]*model.feature_importances_)

l2=['有意义单词占比','1-gram','2-gram','3-gram','4-gram','5-gram','数字占比','不同字母占比','不同数字占比','长度','元音字母占比','字母数字的交换次数']

df=pd.DataFrame()
df['label']=l2
df['importance']=l1
df.to_csv("importance.csv",encoding='utf_8_sig')
