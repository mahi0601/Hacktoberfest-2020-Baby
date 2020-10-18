import math

def isPerfectSquare(x): 
	s = int(math.sqrt(x)) 
	return s*s == x 
def isFibonacci(n): 
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
  
for i in range(1,11): 
	if (isFibonacci(i) == True): 
		print i,"is a Fibonacci Number"
	else: 
		print i,"is a not Fibonacci Number "
