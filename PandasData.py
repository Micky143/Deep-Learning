#Create a pandas Series pass as aruguments have NON.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
m = pd.Series(['Micky',2,3,5,np.nan,9])
print(m)

dates = pd.date_range('20180101', periods=6)
print(dates)

'''
important Qus.. for as.
----------------------------------------------------------------------------------------------------
Qus:- Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
----------------------------------------------------------------------------------------------------
'''


dates = pd.date_range('20130101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)




df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print(df2)
print(df2.dtypes)
#Exadatum //Website







