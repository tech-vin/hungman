#import modules
import random

#functions
def hungman():

    # predefine lists
    word = random.choice(['LION', 'BEAR', 'HORSE', 'MULE', 'CROCODILE', "RACOON" , "FOX" , "SKUNK" , "HIPPOPOTAMUS" , "JAGUAR"])
    validLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turns = 10
    guessmade = ''

    # instructions
    while len(word) > 0:
        main = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main += letter
            else:
                main+= '_' + ' '
       
        # check the word
        if main == word:
            print(main)
            print('You win!')
            break
        
        print('Guess the word: ', main)
        guess = input().upper()

        if guess in validLetters:
            guessmade += guess
            
        else:
            print('invalid input')
            guess = input().upper()

        #reduce the turn
        if guess not in word:
            turns -= 1
        print('\n') 
        print('Failed! Attempt left:', turns)
        

        #print the gesture
        if turns == 9:
            print("  --------  ")

        if turns == 8:            
            print("  --------  ")
            print("     O      ")

        if turns == 7:
            print("  --------  ")
            print("     O      ")
            print("     |      ")

        if turns == 6:
            print("  --------  ")
            print("     O      ")
            print("     |      ")
            print("    /       ")

        if turns == 5:
            print("  --------  ")
            print("     O      ")
            print("     |      ")
            print("    / \     ")

        if turns == 4:
            print("  --------  ")
            print("   \ O      ")
            print("     |      ")
            print("    / \     ")

        if turns == 3:
            print("  --------  ")
            print("   \ O /    ")
            print("     |      ")
            print("    / \     ")

        if turns == 2:
            print("  --------  ")
            print("   \ O / |  ")
            print("     |      ")
            print("    / \     ")

        if turns == 1:
            print("Last breaths counting, Take care!")
            print("  --------  ")
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")

        if turns == 0:
            print("You loose")
            print("You let a kind man die")
            print("  --------  ")
            print("     O_|    ")
            print("    /|\     ")
            print("    / \     ")
            break


# main interface

name = input('Enter Name: ')
print('Welcome', name)
print('---'*5)
print('Try to guess the animal name in less than 10 attempts.')
hungman()
print()
