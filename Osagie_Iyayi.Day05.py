#faithful numbers
print('ciao!')
def faithful(n):
    """
this function is aimed at locating the integer position of a faithful number
   """
    n > 0
    x = str(int(bin(n)[2:]))
    y = x[::-1]
    f = 0
    for i in y:
        t = int(i)*7**f
        f += t
    return f            

n = int(input('enter number: '))
print(faithful(n))
print('molto grazie, ci vediamo dopo!')
