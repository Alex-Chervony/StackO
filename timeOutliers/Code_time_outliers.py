#! /usr/bin/python3


import random
import pandas as pd
import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)

# Visualize:
import matplotlib.pyplot as plt

#Create Sample Data
# Parameters:
TimeInExpected=8.5 # 8:30am
TimeOutExpected=17 # 5pm
sig=1 # 1 hour variance
Employees=10
SampleSize=300

SampleDF=pd.DataFrame([[np.random.randint(1,Employees),np.random.normal(TimeInExpected, sig),np.random.normal(TimeOutExpected, sig)] for id in range(1,SampleSize,1)])

SampleDF2=pd.DataFrame([
	np.random.randint(1,Employees,size=(1,SampleSize,1)),
	np.random.normal(TimeInExpected, sig,size=(1,SampleSize,1)),
	np.random.normal(TimeOutExpected, sig,size=(1,SampleSize,1))
])
SampleDF.columns = ['EmployeeID', 'TimeIn','TimeOut']
SampleDF2.columns = ['EmployeeID', 'TimeIn','TimeOut']

# Show Time distributions
pp.pprint(SampleDF)

plt.hist(SampleDF['TimeIn'],rwidth=0.5,range=(0,24))
plt.hist(SampleDF['TimeOut'],rwidth=0.5,range=(0,24))
plt.xticks(np.arange(0,24, 1.0))
plt.xlabel('Hour of day')
plt.ylabel('Arrival / Departure Time Frequency')
#plt.show()




# Use mode - (common number) + 1.96 standard deviation:
pp.pprint(SampleDF['TimeIn'])

# Use 95% percentil of the normal distribution:
