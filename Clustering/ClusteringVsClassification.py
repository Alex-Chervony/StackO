import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)

# A sample Group - 3 members - with indicators
Group1=np.array([[1,3,4,5,3,3,1,1,1],[4,3,3,1,3,3,0,1,0],[4,3,3,1,3,3,0,1,0]])
mu=np.mean(Group1,axis=0)
print("Multi dimentional group center: ")
pp.pprint(mu)
print("Multi dimentional average distance from center: ")
pp.pprint(
	np.mean(
		[np.linalg.norm(mu-point) for point in Group1]
	))
