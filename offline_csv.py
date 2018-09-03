

import pandas as pd
df  = pd.read_csv('D:/auto.csv')
#print(df)

#print(df.describe(include='all'))

#print(df["symboling"])

#print(df.info())

#df["price"]= df["price"].astype("int")

df["length"]=df["length"]/df["length"].max()
