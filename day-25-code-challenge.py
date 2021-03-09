#describe the triangle and compute it's area
print('Toûts d\'vous etez bienvenue au le triangle')
def desc_triangle(a, b, c):
	'''
	this mathematical function is created to describe what type of triangle we created based on the sides and also compute it's area
	'''
#we starting by stating a general formula for the area of a triangle using hero's formula
	s = (a + b + c)/2
	inter_val = s*(s-a)*(s-b)*(s-c)
	A = inter_val**0.5
	if type(A) == complex:
		return 'Undefined !, this is not even a shape, not to talk of triangle'
	if a == b and b == c and a ==c:
		return ('Equilateral Triangle', A)
	if a**2 == b**2 + c**2 and b != c :
		return ('Rightangled Triangle', A)
	if a**2 == b**2 + c**2 and b == c:
		return ('Right angled isosceles triangle', A)
	if a**2 != b**2 + c**2 and b != c:
		return ('Scalene Triangle', A)
	if a**2 != b**2 + c**2 and b ==c:
		return ('Isosceles Triangle', A)
		
		
a = float(input('Enter longest Side:'))
b = float(input('Enter intermediate side: '))
c = float(input('Enter shortest side: '))
print(desc_triangle(a, b, c))
print('Merci une fois encore et un amour ECX !')
