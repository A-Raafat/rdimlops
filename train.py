import numpy as np
import matplotlib.pyplot as plt
import lightgbm as lgb
from lightgbm import LGBMClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
import cv2
import os
from glob import glob
import joblib
import seaborn as sns


train_data_path='Data/train/'
test_data_path ='Data/test/'

train_x_list = glob(train_data_path + "*/*.jpg")
test_x_list = glob(test_data_path + "*/*.jpg")


def prep_data(list_of_path):
    x = []
    y = []
    for path in list_of_path:
        im = cv2.imread(path,0)/255.0
        if 'NORMAL' in path :
            label = 0
        elif 'COVID' in path:
            label = 1
        im = cv2.resize(im, (150,150))
        im = im.reshape(1,-1)
        x.append(im)
        y.append(label)
    
    x = np.array(x)
    y = np.array(y)
    
    return x,y
    
    
x_train, y_train = prep_data(train_x_list)
x_test, y_test = prep_data(test_x_list)

x_train = x_train.reshape((x_train.shape[0], x_train.shape[-1]))
x_test = x_test.reshape((x_test.shape[0], x_test.shape[-1]))


## Creating lightgbm datasets
lgb_train = lgb.Dataset(x_train, y_train)
lgb_valid = lgb.Dataset(x_test, y_test, reference=lgb_train)

#Configuring parameters:
params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': {'binary_error'},
    'num_leaves': 20,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'min_data_in_leaf':4,
     #'min_sum_hessian_in_leaf': 5,
    'verbose':10
}

# Training

evals_result = {} 
gbm = lgb.train(params,
                lgb_train,
                num_boost_round=200,
                valid_sets=[lgb_train, lgb_valid],
                evals_result=evals_result,
                verbose_eval=10,
                early_stopping_rounds=50)

#Plotting the result:
lgb.plot_metric(evals_result, metric='binary_error')

pred = model.predict(x_test)
pred[pred > 0.5] = 1
pred[pred < 0.5] = 0


cm = confusion_matrix(y_test, pred)
sns.heatmap(cm, annot=True, xticklabels=['Covid', 'Normal'], yticklabels=['Covid', 'Normal'])

Precision,Recall,F1_score,_ = precision_recall_fscore_support(y_test, pred, average='macro')
Accuracy = accuracy_score(y_test, pred)
print(f'Precision: {Precision}\nRecall: {Recall}\nF1_score: {F1_score}\nAccuracy: {Accuracy}')


joblib.dump(model, 'lgb.pkl')
