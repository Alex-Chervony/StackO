# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:04:26 2018

@author: Eli-Lenovo
"""


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
