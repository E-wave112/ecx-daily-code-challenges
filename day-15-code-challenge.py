#Reversing the lines and characters in a text file
lyrics_file = open('lira for ecx.py', 'r+')
#opens  the file in a readable and appendable format and then then prints it out
for i in lyrics_file.readlines():
    print(i)
#splitting each character
words = i.split(' ')
#each character been reversed
delta = [letter[::-1] for letter in words]
#then joined together to form a new set of lras
new_id = ''.join(delta)
print(new_id)
lyrics_file.close()
