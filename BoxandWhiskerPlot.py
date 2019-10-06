'''
Created on Oct 6, 2019
Box and Whisker Plot
@author: asharda
'''
from pandas import DataFrame, read_csv, scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd 

path = r'data/pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names = names)
data.plot(kind = 'box', subplots = True, layout = (3,3), sharex = False,sharey = False)
plt.show()
