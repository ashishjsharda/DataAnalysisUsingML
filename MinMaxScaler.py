'''
Created on Oct 6, 2019
MinMax Scaler
@author: asharda
'''
from pandas import DataFrame, read_csv, scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn import preprocessing
from numpy import set_printoptions

path = r'data/pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names = names)
array = data.values
data_scalar=preprocessing.MinMaxScaler(feature_range=(0,1))
data_rescaled=data_scalar.fit_transform(array)
set_printoptions(precision=1)
print("\n Scaled Data:\n       ",data_rescaled)
