#the infinite hotel paradox
print('buongiorno!')
def captains_room(room_number):
    '''
    the function is aimed at finding a unique room number from an array of rooms in an on end hotel
     '''
    room_number = {1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5,
               6, 2}
    for i in room_number:
        if True:
            if i != 8 :
                return False
            else:
                return True


room_number = int(input('enter your room_no: '))
print(captains_room(room_number))
print('bravo per oggi, ci vediamo dopo!')
