import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from lightgbm import LGBMClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
import cv2
import os
from glob import glob
import joblib

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



model = ltb.LGBMClassifier(boosting_type='gbdt', 
                 objective='binary',
                 num_iteration=100, max_depth=4, learning_rate=0.01, 
                 n_estimators=100, nthread=4, silent=False)
      
      
      
                 
                 
model.fit(x_train,y_train)


pred = model.predict(x_test)

cm = confusion_matrix(y_test, pred)
print(cm)

Precision,Recall,F1_score,_ = precision_recall_fscore_support(y_test, pred, average='macro')
Accuracy = accuracy_score(y_test, pred)
print(f'Precision: {Precision}\nRecall: {Recall}\nF1_score: {F1_score}\nAccuracy: {Accuracy}')


joblib.dump(model, 'lgb.pkl')
