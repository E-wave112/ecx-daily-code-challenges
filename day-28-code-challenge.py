print('¡ la datos de magico !')
m_d = {

'January':[1,31], 'February':[2,28], 'March':[3,31],
	'April':[4,30], 'May':[5,31], 'June':[6,30],'July':[7,31],
	'August':[8,31],'September':[9,30], 'October':[10,31],'November':[11,30], 'December':[12,31]
	
	}

def magic_date(m,d,y):
	#users enter the month in full form,date and year and determine if it is a magic date or not

	##make necessary exceptions& aasertions
	assert type(m) == str and type(d) == int and type(y) == str
	
	if not m in m_d.keys():
		raise ValueError('invalid month, make sure you\'re entering the correct month in the full(not abbreviated ) format')
		
		
	if d not in range(1,m_d[m][1] + 1):
		raise ValueError('invalid day')
	
	if m_d[m][0] * d == int(y[-2:]):
		return True
	else:
		return False
			
			
def count_magic(y):
	##returns only the magic dates in the given year
	assert type(y) == str and len(y) == 4
	
	for i in m_d:
		z = ''.join([ str(j) for j in range(1,m_d[i][1]+ 1)if j * m_d[i][0] == int(y[-2:]) 
	]+ [' ',i,' ',y])
		print(z)

##test cases
print('=========')
count_magic('1960')
print(magic_date('February',20,'1960'))##False
print(magic_date('December',1,'2012'))##True
