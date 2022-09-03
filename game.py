#####################################################
# interface for the Riddler, a riddle guessing game
# ----------
# it's up to you to finish it!
# feel free to customize it as you please.
######################################################

# Imports a list of Riddle objects from riddle.py
from riddle import riddles

def game_loop():
    '''This function runs the game.'''

    print("-"*35)
    print("---- Welcome to the Riddler ----")
    print("-"*35,"\n")

    for riddle in riddles:
        print(riddle.prompt)
        guess = input('> ')

        if riddle.check_guess(guess):
            print('Correct!')

        else:
            print('Incorrect!')
    
        print()

if __name__=='__main__':
    game_loop()