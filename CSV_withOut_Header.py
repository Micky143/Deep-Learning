#EDA
import pandas as pd

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url,header=None)
print(df)

header = ["sysboling","normalized-losses","make","fuel-type","aspiration",
                "num-of-door","body-style","drive-wheels","engine-location","lenght",
                "width","height","crub-weight","engine-type","num-of-cylinders",
                "engine-size","fuel-system","bore","strok","compression-ratio","horsepower",
                "peak-rpm","city-mpg","highway-mpg","price"]


#df.head(5) first row
#df.tail(5)  last row
#df.info(5)
#df.describe(5)

df.columns=header
df.head(5)
