#Finding the Edit Distance
print('Buongiorno ! , felice pasquas !')
def find_edit_dist(w1, w2, l1, l2):
	'''
	this function is created to find the minimum number of operations that can be performed on each string to make them equal
	'''
	if l1 == 0:
		return l2
	if l2 == 0:
		return l1
	if w1[l1 - 1] == w2[l2 - 1]:
		return find_edit_dist(w1, w2, l1 - 1, l2 - 1)
	else:
		return 1 + min(find_edit_dist(w1, w2, l1, l2 - 1),                           find_edit_dist(w1, w2, l1 - 1, l2),                           find_edit_dist(w1, w2, l1 - 1, l2 - 1))
		
		
w1 = input('Enter word :')
w2 = input('Enter word :')
print(find_edit_dist(w1, w2, len(w1), len(w2)))	
