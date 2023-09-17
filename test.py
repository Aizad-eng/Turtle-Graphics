#Spirograph with Turtle Graphics
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
heading = 1
tilt = 0
tim.speed(20)
heading = 5

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

while True:
    tim.pensize(10)
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(heading)
    heading+=5


screen = Screen()
screen.exitonclick()
