def find_7(n):
	'''
	this function is aimed to find the sum of numbers that can result in a number containing or equaling 7
	'''
	x = []
	Sec_list = [i for i in range(1, n)]
	for i in Sec_list:
		y = str(i)
		if '7' in y:
			x.append(i)
	for e in x:
		Sec_list.remove(e)
	for a in Sec_list:
		for k in Sec_list:
			while False:
				h = a + k
	return [a, k]
	
n = int(input('enter any number containing 7: '))
print(find_7(n))
