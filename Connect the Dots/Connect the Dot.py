'''
Name: Shrut
Date: 12/7/23
Purpose: This program will make you connect the dots

'''

# Importing necessary modules
import pgzrun
from random import randint

# Setting the width and height of the screen
WIDTH = 400
HEIGHT = 400

# Creating empty lists to store dots and lines
dots = []
lines = []

# Variable to keep track of the next dot to connect
next_dot = 0

# Generating 10 random dots and adding them to the dots list
for dot in range(0, 10):
    actor = Actor("bluedot.png")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

# Drawing function to display dots and lines on the screen
def draw():
    # Filling the screen with a black color
    screen.fill("black")
    number = 1

    # Drawing each dot on the screen with a number
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1

    # Drawing lines between connected dots
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

# Function to handle mouse clicks
def on_mouse_down(pos):
    global next_dot
    global lines

    # Checking if the mouse click is on the next dot
    if dots[next_dot].collidepoint(pos):
        # Checking if it's not the first dot
        if next_dot:
            # Adding a line between the current dot and the previous dot
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
    else:
        # Resetting lines and starting over if the wrong dot is clicked
        lines = []
        next_dot = 0

# Running the game
pgzrun.go()