#The Fibonacci sequence, as named after the Italian mathematician Leonardo Fibonacci
print('Benevuti uno di nuovo !')
def fibonacci(n):
	'''
	the function is created to locate the position of a fibonacci term in the fibonacci sequence
	'''
	if n < 0:
		return 'fib doesn\'t accept negative'
#since the first two fibonacci numbers are 0, 1 ; we make them base values
	elif n == 1:
		return 0
	elif n == 2:
		return 1
#to get other fibonacci numbers, we use recursio s
	elif n > 2 :
		return fibonacci(n - 1) + fibonacci(n - 2)
		
n = int(input('enter term: '))		
print(fibonacci(n))
print('Arriverderci !')
