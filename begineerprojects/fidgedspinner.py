from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(80, 'violet')
    back(100)
    right(51.42)
    forward(100)
    dot(80, 'indigo')
    back(100)
    right(51.42)
    forward(100)
    dot(80, 'blue')
    back(100)
    right(51.42)
    forward(100)
    dot(80, 'green')
    back(100)
    right(51.42)
    forward(100)
    dot(80, 'yellow')
    back(100)
    right(51.42)
    forward(100)
    dot(80, 'orange')
    back(100)
    right(51.42)
    forward(100)
    dot(80, 'red')
    back(100)
    right(51.42)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()