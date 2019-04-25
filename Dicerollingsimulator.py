import random


# making a dice rolling simulator

youranswer = ' '
print('Would you like to roll the dice?')  #asks if they want to roll the dice

while True:
    youranswer = input()
    if youranswer == 'yes':
        diceroll = random.randint(1,6)    #picks a random number between 1 and 6
        print(diceroll)                                #prints the random diceroll
        print('Would you like to roll the dice, again?')    #asks if they want to roll again
        
    elif youranswer != 'yes':     #if their answer is not 'yes' , then the loop is broken
        break

    
print('Thanks for playing!')    # prints this once the program reaches the end
    
