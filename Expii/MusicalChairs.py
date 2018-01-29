# https://www.expii.com/solve/5/5
# You are playing the biggest game of musical chairs ever, with 6,469,693,230 chairs. The rules are a little different: an integer D is uniformly and randomly selected from 1 to 6,469,693,230 (inclusive) and when the music starts, everyone moves D chairs to their left, then another D chairs, then another, on and on, forever. What is the expected number of unique chairs that you will sit in during this game? Note that for some values of D, you will not be able to reach every chair. For example, if D=2, you can only sit in half the chairs.

import numpy as np 
from fractions import gcd

#n = 6469693230
n = 2*3*5*7*11*13*17*19*23*29
res = 0
for i in np.arange(1,n+1):
	res = res + 1./gcd(i,n)	
print res

