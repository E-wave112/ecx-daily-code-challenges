#Validating Nigeria Phone Numbers
print('bienvenidos alla otenticacionnes de numeras del Nigerià')
def is_Nigerian(code):
	'''
	The function is created to verify contact numbers if it is Nigerian or otherwise
	'''
	if num.startswith('+234') and len(num) ==14:
		return '\nTrue'
	elif  num.startswith('+234') and len(num) != 14:
		return '\nthe code is Nigerian but the number is wrong or probably you didn\'t count your digits well'
	elif not num.startswith('+234') and len(num) == 14:
		return '\nwrong country code, correct count; are you sure you\'re in the right country?'
	elif not num.startswith('+234') and len(num) !=14:
		return '\nAlexa, can you give this guy the right coordinates?, apparently he doesn\'t know where he is !'


num = input('\nEnter Number :')
print(is_Nigerian(num))
print('\n¿espero que tu disfrutas este practico?, ten cuidate y adios')
