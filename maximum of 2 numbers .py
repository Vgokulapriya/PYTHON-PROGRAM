#python program to find 
#Maximum of two numbers
a=int(input("enter the number:"))
b=int(input("enter the number:"))

def maximum(a, b):
	
	if a >= b:
	   return a
	else :
	   return b
	  
print(maximum(a,b))