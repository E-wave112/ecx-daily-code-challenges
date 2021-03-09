#Finding an Array of Armstrong Numbers
print('Welcome to the Armstrongs !')
def Armstrong(n):
	'''
	this function is created to find armstrong numbers(numbers whose sum of  cubed digits yields the number)
	'''
#convert the integer to string to make it iterable
	y = str(n)
	t = y[0]
	u = y[1]
	v = y[2]
#from the indexes, we see that our range for n is between 100 and 1000
#recomverting the strings to integers;
	a = int(t)
	b = int(u)
	c = int(v)
	if n == a**3 + b**3 + c**3:
		return n
	else:
		return False
#we then create a function to evaluate our final program
def find_armstrong(x, y):
	'''
	this inner function is created to find the armstrong numbers within a specified range
	'''	
	fin = [Armstrong(i) for i in range(x, y)]
	fin = list(dict.fromkeys(fin))
	fin.remove(False)
	return fin


Arm_output = find_armstrong(100, 1000)		
print(Arm_output)
print('Hope it was worthwhile, hopefully i will get to program Aldrin Numbers !')
