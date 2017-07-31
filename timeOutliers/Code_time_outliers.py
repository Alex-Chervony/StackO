#! /usr/bin/python3

import random
import pandas as pd
import numpy as np
import scipy.stats
import pprint
pp = pprint.PrettyPrinter(indent=4)

# Visualize:
import matplotlib.pyplot as plt

#### Create Sample Data START
# Parameters:
TimeInExpected=8.5 # 8:30am
TimeOutExpected=17 # 5pm
sig=1 # 1 hour variance
Persons=11
# Increasing the ratio between sample size and persons will make more people outliers.
SampleSize=20
Accuracy=1 # Each hour is segmented by hour tenth (6 minutes)

# Generate sample
SampleDF=pd.DataFrame([
	np.random.randint(1,Persons,size=(SampleSize)),
	np.around(np.random.normal(TimeInExpected, sig,size=(SampleSize)),Accuracy),
	np.around(np.random.normal(TimeOutExpected, sig,size=(SampleSize)),Accuracy)
	]).T
SampleDF.columns = ['PersonID', 'TimeIn','TimeOut']

# Visualize
plt.hist(SampleDF['TimeIn'],rwidth=0.5,range=(0,24))
plt.hist(SampleDF['TimeOut'],rwidth=0.5,range=(0,24))
plt.xticks(np.arange(0,24, 1.0))
plt.xlabel('Hour of day')
plt.ylabel('Arrival / Departure Time Frequency')
plt.show()
#### Create Sample Data END


#### Analyze data 
# Threshold distribution percentile
OutlierSensitivity=0.05 # Will catch extreme events that happen 5% of the time. - one sided! i.e. only late arrivals and early departures.
presetPercentile=scipy.stats.norm.ppf(1-OutlierSensitivity)

# Distribution feature and threshold percentile
argdictOverall={
	"ExpIn":SampleDF['TimeIn'].mode().mean().round(1)
	,"ExpOut":SampleDF['TimeOut'].mode().mean().round(1)
	,"sigIn":SampleDF['TimeIn'].var()
	,"sigOut":SampleDF['TimeOut'].var()
	,"percentile":presetPercentile
}
OutlierIn=argdictOverall['ExpIn']+argdictOverall['percentile']*argdictOverall['sigIn']
OutlierOut=argdictOverall['ExpOut']-argdictOverall['percentile']*argdictOverall['sigOut']

# Overall
# See all users with outliers - overall
Outliers=SampleDF["PersonID"].loc[(SampleDF['TimeIn']>OutlierIn) | (SampleDF['TimeOut']<OutlierOut)]

# See all observations with outliers - Overall
# pp.pprint(SampleDF.loc[(SampleDF['TimeIn']>OutlierIn) | (SampleDF['TimeOut']<OutlierOut)].sort_values(["PersonID"]))

# Sort and remove NAs
Outliers=np.sort(np.unique(Outliers))
# Show users with overall outliers:
print("Outlier PersonIDs based on overall data")
pp.pprint(Outliers)

# For each
OutliersForEach=[]
for Person in SampleDF['PersonID'].unique():
	# Person specific dataset
	SampleDFCurrent=SampleDF.loc[SampleDF['PersonID']==Person]
	# Distribution feature and threshold percentile
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
		Outliers=np.append(Outliers,Person)

# Sort and get unique values
Outliers=np.sort(np.unique(Outliers))
# Show users with overall outliers:
print("Outlier PersonIDs based on each user's data and overall deviation")
pp.pprint(Outliers)