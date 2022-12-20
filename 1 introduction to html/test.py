

import math

def primeFactors(n):

	while n % 2 == 0:
		print 2,
		n = n / 2

	for i in range(3,int(math.sqrt(n))+1,2):

		while n % i== 0:
			print i,
			n = n / i
			
	# Condition if n is a prime
	# number greater than 2
	if n > 2:
		print n
		
# Driver Program to test above function

n = 315
primeFactors(n)

# This code is contributed by Harshit Agrawal
