#Python program to find simple interest
#for given number principal amount,time 
# and rate of interest


def simple_interest(p,t,r) :
	   print('The principal is', p)
	   print('The time period is',t)
	   print('The rate of interest',r)
	   
	   si = (p*t*r)/100
	   
	   print('The simple interest is',si)
	   return si
	
#Driver code
simple_interest  (8,6,8)
