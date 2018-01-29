# Simple monte carlo to check the answer of the casino riddler. The game works like this: The casino draws random numbers between 0 and 1, from a uniform distribution. It adds them together until their sum is greater than 1, at which time it stops drawing new numbers. You get a payout of $100 each time a new number is drawn.

########

import numpy as np
import random 

listwinnings = []
numtries = 1000000

for i in np.arange(0,numtries):
	total = 0
	winnings = 0
	while (total <=1):
		total += random.uniform(0,1)
		winnings += 100
	listwinnings.append(winnings)

print np.mean(listwinnings)
