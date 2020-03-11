import os
import pandas as pd
import numpy as np
from datetime import *

df=pd.DataFrame()
df['name']='lstm'
df['time']=[date(2019 ,5,1),date(2019 ,5,2),date(2019 ,5,3),date(2019 ,5,4),date(2019 ,5,5)]
df['venn_abers_score']=[0.9197419,0.79371844,0.73002601,0.67301801,0.63623541]
df['name']='lstm'

data=df

df=pd.DataFrame()
df['name']='RandomForest'
df['time']=[date(2019 ,5,1),date(2019 ,5,2),date(2019 ,5,3),date(2019 ,5,4),date(2019 ,5,5)]
df['venn_abers_score']=[0.99256189,0.99249703,0.98103479,0.97503314,0.94685059]
df['name']='RandomForest'

data=pd.concat([data,df])


df=pd.DataFrame()
df['name']='GradientBoosting'
df['time']=[date(2019 ,5,1),date(2019 ,5,2),date(2019 ,5,3),date(2019 ,5,4),date(2019 ,5,5)]
df['venn_abers_score']=[0.92866097,0.82015125,0.75800008,0.71218167,0.67197485]
df['name']='GradientBoosting'

data=pd.concat([data,df])



df=pd.DataFrame()
df['name']='AdaBoost'
df['time']=[date(2019 ,5,1),date(2019 ,5,2),date(2019 ,5,3),date(2019 ,5,4),date(2019 ,5,5)]
df['venn_abers_score']=[0.92839353,0.82532622,0.76893411,0.72469152,0.68838117]
df['name']='AdaBoost'

data=pd.concat([data,df])



df=pd.DataFrame()
df['name']='Bagging'
df['time']=[date(2019 ,5,1),date(2019 ,5,2),date(2019 ,5,3),date(2019 ,5,4),date(2019 ,5,5)]
df['venn_abers_score']=[0.99782707,0.99752372,0.99810624,0.99106076,0.97885181]
df['name']='Bagging'

data=pd.concat([data,df])





df=pd.DataFrame()
df['name']='LogisticRegression'
df['time']=[date(2019 ,5,1),date(2019 ,5,2),date(2019 ,5,3),date(2019 ,5,4),date(2019 ,5,5)]
df['venn_abers_score']=[0.89829007,0.79516607,0.74148155,0.6941717,0.66473527]
df['name']='LogisticRegression'

data=pd.concat([data,df])



df=pd.DataFrame()
df['name']='GaussianNB'
df['time']=[date(2019 ,5,1),date(2019 ,5,2),date(2019 ,5,3),date(2019 ,5,4),date(2019 ,5,5)]
df['venn_abers_score']=[0.79577783,0.73263642,0.700828,0.6768837,0.66388579]
df['name']='GaussianNB'

data=pd.concat([data,df])


df=pd.DataFrame()
df['name']='KNeighbors'
df['time']=[date(2019 ,5,1),date(2019 ,5,2),date(2019 ,5,3),date(2019 ,5,4),date(2019 ,5,5)]
df['venn_abers_score']=[0.93299012,0.92591934,0.93616521,0.74381727,0.6729004]
df['name']='KNeighbors'

data=pd.concat([data,df])




df=pd.DataFrame()
df['name']='xgboost'
df['time']=[date(2019 ,5,1),date(2019 ,5,2),date(2019 ,5,3),date(2019 ,5,4),date(2019 ,5,5)]
df['venn_abers_score']=[0.81000417,0.7364299,0.69576565,0.66516392,0.63922649]
df['name']='xgboost'

data=pd.concat([data,df])





data.to_csv("venn_abers.csv")




