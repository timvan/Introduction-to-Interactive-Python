# http://www.codeskulptor.org/#user40_aOSKrcKRnLRgopW_4.py
# Mini-project #6 - Blackjack

# negative red - http://www.codeskulptor.org/#user41_rPrAwkQWzK_0.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]

    def __str__(self):
        hand_string = "Hand Contains:"
        for i in range(len(self.hand)):
            hand_string += " " + str(self.hand[i])
        return hand_string
        
    def add_card(self, card):
        self.hand.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        ace = False
        
        for i in range(len(self.hand)):
            c_rank = self.hand[i].get_rank()
            if c_rank == "A":
                ace = True
            hand_value += VALUES[c_rank]
        
        if ace:
            if hand_value <= 11:
                hand_value += 10              
        
        return hand_value
        
    def draw(self, canvas, pos):
        
        
        for i in range(len(self.hand)):
            
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.hand[i].rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.hand[i].suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + i*CARD_SIZE[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
        
# define deck class

class Deck:
    def __init__(self):
        
        self.deck = []
        
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        
        deck_string = "Deck Contains:"
        
        for i in range(len(self.deck)):
            deck_string += " " + str(self.deck[i])
       
        return deck_string


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer, player, score
    
    outcome = "New Deal, Hit or Stand?"
    
    deck = Deck()
    deck.shuffle()
    
    if in_play == True:
        score += -1
    
    dealer = Hand()
    player = Hand()
    
    for i in range(2):
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
    print "-" * 30
    print "\nDeal\n"
    print "Dealer's " + str(dealer) + " (" + str(dealer.get_value()) + ")"
    print "Player's " + str(player) + " (" + str(player.get_value()) + ")"
 
    in_play = True

def hit():
    
    global player, in_play, outcome, score
    
    
    if in_play:
        player.add_card(deck.deal_card())
        
        print "\nHit\n"
        outcome = "You Hit, Hit or Stand?"
        print "Player's " + str(player) + " (" + str(player.get_value()) + ")"
        

        
        if player.get_value() > 21:
            print "Bust!"
            outcome = "Bust!, Deal?"
            in_play = False
            score += -1

            
def stand():
    global player, dealer, in_play, outcome, score
   
    if in_play:
        
        outcome = "Stand"
        print "\nStand\n"
        
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
            print "Dealer's " + str(dealer) + " (" + str(dealer.get_value()) + ")"

        if dealer.get_value() > 21:
            print "Dealer Bust!"
            in_play = False
            outcome = "Dealer Bust, you WIN! Deal?"
            score += 1
        
        if in_play:
            if dealer.get_value() > player.get_value():
                print "Dealer Wins"
                outcome = "Dealer Wins, Deal?"
                in_play = False
                score += - 1
            else:
                print "Player Wins!"
                outcome = "You WIN! Deal?"
                in_play = False
                score += 1
    elif not in_play and player.get_value() > 21:
        print 'You have Busted, press "Deal"'
    

# draw handler    
def draw(canvas):
    
    global in_play, outcome, score
    # test to make sure that card.draw works, replace with your code below
    
    player.draw(canvas,[100,300])
    
    dealer.draw(canvas,[100,100])
    
    if in_play:
        card_loc = (CARD_CENTER[0], CARD_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [100 + CARD_CENTER[0], 100 + CARD_CENTER[1]], CARD_SIZE)

    canvas.draw_text(outcome, [50,50], 20, "black")
    canvas.draw_text(str(score), [400,50], 20, "red")     


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric