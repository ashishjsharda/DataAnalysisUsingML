'''
Created on Oct 21, 2019

@author: asharda
'''
from pandas import DataFrame, read_csv, scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd 

file = r'data/PlanningComm.xlsx'
df = pd.read_excel(file)
print(df.shape)
print(df[:3])
#Histogram
df.hist()
plt.show()
