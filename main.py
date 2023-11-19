import random
import turtle
from turtle import Screen, Turtle
from random import choice

tim = Turtle()

#Colours
turtle.colormode(255)
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colour = (r, g, b)

    return colour

#Turtle Properties
tim.shape("turtle")
tim.color("red")

#Pen
tim.pendown()
tim.pensize(2)

#Angle


#Motion
turtle.speed("fastest")
for i in range(0, 360, 5):
    tim.color(random_colour())
    tim.setheading(i)
    tim.circle(100)

screen = Screen()
screen.exitonclick()