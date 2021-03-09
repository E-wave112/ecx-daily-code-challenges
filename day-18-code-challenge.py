#Amicable numbers
print('salut chez un noveau chalenge')
def amicable(a, b):
    '''
the onus of the function is to determine if the sum of the proper divisors of each
arguments are the same
    '''
    e = [i for i in range(1, a + 1) if a % i ==0]
    v = sum(e)
    f = [i for i in range(1, b + 1) if b % i ==0]
    y = sum(f)
    if v == y:
        return True
    else:
        return False

    
a = int(input('enter number: '))
b = int(input('enter number: '))
print(amicable(a, b))
print('merci for aujourd\'hui, a bientot')
