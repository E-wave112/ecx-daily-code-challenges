#Temperature and pressure converter
print('Bienvenue au cet pratique d\'physique ') 
def intensive_properties(N_per_sqm, K):
	'''
	the function is created as a conversion mechanism of  physical quantites from one S.I unit to another, which in this case is the pressure(N_per_sqM) and thermodynamic temperature(Kelvin)
	'''
	mmHg = 0.007500617*(N_per_sqm)
	C = K - 273
	return (mmHg, C)
#converting to our desired units;


N_per_sqm = int(input('Enter your initial pressure value:'))
K = int(input('Enter  your thermodynamic temperature: '))
print(intensive_properties(N_per_sqm, K))
print('C\'est finit et a bientôt')
