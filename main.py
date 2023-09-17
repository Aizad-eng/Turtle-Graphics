#Random Walk with Turtle Graphics

import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

angles = [0, 90, 180, 360]
tim.pensize(20)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

while True:
    tim.speed(20)
    tim.hideturtle()
    tim.color(random_color())
    tim.setheading(random.choice(angles))
    tim.forward(50)



screen = Screen()
screen.exitonclick()
