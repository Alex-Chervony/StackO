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
presetPercentile=scipy.stats.norm.ppf(1-OutlierSensitivity)


# Use mode - (common number) + 95% percentile of the normal distribution:
argdictOverall={
	"ExpIn":SampleDF['TimeIn'].mode().mean().round(1)
	,"ExpOut":SampleDF['TimeOut'].mode().mean().round(1)
	,"sigIn":SampleDF['TimeIn'].var()
	,"sigOut":SampleDF['TimeOut'].var()
	,"percentile":presetPercentile
}
OutlierIn=argdictOverall['ExpIn']+argdictOverall['percentile']*argdictOverall['sigIn']
OutlierOut=argdictOverall['ExpOut']-argdictOverall['percentile']*argdictOverall['sigOut']

# For all
# See all users with outliers - overall
Outliers=SampleDF["EmployeeID"].loc[(SampleDF['TimeIn']>OutlierIn) | (SampleDF['TimeOut']<OutlierOut)]

# See all observations with outliers - Overall
# pp.pprint(SampleDF.loc[(SampleDF['TimeIn']>OutlierIn) | (SampleDF['TimeOut']<OutlierOut)].sort_values(["EmployeeID"]))

# For each
OutliersForEach=[]
for Employee in SampleDF['EmployeeID'].unique():
	#print(Employee)
	SampleDFCurrent=SampleDF.loc[SampleDF['EmployeeID']==Employee]
	argdictCurrent={
		"ExpIn":SampleDFCurrent['TimeIn'].mode().mean().round(1)
		,"ExpOut":SampleDFCurrent['TimeOut'].mode().mean().round(1)
		,"sigIn":SampleDFCurrent['TimeIn'].var()
		,"sigOut":SampleDFCurrent['TimeOut'].var()
		,"percentile":presetPercentile
	}
	OutlierIn=argdictCurrent['ExpIn']+argdictCurrent['percentile']*argdictCurrent['sigIn']
	OutlierOut=argdictCurrent['ExpOut']-argdictCurrent['percentile']*argdictCurrent['sigOut']
	if SampleDFCurrent['TimeIn'].max()>OutlierIn or SampleDFCurrent['TimeOut'].min()<OutlierOut:
		Outliers=np.append(Outliers,Employee)
	#Outliers=np.append(Outliers,SampleDF["EmployeeID"].loc[(SampleDF['TimeIn']>OutlierIn) | (SampleDF['TimeOut']<OutlierOut)])
	#pp.pprint(argdictCurrent)

# Sort and remove NAs
Outliers=np.sort(np.unique(Outliers))
#Outliers=np.sort(Outliers.unique()[~np.isnan(Outliers.unique())])
# Show users with overall outliers:
pp.pprint(Outliers)