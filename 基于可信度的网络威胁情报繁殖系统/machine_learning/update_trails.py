import os
import pandas as pd
import numpy as np
from os import path
d = path.dirname(__file__)
parent_path = os.path.dirname(d)
def update():

    #basepath=os.path.abspath(os.path.dirname(__file__))
    basepath=parent_path
    i=0
    for info in os.listdir(basepath+"/trails"):
        _info=info.strip('.csv')
        print(_info)
        domain = os.path.abspath(basepath+"/trails") #获取文件夹的路径
        info = os.path.join(domain,info) #将路径与文件名结合起来就是每个文件的完整路径  
        data = pd.read_csv(info,sep='\t',header=None)
        if data.shape[1]!=13:
            print("????")
            print(_info)
            i=input()

        if i==0:
            df=data
        else:
            df=pd.concat([df,data])
                
        print(data)

        i+=1
    
    df=df.sample(frac = 1)
    df=df.dropna(axis=0)


    temp=df.iloc[:10000]
    print(temp)
    temp.to_csv("machine_learning/test_data1.csv")

    temp=df.iloc[10000:20000]
    print(temp)
    temp.to_csv("machine_learning/test_data2.csv")

    temp=df.iloc[20000:30000]
    print(temp)
    temp.to_csv("machine_learning/test_data3.csv")

    temp=df.iloc[30000:40000]
    print(temp)
    temp.to_csv("machine_learning/test_data4.csv")

    temp=df.iloc[40000:50000]
    print(temp)
    temp.to_csv("machine_learning/test_data5.csv")

    temp=df.iloc[50000:150000]
    print(temp)
    temp.to_csv("machine_learning/train_data.csv")


