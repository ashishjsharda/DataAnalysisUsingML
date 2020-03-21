from pandas import read_csv
path=r'pima-indians-diabetes.csv'
data=read_csv(path)
print(data.shape)
print(data[:4])
