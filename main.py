import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df1=pd.read_csv("zillow.csv")
pd.read_csv('zillow.csv',names=['ID','LivingSpace (sqft)','Beds','Baths','Zip','Year','ListPrice ($)'],index_col=False)
sort=df1.sort_values(by='Baths').head(20)
df=pd.DataFrame(sort)
print(df)
x=np.arange(20)
plt.plot(x,df['Baths'],label='Baths',color='r')
plt.show()