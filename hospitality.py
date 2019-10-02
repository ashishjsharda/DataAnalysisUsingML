'''
Created on Oct 2, 2019
DataSet:Hospitality in era of AirBnb
https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
@author: asharda
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data = pd.read_csv(r'data/AB_NYC_2019.csv')
print(data.head(5))
print(data.shape)
print(data.describe().T)
# print(data.corr().style.background_gradient(cmap="coolwarm"))
data.corr().style.background_gradient(cmap="coolwarm")
plt.show()
f,ax=plt.subplots(1,2,figsize=(18,8))
data['neighbourhood_group'].value_counts().plot.pie(explode=[0,0.1,0,0,0],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Share of Neighborhood')
ax[0].set_ylabel('Neighborhood Share')
sns.countplot('neighbourhood_group',data=data,ax=ax[1])
ax[1].set_title('Share of Neighborhood')
plt.show()
