#! /usr/bin/python3

#https://stackoverflow.com/questions/45357547/outliers-in-works-schedule
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
#pp.pprint(SampleDF)

plt.hist(SampleDF['TimeIn'],rwidth=0.5,range=(0,24))
plt.hist(SampleDF['TimeOut'],rwidth=0.5,range=(0,24))
plt.xticks(np.arange(0,24, 1.0))
plt.xlabel('Hour of day')
plt.ylabel('Arrival / Departure Time Frequency')
#plt.show()
#Create Sample Data #Create Sample Data #Create Sample Data #Create Sample Data 

# Analyze data # Analyze data # Analyze data # Analyze data # Analyze data # Analyze data 
OutlierSensitivity=0.05 # Will catch extreme events that happen 5% of the time. - one sided! i.e. only late arrivals and early departures.

# Identify one sided outlier: only late arrivals and early departures.
def detect_outlier(obs,argdict):
	#ExpIn,ExpOut,sigIn,sigOut,percentile
	# If Time In is later than expected + 95%
	if ((obs['TimeIn']>argdict['ExpIn']+argdict['percentile']*argdict['sigIn']) 
	# If Time Out is earlier than expected - 95%
		or (obs['TimeOut']<argdict['ExpOut']-argdict['percentile']*argdict['sigOut'])):
		return(obs['EmployeeID'])

# Use mode - (common number) + 95% percentile of the normal distribution:
#ExpectedTimeIn=SampleDF['TimeIn'].mode().mean().round(1)
#ExpectedTimeOut=SampleDF['TimeOut'].mode().mean().round(1)
argdict_current={
	"ExpIn":SampleDF['TimeIn'].mode().mean().round(1)
	,"ExpOut":SampleDF['TimeOut'].mode().mean().round(1)
	,"sigIn":SampleDF['TimeIn'].var()
	,"sigOut":SampleDF['TimeOut'].var()
	,"percentile":scipy.stats.norm.ppf(1-OutlierSensitivity)
}
OutlierIn=argdict_current['ExpIn']+argdict_current['percentile']*argdict_current['sigIn']
OutlierOut=argdict_current['ExpOut']-argdict_current['percentile']*argdict_current['sigOut']
print(OutlierIn)
print(OutlierOut)
#pp.pprint(SampleDF.apply(detect_outlier,argdict=argdict_current,axis=1))
Outliers=SampleDF.apply(detect_outlier,argdict=argdict_current,axis=1)
Outliers=np.sort(Outliers.unique()[~np.isnan(Outliers.unique())])
pp.pprint(argdict_current)
pp.pprint(Outliers)
#pp.pprint(SampleDF.loc[SampleDF['EmployeeID'].isin(Outliers)].sort_values(["TimeIn","TimeOut"],ascending=[0,1]))
#pp.pprint(SampleDF.loc[(SampleDF['TimeIn']>OutlierIn) or (SampleDF['TimeOut']<OutlierOut)].sort_values(["TimeIn","TimeOut"],ascending=[0,1]))
pp.pprint(SampleDF.loc[(SampleDF['TimeIn']>OutlierIn) | (SampleDF['TimeOut']<OutlierOut)].sort_values(["EmployeeID"]))
#pp.pprint(SampleDF['TimeIn'].mode().mean().round(1))
#pp.pprint(SampleDF['TimeIn'])
# For all
# For each
