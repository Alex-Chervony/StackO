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
SampleSize=500
Accuracy=1 # Each hour is segmented by hour tenth (6 minutes)

SampleDF=pd.DataFrame([
	np.random.randint(1,Employees,size=(SampleSize)),
	np.around(np.random.normal(TimeInExpected, sig,size=(SampleSize)),Accuracy),
	np.around(np.random.normal(TimeOutExpected, sig,size=(SampleSize)),Accuracy)
	]).T
SampleDF.columns = ['EmployeeID', 'TimeIn','TimeOut']

# Show Time distributions
pp.pprint(SampleDF)

plt.hist(SampleDF['TimeIn'],rwidth=0.5,range=(0,24))
plt.hist(SampleDF['TimeOut'],rwidth=0.5,range=(0,24))
plt.xticks(np.arange(0,24, 1.0))
plt.xlabel('Hour of day')
plt.ylabel('Arrival / Departure Time Frequency')
plt.show()
#Create Sample Data #Create Sample Data #Create Sample Data #Create Sample Data 

# Analyze data # Analyze data # Analyze data # Analyze data # Analyze data # Analyze data 
OutlierSensitivity=0.05 # Will catch extreme events that happen 5% of the time. - one sided! i.e. only late arrivals and early departures.
sensitivity_percentile=scipy.stats.norm.ppf(1-OutlierSensitivity)

# Identify one sided outlier: only late arrivals and early departures.
def detect_outlier(obs,ExpIn,ExpOut,sigIn,sigOut,percentile):
	# If Time In is later than expected + 95%
	if ((obs['TimeIn']>ExpIn+percentile*sigIn) 
	# If Time Out is earlier than expected - 95%
		or (obs['TimeOut']<ExpOut-percentile*sigOut)):
		return(obs['EmployeeID'])

# Use mode - (common number) + 95% percentile of the normal distribution:
pp.pprint(SampleDF.mode())
#pp.pprint(SampleDF['TimeIn'])
# For all
# For each
