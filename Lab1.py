# -----------------------------------------+
# Michael Belmear                          |
# CSCI 127, Lab 1                          |
# -----------------------------------------|
# Modify an etch-a-sketch program.         |
# -----------------------------------------+

import turtle
import random

window = turtle.Screen()

pencil = turtle.Turtle()
square = turtle.Turtle()
text = turtle.Turtle()

# ---------------------------------

def draw_square():  
    square.up()
    square.speed(0)
    square.goto(-200, 200)
    square.down()
    for i in range(4):
        square.forward(100)
        square.right(90)

# ---------------------------------

def draw_text():
    text.hideturtle()
    text.up()
    text.goto(-190, 150)
    text.write("Change\nColor", font = ("Arial", 15, "bold"))
        
# ---------------------------------

def drawing_controls(x, y):
    if (-200 <= x <= -100) and (100 <= y <= 200):
        red = random.random()
        green = random.random()
        blue = random.random()
        pencil.color(red, green, blue)
        square.color(red, green, blue)
        text.color(red, green, blue)
        draw_square()
        draw_text()
        
# ---------------------------------

def main():
    pencil.shape("circle")
    square.pensize(3)
    
    square.hideturtle()
    draw_square()

    draw_text()
    
    window.onclick(drawing_controls)
    pencil.onrelease(pencil.goto)

# ---------------------------------

main()
