#decryption exercise
print('welcome to elementary blockchain')
def decryptor(text):
	k = int(input('enter key: '))
	dcrypt = ""
	char = ""
	for i in range(len(text)):
		char = text[i]
		n = ord(char)
		if (char.isupper()):
			crypt1 = chr((n + k - 65) % 26 + 65)
			dcrypt += crypt1
		elif(char.islower()):
			crypt2 = chr((n + k - 97) % 26 + 97)
			dcrypt += crypt2
			fin = ' '.join(dcrypt)
	return fin
			
			
text = input('Enter Text: ')
print(decryptor(text))
print('end of chain, looking forward to more crypts')
