import random
import numpy as np

# Monte Carlo to calculate the average smallest distance between 3 points 
# randomly placed in a line of lenght 1
vals = []
for i in np.arange(0,10001):
	dists, pts = [], []
	for j in np.arange(0,3):
		pts.append(random.uniform(0,1))
	pts.sort()
	dists.append(pts[2]-pts[1])
	dists.append(pts[1]-pts[0])
	dists.sort()
	vals.append(dists[0])
print "MC answer = " + str(np.mean(vals))
print "Correct answer = " + str(1./8.)
