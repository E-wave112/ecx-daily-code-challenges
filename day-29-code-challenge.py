##keylogger-like code task that prints out the number of key presses corresponding to tye number pressed to get each character of the text
def text_messaging(text):
	
	letter_conv = []
	##character-key dict
	msg_dict = {
	 ' ':'0' , '.':'1', ',':'1'*2, '?':'1'*3, '!':'1'*4,':':'1'*5,
	 'A':'2','B':'2'*2,'C':'2'*3, 'D':'3','E':'3'*2,
	 'F':'3'*3,'G':'4','H':'4'*2,'I':'4'*3,
	 'J':"5",'K':'5'*2,'L':'5'*3,
	 'M':'6','N':'6'*2,'O':'6'*3,
	 'P':'7','Q':'7'*2,'R':'7'*3,'S':'7'*4,
	 'T':'8','U':'8'*2,'V':'8'*3,'W':'9',
	 'X':'9'*2,'Y':'9'*3,'Z':'9'*4
	}
	##generalize the text by converting to uppercase
	texts = text.upper()
	for letter in texts:
		letter_conv.append(msg_dict[letter])
		
	return ''.join(letter_conv)
	
print('*'*30)
print('*'*30)
print(text_messaging("Hello World!"))
print('*'*30)
print('*'*30)
