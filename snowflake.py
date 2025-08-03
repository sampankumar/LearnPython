import turtle
from turtle import Screen

window3 = Screen()
t = turtle.Turtle()
t.speed(7)
t.pencolor("white")
t.pensize(6)
window3.bgcolor("cyan")
def vshape():
    t.right(25)
    t.forward(50)
    t.backward(50)
    t.left(50)
    t.forward(50)
    t.backward(50)
    t.right(25)
def arm():
    for i in range(0,4):
        t.forward(20)
        vshape()
    t.backward(80)
def snowflake():
    for x in range(0,6):
     arm()
     t.right(60)
snowflake()

window3.exitonclick()
