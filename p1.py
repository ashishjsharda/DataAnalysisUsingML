from numpy import loadtxt
path = r"pima-indians-diabetes.csv"
datapath=open(path,'r')
data=loadtxt(datapath,delimiter=",")
print(data.shape)
print(data[:2])
