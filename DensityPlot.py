'''
Created on Oct 5, 2019
Density Plot
@author: asharda
'''
from pandas import DataFrame, read_csv, scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd 

file = r'data/PlanningComm.xlsx'
df = pd.read_excel(file)
print(df.shape)
# print(df[:3])
#Density Plot
df.plot(kind='density',subplots=True,layout=(3,3),sharex=False)
plt.show()
