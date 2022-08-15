# Python program to find the factor of a number 

# This function computes the factor of the agument passed 
def print_factors(x) :
	print("The factor of",x,"are:")
	for i in range(1,x+1) :
		if x % i == 0:
			print(i)
			
num=int(input())
print_factors(num)			