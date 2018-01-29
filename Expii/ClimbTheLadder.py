# https://www.expii.com/solve/1/5
# Oh no! You are above a pit of fire and the only way out is a 1000-rung escape ladder. Every second, a standard (6 sided) die rolls. If it is a 1 or 2, you move down one rung. Anything 3 or greater, you move up one rung. If you move down from the first rung, you fall into the fire! If you move up from the 1000th rung, you escape.
# What is the probability that you escape?

########

import numpy as np
import random 

scape = []
numtries = 100000

for i in np.arange(0,numtries):
	step = 1
	while (step!=0 and step!=1001):
		if (random.uniform(0,1)>1/3.) :
			step = step + 1
		else :
			step = step - 1
	if step==0:
		success = 0
	else:
		success = 1
	#print step
	scape.append(success)

print np.sum(scape)/float(numtries)
