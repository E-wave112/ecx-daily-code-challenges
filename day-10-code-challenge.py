#les filtrer_de_eratosthenes
print('Bienvenue chez autre chalenge !')
def sieve_of_eratos(lim):
	'''
	the sieve function is created with the prime aim of returning a list of prime numbers less than the specific limiting value otherwise, the condtions are altered
	'''
	x = [2, 3, 5, 7]
	y = [i for i in range(2, lim + 1)   if i % 2 != 0 and  i % 3 != 0 and i % 5 != 0  and i % 7 !=0]
	z = x + y
	return z
	  
	  
print(sieve_of_eratos(100))
print('C\'est finit et merci')
