#! /usr/bin/python3


import random
import pandas as pd
import numpy as np
import scipy.stats
import pprint
pp = pprint.PrettyPrinter(indent=4)

# Visualize:
import matplotlib.pyplot as plt

#Create Sample Data #Create Sample Data #Create Sample Data #Create Sample Data 
# Parameters:
TimeInExpected=8.5 # 8:30am
TimeOutExpected=17 # 5pm
sig=1 # 1 hour variance
Employees=10
SampleSize=300

SampleDF2=pd.DataFrame([
	np.random.randint(1,Employees,size=(SampleSize)),
	np.around(np.random.normal(TimeInExpected, sig,size=(SampleSize)),2),
	np.around(np.random.normal(TimeOutExpected, sig,size=(SampleSize)),2)
	]).T
SampleDF2.columns = ['EmployeeID', 'TimeIn','TimeOut']

# Show Time distributions
#pp.pprint(SampleDF2)

plt.hist(SampleDF2['TimeIn'],rwidth=0.5,range=(0,24))
plt.hist(SampleDF2['TimeOut'],rwidth=0.5,range=(0,24))
plt.xticks(np.arange(0,24, 1.0))
plt.xlabel('Hour of day')
plt.ylabel('Arrival / Departure Time Frequency')
plt.show()
#Create Sample Data #Create Sample Data #Create Sample Data #Create Sample Data 

# Analyze data # Analyze data # Analyze data # Analyze data # Analyze data # Analyze data 
# Use mode - (common number) + 1.96 standard deviation - 
#pp.pprint(SampleDF2['TimeIn'])
scipy.stats.norm(0, 1).cdf(0.95)


# Use 95% percentil of the normal distribution:
