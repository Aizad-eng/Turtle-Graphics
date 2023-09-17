#Random colored Dots

import colorgram
import random
import turtle as t
from turtle import Screen

tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed(20)
t.colormode(255)

colors = colorgram.extract('image.jpg', 60)
rgb_colors = []

for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    color_tuple = (r,g,b)
    rgb_colors.append(color_tuple)

ycor=-100
number_of_horizontal_dots = 10
number_of_vertical_dots = 10

for i in range(0,number_of_vertical_dots):
    tim.setx(-200)
    tim.sety(ycor)
    ycor += 50
    for j in range(0,number_of_horizontal_dots):
        tim.dot(20,random.choice(rgb_colors))
        tim.forward(40)


screen = Screen()
screen.exitonclick()

