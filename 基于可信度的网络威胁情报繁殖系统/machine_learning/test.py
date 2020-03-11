import os
import pandas as pd
import numpy as np
from machine_learning.Venn_abers import *
from sklearn.externals import joblib
from keras.models import load_model
from machine_learning.lstm import split_data
from machine_learning.xgboost_multi import XGBC
import xgboost as xgb
import heapq
from sklearn.metrics import precision_score,recall_score,f1_score





basepath=os.path.abspath(os.path.dirname(__file__))
data = pd.read_csv(basepath+'/test_data2.csv')
row=data.shape[0]
col=data.shape[1]
features=data.iloc[:,1:col-1].values
labels=data.iloc[:,col-1].values
print(features)
print(labels)
print(features.shape)

def test_lstm_vennabers():
    print("test_lstm_vennabers")
    model = load_model('machine_learning/my_model.h5')
    x=data.iloc[:,1:col-1]
    y=data.iloc[:,col-1]

    (x_test, y_test),(x, y)= split_data(x,y)
    #x_test = reshape_3(x_test)
    pred= model.predict(x_test, batch_size=1000)
    
    l1=[]
    pred_=[]

    for i in range(labels.shape[0]):
        if pred[i,0]>=0.5:
            pred_.append(1)
        else:
            pred_.append(0)
        temp=(labels[i],pred_[i])
        l1.append(temp)
        
    l2=pred_


    p0,p1=ScoresToMultiProbs(l1,l2)

    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=y_test[:,0]
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/lstm_result.csv')
    print(precision_score(labels,pred_))
    print(recall_score(labels,pred_))
    print(f1_score(labels,pred_))
    print(p0[0])
    return p0[0],pred_


def test_svm_vennabers():
    print("test_svm_vennabers")
     
    clf = joblib.load("machine_learning/svc.model")
        
    pred=clf.predict(features)

    l1=[]
    
    for i in range(labels.shape[0]):
        temp=(labels[i],pred[i])
        l1.append(temp)

    l2=list(pred)

    p0,p1=ScoresToMultiProbs(l1,l2)

    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/svm_result.csv')
    print(precision_score(labels,pred))
    print(recall_score(labels,pred))
    print(f1_score(labels,pred))
    print(p0[0])
    return p0[0],pred


def test_rfc_vennabers():

    print("test_rfc_vennabers")
     
    clf = joblib.load("machine_learning/rfc.model")
        
    pred=clf.predict(features)

    l1=[]
    
    for i in range(labels.shape[0]):
        temp=(labels[i],pred[i])
        l1.append(temp)

    l2=list(pred)

    p0,p1=ScoresToMultiProbs(l1,l2)


    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/rfc_result.csv')
    print(precision_score(labels,pred))
    print(recall_score(labels,pred))
    print(f1_score(labels,pred))
    print(p0[0])
    return p0[0],pred

def test_gbc_vennabers():
    print("test_gbc_vennabers")
     
    clf = joblib.load("machine_learning/gbc.model")
        
    pred=clf.predict(features)

    l1=[]
    for i in range(labels.shape[0]):
        
        temp=(labels[i],pred[i])
        l1.append(temp)

    l2=list(pred)

    p0,p1=ScoresToMultiProbs(l1,l2)


    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/gbc_result.csv')
    print(precision_score(labels,pred))
    print(recall_score(labels,pred))
    print(f1_score(labels,pred))
    print(p0[0])
    return p0[0],pred

def test_ada_vennabers():
    print("test_ada_vennabers")
    clf = joblib.load("machine_learning/ada.model")
        
    pred=clf.predict(features)

    l1=[]
    
    for i in range(labels.shape[0]):
        
        temp=(labels[i],pred[i])
        l1.append(temp)

    l2=list(pred)

    p0,p1=ScoresToMultiProbs(l1,l2)


    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/ada_result.csv')
    print(precision_score(labels,pred))
    print(recall_score(labels,pred))
    print(f1_score(labels,pred))
    print(p0[0])
    return p0[0],pred


def test_bc_vennabers():
    print("test_bc_vennabers")
    clf = joblib.load("machine_learning/bc.model")
        
    pred=clf.predict(features)

    l1=[]
    
    for i in range(labels.shape[0]):
        
        temp=(labels[i],pred[i])
        l1.append(temp)

    l2=list(pred)

    p0,p1=ScoresToMultiProbs(l1,l2)


    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/bc_result.csv')
    print(precision_score(labels,pred))
    print(recall_score(labels,pred))
    print(f1_score(labels,pred))
    print(p0[0])
    return p0[0],pred


def test_lgr_vennabers():
    print("test_lgr_vennabers")
     
    clf = joblib.load("machine_learning/lgr.model")
        
    pred=clf.predict(features)

    l1=[]
    
    for i in range(labels.shape[0]):
        
        temp=(labels[i],pred[i])
        l1.append(temp)

    l2=list(pred)

    p0,p1=ScoresToMultiProbs(l1,l2)

    
    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/lgr_result.csv')
    print(precision_score(labels,pred))
    print(recall_score(labels,pred))
    print(f1_score(labels,pred))
    print(p0[0])
    return p0[0],pred




