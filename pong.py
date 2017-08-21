# Pong 
# http://www.codeskulptor.org/#user40_1e8STtsdCI_4.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
time = 0
paddle1_pos = [HALF_PAD_WIDTH,HEIGHT/2]
paddle2_pos = [WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
paddle1_vel = 0
paddle2_vel = 0
time_modifier = 1
score = [0, 0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, time
    ball_pos = [WIDTH/2, HEIGHT/2]
    time = 0
    if direction == "LEFT":
        ball_vel = [-random.randrange(3, 6), - random.randrange(1, 3)]
    elif direction == "RIGHT":
        ball_vel = [random.randrange(3, 6), - random.randrange(1, 3)]
    else:
        pass
    
    
def ball_collision():
    global ball_pos, ball_vel
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    else:
        return

# define event handlers 
    
def new_game(direction):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score  # these are numbers
    spawn_ball(direction)
    
def timer_handler():
    global time
    time += 1
    
def draw(canvas):
    global score, paddle1_pos, paddle2_pos, ball_pos, ball_vel, time
    
    time_modifier = 1.0 + float(time/100.0)
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_collision()    
    
    ball_pos[0] += ball_vel[0] * time_modifier
    ball_pos[1] += ball_vel[1] * time_modifier
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    
    if paddle1_pos[1] + paddle1_vel * time_modifier <= 0 + HALF_PAD_HEIGHT:
        paddle1_pos[1] = 0 + HALF_PAD_HEIGHT   
    elif paddle1_pos[1] + paddle1_vel * time_modifier >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle1_pos[1] += paddle1_vel * time_modifier
    
    if paddle2_pos[1] + paddle2_vel * time_modifier <= 0 + HALF_PAD_HEIGHT:
        paddle2_pos[1] = 0 + HALF_PAD_HEIGHT
    elif paddle2_pos[1] + paddle2_vel * time_modifier >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle2_pos[1] += paddle2_vel * time_modifier 
    
    # draw paddles
    
    canvas.draw_polygon([(0, paddle1_pos[1] - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT),
                         (PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT), (0, paddle1_pos[1] + HALF_PAD_HEIGHT)],
                         1 , 'White', 'WHITE')
                         
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT),
                         (WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT)],
                        1 , 'White', 'WHITE')
    
    # determine whether paddle and ball collide    
    
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT:
            pass
        else:
            score[0] += 1
            new_game("LEFT")
    
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT:
            pass
        else:
            score[1] += 1
            new_game("RIGHT")
    
    # draw scores
    
    canvas.draw_text(str(score[0]) + ":" + str(score[1]), (WIDTH/2 -36, 40), 40, "White", "monospace")
    
    if ball_vel == [0, 0]:
        canvas.draw_text("press space to start", (WIDTH/2 -60, 60), 10, "White", "monospace")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    pad_vel = 4
    
    if chr(key) == "&":
        paddle2_vel = -pad_vel
    elif chr(key) == "(":
        paddle2_vel = pad_vel
    elif chr(key) == "W":
        paddle1_vel = -pad_vel
    elif chr(key) == "S":
        paddle1_vel = pad_vel
    elif chr(key) == " ":
        if ball_vel == [0, 0]:
            new_game(random.choice(['LEFT','RIGHT']))
    else:
        return

def keyup(key):
    global paddle1_vel, paddle2_vel

    if chr(key) == "&":
        paddle2_vel = 0
    elif chr(key) == "(":
        paddle2_vel = 0
    elif chr(key) == "W":
        paddle1_vel = 0
    elif chr(key) == "S":
        paddle1_vel = 0
    else:
        return

def reset_button():
    global score
    score = [0, 0]
    new_game(random.choice(['LEFT','RIGHT']))
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button_reset = frame.add_button('Restart', reset_button, 60)

timer = simplegui.create_timer(100, timer_handler)

# start frame
timer.start()
frame.start()
