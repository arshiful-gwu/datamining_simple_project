#%%
#All libraries required

# __ __ __ __ __ __ __
#|                    |
#|                    |
#|                    |
#|    HAND WRITTEN    | 28
#|        DIGIT       |
#|                    |
#|__ __ __ __ __ __ __|  
#          28

#28*28=784 pixels
from datetime import datetime
startTime = datetime.now()

import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


import os

#import pixel data
data=pd.read_csv("imageData.csv").as_matrix()

neighbors = 5

knn = KNeighborsClassifier(n_neighbors=neighbors) # instantiate with n value given

#training_dataset
xtrain=data[0:21000,1:]
train_label=data[0:21000,0]

knn.fit(xtrain,train_label)

#testing data
xtest=data[21000:,1:]
actual_label=data[21000:,0]

#d=xtest[15]# this is a 1
#d=xtest[16]# this is a 9
#d=xtest[17]# this is a 5
d=xtest[18]# this is a 2


d.shape=(28,28)
pt.imshow(255-d,cmap='gray')
#print(knn.predict([xtest[15]])) # this is a 1
#print(knn.predict([xtest[16]])) # this is a 9
#print(knn.predict([xtest[17]])) # this is a 5
print(knn.predict([xtest[18]])) # this is a 2
pt.show()


p=knn.predict(xtest)
count=0
for i in range (0,21000):
    count+=1 if p[i]==actual_label[i] else 0
print("KNN Accuracy=", (count/21000)*100)

print(confusion_matrix(actual_label,p))
print(classification_report(actual_label,p))

print(datetime.now() - startTime)
