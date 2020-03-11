Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========================== RESTART: D:\2019\New.py ==========================

Warning (from warnings module):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python37\lib\site-packages\sklearn\externals\joblib\externals\cloudpickle\cloudpickle.py", line 47
    import imp
DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
[0.32685882 0.08596951 0.07625294 0.06214708 0.03831447 0.02682398
 0.02155885 0.01990039 0.01224242 0.2049565  0.11241018 0.0125648 ]
AUC: 0.9293
ACC: 0.9286
Recall: 0.9254
F1-score: 0.9394
Precesion: 0.9538
>>> l1=list(labels.shape[0]*model.feature_importances_)
>>> df['importance']=l1
>>> df
        label    importance
0     有意义单词占比  32685.881853
1      1-gram   8596.950769
2      2-gram   7625.293732
3      3-gram   6214.708090
4      4-gram   3831.447288
5      5-gram   2682.397515
6        数字占比   2155.884728
7      不同字母占比   1990.038902
8      不同数字占比   1224.241592
9          长度  20495.650172
10     元音字母占比  11241.018027
11  字母数字的交换次数   1256.479602
>>> df.to_csv("importance.csv",encoding='utf_8_sig')
>>> 
