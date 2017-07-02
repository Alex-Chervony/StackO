# The sequence seems fine as long as the events are indexed in order and you are comfotable loosing events that happened at the same time but indexed differently as a result of that limitation. 
# Your algorithm in Python:
# Looks like you are dealing with time series. 
# For time series, I would suggest rolling sum or rolling weighted averages, there's an example here
# Below are some Python code samples using loops and recursion and a data sample (event indicator & epoch time stamp)

# Sample data
postingevents=[1,0,1,1,0,1]

# Algorithm:
sumofPi = 0 
ti=4
for i in range(0,ti):
	sumofPi += postingevents[i]

print(sumofPi)
	
# Data sample:
postingevents=[1,0,1,1,0,1]
postingti=[1497634668,1497634669,1497634697,1497634697,1497634714,1497634718]
postings=([postingevents,postingti])

# All events preceeding time stamp T. Events do not need to be ordered by time.
def sumpi_notordered(X,t):
	return sum([xv if yv<=t else 0 for (xv,yv) in zip(X[0],X[1])])

# Sum ordered events indexed by T, using recursion.
def sumpi_ordered(X,t):
	if t>=1:
		return X[t]+sumpi_ordered(X,t-1)
	else:
		return(X[t])

print(sumpi_notordered(postings,1497634697))
print(sumpi_ordered(postingevents,3))

# [1](https://stackoverflow.com/questions/13728392/moving-average-or-running-mean)