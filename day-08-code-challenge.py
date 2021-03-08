#hangman game
print('salut!')
def hangman(word, guessnum):
    """
the function is targeted at counting the number of times a user can guesstimate the number of letters in a word
    """
    for t in range(1, guessnum+1):
        if True:
            guessletter = input('enter guessletter :')
            for guessletter in range(1, guessnum+1):
                if True:
                    if i in word:
                        if guessletter == i in word:
                            return i
                        else:
                            return '_'



guessnum = int(input('enter number of trials: '))
word = input('enter word: ')
print(hangman(word, guessnum))
print('a bientot')
