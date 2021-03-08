print(' ¡ Bueno Diaz maestros y bienvenidos a un nuevo  desafio !')
#finding the sum of first n abundant numbers
def abundant(num):
	'''
	This function is created to validate if a number is abundant or not
	'''
	pd = [i for i in range(1, num + 1)  if num % i  == 0]
	total = sum(pd)
	if total > num :
		return True
	elif total < num :
		return False
		
def sum_abundant(n):
	'''
	the local function is to find the summation of the first n abundant numbers whose abundance has been specified in the first function
	'''
	y =[num for num in range(1, n + 1)  if num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9 or num == 10]
	x  = sum(y)
	if True :
		return x
	
					
print((sum_abundant(10)))
print(' ¡ Muchissimo gracias !')
