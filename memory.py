# http://www.codeskulptor.org/#user40_XafP3nf8T6NHUiT_7.py
# implementation of card game - Memory

import simplegui
import random

L_x = 100
L_y= 1.4 * L_x
card_size = [L_x, L_y]
bord = 5

card_x = 10
card_y = 1

frame_size = [card_size[0] * card_x, card_size[1] * card_y]


# helper function to initialize globals
def new_game():  
    global state, turns, exposed, card_list, card_last, card_last2, card_x, card_y
    state = 0
    turns = 0
    
    num_cards = card_x * card_y
    exposed = [False]*card_x*card_y

    card_last = [None, None]
    card_last2 = [None, None]
    
    card_list = range(1, num_cards // 2 + 1) + range(1, num_cards // 2 + 1)
    random.shuffle(card_list)
    label.set_text("Turns = " + str(turns))

    
def add_pairs():
    global card_x, card_y, num_cards
    
    card_y += 1
    
    frame_size = [card_size[0] * card_x, card_size[1] * card_y]
    frame = simplegui.create_frame("Memory", frame_size[0], frame_size[1])
    frame.add_button("Reset", new_game)
    label = frame.add_label("Turns = 0")
    frame.add_button("Add Pairs", add_pairs)
    frame.add_button("Reduce Pairs", reduce_pairs)
    frame.set_mouseclick_handler(mouseclick)
    frame.set_draw_handler(draw)
    new_game()
    frame.start()

     
def reduce_pairs():
    global card_x, card_y, num_cards
    
    if card_y > 1:
        card_y -= 1
    
    frame_size = [card_size[0] * card_x, card_size[1] * card_y]
    frame = simplegui.create_frame("Memory", frame_size[0], frame_size[1])
    frame.add_button("Reset", new_game)
    label = frame.add_label("Turns = 0")
    frame.add_button("Add Pairs", add_pairs)
    frame.add_button("Reduce Pairs", reduce_pairs)
    frame.set_mouseclick_handler(mouseclick)
    frame.set_draw_handler(draw)
    new_game()
    frame.start()
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, card_last, card_last2, turns, card_list, card_x, card_y

    if pos[0] % L_x > bord and pos[0] % L_x < L_x-bord:
        if pos[1] % L_y > bord and pos[1] % L_y < L_y-bord:
            x_e = pos[0] // L_x
            y_e = pos[1] // L_y

            if exposed[x_e + (y_e * card_x)]:
                pass
            
            else: 
                exposed[x_e + (y_e * card_x)] = True
                
                if state == 0:
                    card_last2 = list(card_last)
                    card_last = [x_e, y_e]  
                    state = 1
                
                elif state == 1:
                    if card_list[card_last[0] + (card_last[1] * card_x)] == card_list[x_e + (y_e * card_x)]:
                        turns += 1
                        card_last2 = [None, None] 
                        card_last = [None, None] 
                        state = 0
                    else:
                        card_last2 = list(card_last)
                        card_last = [x_e, y_e]  
                        state = 2
                        turns += 1
                else:
                    exposed[card_last2[0] + (card_last2[1] * card_x)] = False
                    exposed[card_last[0] + (card_last[1] * card_x)] = False
                    state = 1
                    card_last2 = [None, None] 
                    card_last = [x_e, y_e] 
                            
                label.set_text("Turns = " + str(turns))
    
                
                    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    for x in range(card_x):
        for y in range(card_y):
                canvas.draw_polygon(
                    [[bord + x*L_x, bord + y*L_y], 
                    [card_size[0]-bord + x*L_x, bord + y*L_y], 
                    [card_size[0]-bord + x*L_x, card_size[1]-bord + y*L_y],
                    [bord + x*L_x, card_size[1]-bord + y*L_y]],
                    2, "Red", "White")
    
    for x in range(card_x):
        for y in range(card_y):
            if card_list[x + (y * card_x)] > 9:   
                canvas.draw_text(str(card_list[x + (y * card_x)]),
                             (L_x*(x + 0.22), L_y*(y + 0.55)),
                             50, "Black")
            else:
                canvas.draw_text(str(card_list[x + (y * card_x)]),
                             (L_x*(x + 0.35), L_y*(y + 0.55)),
                             50, "Black")
    
    for x in range(card_x):
        for y in range(card_y):
            if not exposed[x + (y * card_x)]:
                canvas.draw_polygon(
                    [[bord + x*L_x, bord + y*L_y], 
                    [card_size[0]-bord + x*L_x, bord + y*L_y], 
                    [card_size[0]-bord + x*L_x, card_size[1]-bord + y*L_y],
                    [bord + x*L_x, card_size[1]-bord + y*L_y]],
                    2, "White", "Red")



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", frame_size[0], frame_size[1])
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

frame.add_button("Add Row", add_pairs)
frame.add_button("Reduce Row", reduce_pairs)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric