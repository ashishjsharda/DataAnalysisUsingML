'''
Created on Oct 6, 2019
K-Means Algorithm
@author: asharda
'''
from pandas import DataFrame, read_csv, scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn import preprocessing
from numpy import set_printoptions
from sklearn.datasets.samples_generator import make_blobs
X, y_true = make_blobs(n_samples = 400, centers = 4, cluster_std = 0.60, random_state = 0)
plt.scatter(X[:, 0], X[:, 1], s = 20);
plt.show()

