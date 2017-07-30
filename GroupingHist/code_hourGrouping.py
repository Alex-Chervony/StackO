#! /usr/bin/python3

# See the list to validate
# import pprint
# pp = pprint.PrettyPrinter(indent=4)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("data.csv")

def sum_hours(obs):
	return(list(range(obs['hour_s'],obs['hour_e']+1,1)))

# Get all existing activity hours (No matter which user)
Hours2D=list(df.apply(sum_hours,axis=1))
# Get all existing hours
HoursFlat=[hour for sublist in Hours2D for hour in sublist]

# See the list to validate
# pp.pprint(HoursFlat)

#fig,ax=plt.subplots(figsize=(6,3))

plt.hist(HoursFlat,rwidth=0.5,range=(0,24))
plt.xticks(np.arange(0,24, 1.0))
plt.xlabel('Hour of day')
plt.ylabel('Frequency')
plt.show()