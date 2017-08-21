# Rock-paper-scissors-lizard-Spock template
# http://codeskulptor-user40.commondatastorage.googleapis.com/user40_PnlLCJxZEb_3.py
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    # convert name to number given catagorisation
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print " Error with name input"
    return number

def number_to_name(number):
    #convert number to corresponding name
    name_list = ["rock", "Spock", "paper", "lizard", "scissors"]
    name = name_list[number]
    return name
    

def rpsls(player_choice): 

    # print a blank line to separate consecutive games
    print "\n"
    
    # print out the message for the player's choice
    print "Human chooses " + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if diff > 0 and diff <=2:
        print "Computer Wins!"
    elif diff >2 and diff <=4:
        print "Human Wins!"
    elif diff == 0:
        print "PLayer and computer tie!"
    else:
        print "Error playing"
        
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
