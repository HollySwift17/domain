
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from stacking_classifier import *

basepath=os.path.abspath(os.path.dirname(__file__))
data = pd.read_csv(basepath+'/train_data.csv')
data= data.sample(frac = 1)

X_train=data.iloc[:,1:8].values
y_train=data.iloc[:,8].values


data1= pd.read_csv(basepath+'/test_data.csv')
data1= data1.sample(frac = 1)

X_test=data1.iloc[:,1:8].values
y_test=data1.iloc[:,8].values


classifier = AdaBoostClassifier(where_store_classifier_model='./classifier_model/demo1_ada.model')
classifier.build_model()
classifier.fit(X_train, y_train)
p_test = classifier.predict(X_test)
print('demo1-1 ada : ', f1_score(y_test, p_test, average='macro'))
'''
classifier = SimpleMLPClassifer(where_store_classifier_model='./classifier_model/demo1_mlp.model',
                                train_params={'input_num': 64, 'class_num': 10})  # 分类器的训练参数通过train_params传入
classifier.build_model()
classifier.fit(X_train, y_train)
p_test = classifier.predict(X_test)
print('demo1-2 mlp: ', f1_score(y_test, p_test, average='macro'))


#demo2:交叉训练包装器,包装后依然当作Classifer使用，所以可以无限包装，但分类器数量会指数增涨
该部分主要为Stacking分类的cv提供协助,独立使用的例子如下:
'''
classifier = RandomForestClassifier(where_store_classifier_model='./classifier_model/demo2_1_rf.model')
classifier = KFolds_Classifier_Training_Wrapper(classifier)  # 默认2-fold,可指定KFolds_Training_Wrapper(classifier,k_fold=5)
classifier.build_model()
classifier.fit(X_train, y_train)
p_test = classifier.predict(X_test)
print('demo2-1 rf : ', f1_score(y_test, p_test, average='macro'))

classifier = RandomForestClassifier(where_store_classifier_model='./classifier_model/demo2_2_rf.model')
classifier = KFolds_Classifier_Training_Wrapper(KFolds_Classifier_Training_Wrapper(classifier, k_fold=5), k_fold=5)  # 这样会训练25个分类器
classifier.build_model()
classifier.fit(X_train, y_train)
p_test = classifier.predict(X_test)
print('demo2-2 rf : ', f1_score(y_test, p_test, average='macro'))

'''
demo3:Stacking集成分类器的使用:Stacking分类器可以利用其它分类器输出,作为另一分类器的输入，前者称基分类器，后者称元分类器
创建方式：classifier=StackClassifer(base_classifiers,meta_classifier,use_probas=True, force_cv=True)
base_classifers:基分类器列表
meta_classifier:元分类器
use_probas:使用使用基分类器的概率预测标签作为元分类器的输入,默认使用
force_cv:是否强制为每个基分类器和元分类器添加KFolds_Training_Wrapper包装,默认添加(如果已经包装的不会再包装),个别分类器不想使用CV方式训练，可以定义force_cv=False,然后单独定义每个基分类器和元分类器
'''

