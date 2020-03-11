import numpy as np
import pandas as pd
import os


from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC

from machine_learning.lstm import lstm
from machine_learning.xgboost_multi import XGBC

def train_models():
    basepath=os.path.abspath(os.path.dirname(__file__))

    path1=basepath+"/train_data.csv"


    f1=open(path1)
    a=pd.read_csv(f1,header=0).values

    A=np.mat(a)
    print(A)

    row=A.shape[0]
    col=A.shape[1]

    train=A[:,1:col-1]
    label=A[:,col-1]

    print("——————training models——————")

    xgb_model=XGBC()
    xgb_model.fit(train,label)
    xgb_model.bst.save_model('machine_learning/xgb.model')

    clf=SVC()
    clf.fit(train,label)
    joblib.dump(clf, "machine_learning/svc.model")

    clf1 = RandomForestClassifier()
    clf1.fit(train,label)
    joblib.dump(clf1, "machine_learning/rfc.model")


    clf2 = GradientBoostingClassifier()
    clf2.fit(train,label)
    joblib.dump(clf2, "machine_learning/gbc.model")

    clf3 = AdaBoostClassifier()
    clf3.fit(train,label)
    joblib.dump(clf3, "machine_learning/ada.model")

    clf4 = BaggingClassifier()
    clf4.fit(train,label)
    joblib.dump(clf4, "machine_learning/bc.model")

    clf5 = LogisticRegression()
    clf5.fit(train,label)
    joblib.dump(clf5, "machine_learning/lgr.model")


    clf6 = GaussianNB()
    clf6.fit(train,label) 
    joblib.dump(clf6, "machine_learning/nb.model")


    clf7 = KNeighborsClassifier()
    clf7.fit(train,label) 
    joblib.dump(clf7, "machine_learning/knn.model")



    clf8 = LinearRegression()
    clf8.fit(train,label) 
    joblib.dump(clf8, "machine_learning/lnr.model")

    lstm()
    print("done")




