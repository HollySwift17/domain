import os
import pandas as pd
import numpy as np
import random

data = pd.read_csv('lstm_result.csv')

l1=data['label'].values
l2=data['pred'].values
l=[]
for i in range(l1.shape[0]):
    l.append(float(l1[i])+random.random())
df=pd.DataFrame()
df['pred']=list(l2)
df['label']=l
df.to_csv('draw.csv')

import matplotlib.pyplot as plt

plt.figure()
plt.scatter(df['label'],df['pred'])

plt.show()
