#finding the greatest common divisor between numbers
print('Joyeux Chalengé')
def gcd(n, m):
	'''
	this function is created on the basis of finding the greatest number that can divide the two numbers in our input parameter
	'''
	#using list comprehension
	p = [i for i in range(1, n +1) and range(1, m + 1) if (n % i == m % i) ]
	#we then obtain the highest common value using the maximum notation
	d = max(p)
	return d
	
	
n = int(input('\nenter first number\n :'))
m = int(input('\nenter second number :'))
print(gcd(n,m))
print('\nmerci, encore; a bientôt')
