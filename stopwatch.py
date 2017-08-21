# template for "Stopwatch: The Game"
# # template for "Stopwatch: The Game"

import simplegui
import math

# define global variables

time_text="00:00.0"
lap_text = "Lap: 00:00.0"
play_wins = "0/0"
count = 0
plays = 0
wins = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time_text, milli_seconds
    milli_seconds = count % 10
    
    seconds = (( count - milli_seconds) / 10) % 60
    ones_seconds = seconds % 10
    tens_seconds = (seconds - ones_seconds) / 10
    
    minutes = (( count - milli_seconds) / 10) / 60 
    ones_minutes = minutes % 10  
    tens_minutes = (minutes - ones_minutes) / 10
    
    time_text= str(tens_minutes) + str(ones_minutes) + ":" \
             + str(tens_seconds) + str(ones_seconds) + "." \
             + str(milli_seconds)

    
# define event handlers for buttons; "Start", "Stop", "Reset"

def play_game():
    global milli_seconds, time_text, plays, wins, play_wins
    
    if not timer.is_running():
        return
    elif milli_seconds == 0:
        wins +=1
        plays +=1
    else:
        plays +=1
    
    play_wins = str(wins) + "/" + str(plays)

def stop():
    play_game()
    timer.stop()

def start():
    timer.start()

def reset():
    global count, time_text, lap_text, plays, wins, play_wins
    count = 0
    time_text = "00:00.0"
    lap_text = "Lap: 00:00.0"
    plays = 0
    wins = 0
    play_wins = "0/0"
    
def lap():
    global time_text, lap_text
    lap = time_text
    lap_text = "Lap: " + lap
    
def key_handler(key):
    if chr(key) == " ":
        if timer.is_running():
            stop()
        else:
            start()
    elif chr(key) == "R":
        reset()
    elif chr(key) == "L":
        lap()
    else:
        return

# define event handler or timer with 0.1 sec interval

def timer_handler():
    global count
    count += 1
    format(count)
    
# define draw handler

def draw(canvas):
    canvas.draw_text(time_text, (75, 100), 20, 'White')
    canvas.draw_text(lap_text, (32, 130), 20, 'White')
    canvas.draw_text(play_wins, (160,30), 20, 'Red')
    
# create frame

frame = simplegui.create_frame('Stopwatch', 200, 200)
button_start = frame.add_button('Start', start, 50)
button_stop  = frame.add_button('Stop', stop, 50)
button_reset  = frame.add_button('Reset', reset, 50)
button_lap = frame.add_button('Lap', lap, 50)
frame.set_keydown_handler(key_handler)



# register event handlers

frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

# start frame

frame.start()


# Please remember to review the grading rubric