'''
demo3-1:比如利用RF,Ada,Bag,SVM作为基分类器,LR作为元分类器做集成
'''
classifier = StackingClassifier(
    base_classifiers=[
        RandomForestClassifier(where_store_classifier_model='./classifier_model/demo_3_1_layer_2_rf_stack_cv.model'),
        AdaBoostClassifier(where_store_classifier_model='./classifier_model/demo_3_1_layer_2_ada_stack_cv.model'),
        BaggingClassifier(where_store_classifier_model='./classifier_model/demo_3_1_layer_2_bag_stack_cv.model'),
        SVMClassifier(where_store_classifier_model='./classifier_model/demo_3_1_layer_2_svm_stack_cv.model'),
    ],
    meta_classifier=LogisticRegression(where_store_classifier_model='./classifier_model/demo_3_1_layer_1_lr_stack_cv.model'),
)
classifier.build_model()
classifier.fit(train_x=X_train, train_y=y_train)
p_test = classifier.predict(X_test)
print('demo3-1 simple stack: ', f1_score(y_test, p_test, average='macro'))
'''
demo3-2:单独为某些分类器包装KFolds_Training_Wrapper时,设置force_cv=False
'''
classifier = StackingClassifier(
    base_classifiers=[
        KFolds_Classifier_Training_Wrapper(
            RandomForestClassifier(where_store_classifier_model='./classifier_model/demo_3_2_layer_2_rf_stack_cv.model'),
            k_fold=5),  # 仅该基分类器使用CV方式训练
        AdaBoostClassifier(where_store_classifier_model='./classifier_model/demo_3_2_layer_2_ada_stack_cv.model'),
        BaggingClassifier(where_store_classifier_model='./classifier_model/demo_3_2_layer_2_bag_stack_cv.model'),
        SVMClassifier(where_store_classifier_model='./classifier_model/demo_3_2_layer_2_svm_stack_cv.model'),
    ],
    meta_classifier=LogisticRegression(where_store_classifier_model='./classifier_model/demo_3_2_layer_1_lr_stack_cv.model'),
    force_cv=False
)
classifier.build_model()
classifier.fit(train_x=X_train, train_y=y_train)
p_test = classifier.predict(X_test)
print('demo3-2 simple stack: ', f1_score(y_test, p_test, average='macro'))
'''
demo3-3:StackingClassifier也可以作为基分类器使用,所以可以堆叠很深的结构
'''
classifier = StackingClassifier(
    base_classifiers=[
        RandomForestClassifier(where_store_classifier_model='./classifier_model/demo_3_3_layer_2_rf_stack_cv.model'),
        AdaBoostClassifier(where_store_classifier_model='./classifier_model/demo_3_3_layer_2_ada_stack_cv.model'),
        BaggingClassifier(where_store_classifier_model='./classifier_model/demo_3_3_layer_2_bag_stack_cv.model'),
        SVMClassifier(where_store_classifier_model='./classifier_model/demo_3_3_layer_2_svm_stack_cv.model'),
        StackingClassifier(
            base_classifiers=[
                LogisticRegression(where_store_classifier_model='./classifier_model/demo_3_3_layer_3_lr_stack_cv.model'),
                RandomForestClassifier(where_store_classifier_model='./classifier_model/demo_3_3_layer_3_rf_stack_cv.model'),
            ],
            meta_classifier=GradientBoostingClassifier(
                where_store_classifier_model='./classifier_model/demo_3_3_layer_3_gbdt_stack_cv.model'),
        )
    ],
    meta_classifier=LogisticRegression(
        where_store_classifier_model='./classifier_model/demo_3_3_layer_1_lr_stack_cv.model'),
)
classifier.build_model()
classifier.fit(train_x=X_train, train_y=y_train)
p_test = classifier.predict(X_test)
print('demo3-3 deep stack: ', f1_score(y_test, p_test, average='macro'))

'''
demo3-4:StackingClassifier也可以被KFolds_Training_Wrapper包装
'''

classifier = StackingClassifier(
    base_classifiers=[
        RandomForestClassifier(where_store_classifier_model='./classifier_model/demo_3_4_layer_2_rf_stack_cv.model'),
        AdaBoostClassifier(where_store_classifier_model='./classifier_model/demo_3_4_layer_2_ada_stack_cv.model'),
        BaggingClassifier(where_store_classifier_model='./classifier_model/demo_3_4_layer_2_bag_stack_cv.model'),
        SVMClassifier(where_store_classifier_model='./classifier_model/demo_3_4_layer_2_svm_stack_cv.model'),
        StackingClassifier(
            base_classifiers=[
                LogisticRegression(where_store_classifier_model='./classifier_model/demo_3_4_layer_3_lr_stack_cv.model'),
                RandomForestClassifier(where_store_classifier_model='./classifier_model/demo_3_4_layer_3_rf_stack_cv.model'),
            ],
            meta_classifier=GradientBoostingClassifier(
                where_store_classifier_model='./classifier_model/demo_3_4_layer_3_gbdt_stack_cv.model')
        )
    ],
    meta_classifier=LogisticRegression(
        where_store_classifier_model='./classifier_model/demo_3_4_layer_1_lr_stack_cv.model'),
)
classifier=KFolds_Classifier_Training_Wrapper(classifier)
classifier.build_model()
classifier.fit(train_x=X_train, train_y=y_train)
p_test = classifier.predict(X_test)
print('demo3-4 deep deep stack: ', f1_score(y_test, p_test, average='macro'))


"""
classifier = StackingClassifier(
    base_classifiers=[
        RandomForestClassifier(where_store_classifier_model='./classifier_model/demo_3_4_layer_2_rf_stack_cv.model'),
        AdaBoostClassifier(where_store_classifier_model='./classifier_model/demo_3_4_layer_2_ada_stack_cv.model'),
        BaggingClassifier(where_store_classifier_model='./classifier_model/demo_3_4_layer_2_bag_stack_cv.model'),
        SVMClassifier(where_store_classifier_model='./classifier_model/demo_3_4_layer_2_svm_stack_cv.model'),
        SimpleMLPClassifer(where_store_classifier_model='./classifier_model/demo_3_4_layer_2_mlp_stack_cv.model',train_params={'input_num':64,'class_num':10})
    ],
    meta_classifier=LogisticRegression(where_store_classifier_model='./classifier_model/demo_3_4_layer_1_lr_stack_cv.model'),
)
classifier.build_model()
classifier.fit(train_x=X_train, train_y=y_train)
p_test = classifier.predict(X_test)
print('demo3-4 simple stack: ', f1_score(y_test, p_test, average='macro'))

"""
