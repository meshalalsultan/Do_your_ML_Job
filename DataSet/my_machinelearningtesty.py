# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import keras
from keras import Sequential
import pandas as pd
import sklearn


df=pd.read_csv('House price prediction.csv')


new_df = df.drop(['city' ,'statezip' ,'street'] , axis = 1)

x = new_df.iloc[ : , 2:15]
y = new_df.iloc[ : , 1]

from sklearn.preprocessing import LabelEncoder , OneHotEncoder

onehotencoder = OneHotEncoder(categorical_features = [15])
x = onehotencoder.fit_transform(x).toarrey()



labelencoder_x_1 = LabelEncoder()
x [ :,15] = labelencoder_x_1.fit_transform (x [ :,15])

#labelencoder_x_2 = LabelEncoder()
#x [ :,15] = labelencoder_x_2.fit_transform (x [ :,15])
