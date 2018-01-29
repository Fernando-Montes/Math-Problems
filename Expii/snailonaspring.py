# https://www.expii.com/solve/19/4
# A snail starts on one end of a 1-meter long elastic spring. Every minute, the snail crawls forward one centimeter and then the spring is stretched by one centimeter. How long is the spring when the snail reaches the end, in centimeters?

import numpy as np

d = 100
n = 1
# If the string were not stretching the new distance to finish after a step would be d = d-1
# Since it is stretching the different in length after every step is simply (100+n)/(99+n)
while d>0 :
	d =(100.+n)/(99.+n)*(d-1.)
	n = n + 1
	print d,n
