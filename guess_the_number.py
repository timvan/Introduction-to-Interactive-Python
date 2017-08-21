# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# http://www.codeskulptor.org/#user40_2ksaqKMa4x_0.py

import simplegui
import random
import math

range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, n
    secret_number = random.randrange(0,range-1)
    n = math.ceil(math.log(range+1)/math.log(2))
    print "\n"
    print "-" * 10
    print "New Game"
    print "Number range [0, " + str(range) + ")"
    print "You have %d guess" %n

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range=100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range=1000
    new_game()
    
def taken_guess():
    global n
    n += -1
    
    if n == 0:
        print "You ran out of guesses"
        print "The number was: %d" % secret_number
        new_game()
    else:
        print "You have %d guesses left" %n
    
def input_guess(guess):
    # main game logic goes here
    print "\n"
    print "Guess was " + guess
    guess = float(guess)


    if secret_number == guess:
        print "Correct"
        new_game()       
    elif secret_number < guess:
        print "Lower"
        taken_guess()
    else:
        print "Higher"
        taken_guess() 
        


# create frame
f = simplegui.create_frame('Guess the numer', 200, 200)

# register event handlers for control elements and start frame
guess = f.add_input('Your Guess:', input_guess, 100)
b_100 = f.add_button('Range is [0, 100)', range100, 100)
b_1000 = f.add_button('Range is [0, 1000)', range1000, 100)


# call new_game 
new_game() 


# always remember to check your completed program against the grading rubric
