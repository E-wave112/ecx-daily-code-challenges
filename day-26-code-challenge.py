#compute a GPA
print('welcome to LA LA land')
def gpa_calculator(resulta, unirte, numero):
    '''
the purpose of this function is to create a functional working formula for computing
the GPA of a grad student
    '''
    #we use the dictionary data structure to write this program
    g = {0:0, 1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,
         33:0,34:0,35:0,36:0,37:0,38:0,39:0,40:1,41:1,42:1,43:1,44:1,45:2,46:2,47:2,48:2,49:2,50:3,51:3,52:3,53:3,54:3,55:3,56:3,57:3,58:3,59:3,
         60:4,61:4,62:4,63:4,64:4,65:4,66:4,67:4,68:4,69:4,70:5,71:5,72:5,73:5,74:5,75:5,76:5,77:5,78:5,79:5,80:5,81:5,82:5,83:5,84:5,85:5,86:5,87:5,88:5,89:5,90:5,
        91:5,92:5,93:5,94:5,95:5,96:5,97:5,98:5,99:5,100:5}
    #use list comprehension to convert the score grade to a dictionary value
    t = [g[s] for s in resulta]
    #use the zip function to multiply two lists together and then find their avarege using the second arguement
    produite = [i*j for i,j in zip(t,unirte)]
    aggregando = sum(produite)
    aggregate = sum(unirte)
    result = aggregando/aggregate
    return result

numero = int(input('\nenter no: '))
resulta = list(map(int, input('\nenter scores:').strip().split()))[:numero]
unirte = list(map(int, input('\nenter units: ')))
print(gpa_calculator(resulta, unirte, numero))
print('\nmoving higher!, thanks ECX')
