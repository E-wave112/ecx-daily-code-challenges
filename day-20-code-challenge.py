print('Měihǎo de yītiān de yīnyì !')
#Lingual number conversion
def to_mandarin(num):
	'''
	the aim of the function is to convert an arabic numeral to a mandarin number
	'''
	constants = { 1 : 'yi', 2 : 'er', 3 : 'san', 4 : 'si',
	5 : 'wu', 6 : 'liu', 7 : 'qi', 8 : 'ba', 9 : 'jiu', 10: 'shi'}
	
	if num in range(11, 20):
		y = constants[10]  + constants[num - 10]
		return y
	if num in range(20, 100):
		if j == str(0):
			z = constants[int(i)] + constants[10]
			return z
	if num in range(20, 100):
		x = constants[int(i)] +   constants[10] +  constants[int(j)]
		return x
		
		
i = input('enter logic1: ')
j = input('enter logic2: ')	
num = int(i + j)
print(to_mandarin(num))
print(' Xièxiè nǐ de yīnyì ! ')