def test_nb_vennabers():
    print("test_nb_vennabers")
    clf = joblib.load("machine_learning/nb.model")
        
    pred=clf.predict(features)

    l1=[]
    
    for i in range(labels.shape[0]):
        
        temp=(labels[i],pred[i])
        l1.append(temp)

    l2=list(pred)

    p0,p1=ScoresToMultiProbs(l1,l2)


    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/nb_result.csv')
    print(precision_score(labels,pred))
    print(recall_score(labels,pred))
    print(f1_score(labels,pred))
    print(p0[0])
    return p0[0],pred


def test_knn_vennabers():
    print("test_knn_vennabers")
     
    clf = joblib.load("machine_learning/knn.model")
        
    pred=clf.predict(features)

    l1=[]
    
    for i in range(labels.shape[0]):
        
        temp=(labels[i],pred[i])
        l1.append(temp)

    l2=list(pred)

    p0,p1=ScoresToMultiProbs(l1,l2)


    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/knn_result.csv')
    print(precision_score(labels,pred))
    print(recall_score(labels,pred))
    print(f1_score(labels,pred))
    print(p0[0])
    return p0[0],pred


def test_lnr_vennabers():
    print("test_lnr_vennabers")
     
    clf = joblib.load("machine_learning/lnr.model")
        
    pred=clf.predict(features)

    l1=[]
    
    for i in range(labels.shape[0]):
        
        temp=(labels[i],pred[i])
        l1.append(temp)

    l2=list(pred)

    p0,p1=ScoresToMultiProbs(l1,l2)


    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred
    df.to_csv(basepath+'/pred_result/lnr_result.csv')
    print(precision_score(labels,pred))
    print(recall_score(labels,pred))
    print(f1_score(labels,pred))
    print(p0[0])
    return p0[0],pred




    

def test_xgb_vennabers():
    print("test_xgb_vennabers")

    model=XGBC()
    model.bst = xgb.Booster(model_file='machine_learning/xgb.model')

    pred = model.predict_proba(features)

    l1=[]
    l2=[]
    pred_=[]
    for i in range(labels.shape[0]):
        if pred[i,1]>pred[i,0]:
            pred_.append(1)
            
        if pred[i,1]<pred[i,0]:
            pred_.append(0)
            
                
        temp=(labels[i],pred[i,1])
        l1.append(temp)
        l2.append(pred[i,1])


    p0,p1=ScoresToMultiProbs(l1,l2)

    #print(p0)
    #print(p1)
    df=pd.DataFrame()

    df['label']=labels
    df['pred']=pred[:,1]
    df.to_csv(basepath+'/pred_result/xgb_result.csv')
    print(precision_score(labels,pred_))
    print(recall_score(labels,pred_))
    print(f1_score(labels,pred_))
    print(p0[0])
    return p0[0],pred_

k=3
rate=0.5

def test():
    p=[]
    pred=[]
    p0,pred0=test_lstm_vennabers()
    p.append(p0)
    pred.append(pred0)
    p0,pred0=test_svm_vennabers()
    p.append(p0)
    pred.append(pred0)
    p0,pred0=test_rfc_vennabers()
    p.append(p0)
    pred.append(pred0)
    p0,pred0=test_gbc_vennabers()
    p.append(p0)
    pred.append(pred0)
    p0,pred0=test_ada_vennabers()
    p.append(p0)
    pred.append(pred0)
    p0,pred0=test_bc_vennabers()
    p.append(p0)
    pred.append(pred0)
    p0,pred0=test_lgr_vennabers()
    p.append(p0)
    pred.append(pred0)
    p0,pred0=test_nb_vennabers()
    p.append(p0)
    pred.append(pred0)
    p0,pred0=test_knn_vennabers()
    p.append(p0)
    pred.append(pred0)

    p0,pred0=test_xgb_vennabers()
    p.append(p0)
    pred.append(pred0)
    print(p)
    
    max_num_index_list = map(p.index, heapq.nlargest(k, p))
    l=list(max_num_index_list)
    print(l)

    pred_=[]
    preds=np.zeros((k,labels.shape[0]))
    tttt=0
    
    
    for i in l:
        temp=pred[i]
        print(i)
        print(temp)
        for j in range(labels.shape[0]):
            preds[tttt,j]=temp[j]
            
        tttt+=1
    

    pred_=[]
    for i in range(labels.shape[0]):
        if np.mean(preds[:,i])>rate:
            pred_.append(1)
        else:
            pred_.append(0)
    

    
    print(precision_score(labels,pred_))
    print(recall_score(labels,pred_))
    print(f1_score(labels,pred_))

    data.iloc[:,col-1]=pred_
    df=pd.read_csv(basepath+'/train_data.csv')
    df=pd.concat([df,data])
    df=df.iloc[:,1:col-1]
    df.to_csv("machine_learning/train_data.csv")
    










