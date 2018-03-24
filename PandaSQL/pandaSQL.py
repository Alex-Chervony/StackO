# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:04:26 2018

@author: Eli-Lenovo
"""

#%% Setup
import pandas as pd
import pandasql as ps

df = pd.DataFrame([['Apple',2,4],
['Apple',3,3],
['Apple',5,9],
['Mango',4,5],
['Mango',6,12],
['Banana',2,2],
['banana',1,2]], columns=
['Fruit',   'Rate',   'Quantity'])

#%% Query
q1 = """
select df.*
from df,
( select fruit, sum(quantity) sm
  from df
  group by fruit
 ) temp
 where 
 df.fruit=temp.fruit
 order by temp.sm desc, df.rate desc;"""

newdf = ps.sqldf(q1, locals())

print(newdf)

#%% Performance Analysis
import timeit
from sklearn.utils import resample

df5mil = resample(df , n_samples=5000, random_state=0)
q2 = """
select df5mil.*
from df5mil,
( select fruit, sum(quantity) sm
  from df5mil
  group by fruit
 ) temp
 where 
 df5mil.fruit=temp.fruit
 order by temp.sm desc, df5mil.rate desc;"""


def performance_test(df):
    df['Total'] = df.groupby('Fruit')['Quantity'].transform('sum')
    return df.sort_values(by=['Total', 'Rate'], ascending=False, axis=0)\
        .drop('Total', 1)

#%% Time
timeit.timeit('newdf5mil = ps.sqldf(q2, locals())', number=10, setup = 'from __main__ import df5mil',globals=globals())
timeit.timeit('newdf5mil = performance_test(df5mil)', number=10, setup = 'from __main__ import df5mil',globals=globals())
