#Power List Generator
'''
The function is created to find the maximum number of local list that can be formed from the global list
'''
print('Buenos Diaz, Commencar')
import math;   
def printPowerSet(set,set_size): 
    pow_set_size = (int) (math.pow(2, set_size)); 
    counter = 0
    j = 0
    for counter in range(0, pow_set_size): 
        for j in range(0, set_size):   
            if((counter & (1 << j)) > 0): 
                print(set[j], end = "")
        print("")

set = list(input('enter your set list: '))
set_size = int(input('Enter your set_size :'))
printPowerSet(set, set_size); 
print('¡ Gracias por hoy, Luego !')
