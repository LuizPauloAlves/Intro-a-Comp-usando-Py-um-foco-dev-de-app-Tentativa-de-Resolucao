import turtle
s = turtle.Screen()
t = turtle.Turtle()
j = -150
t.penup()
t.goto(-200,-200)
t.pendown()
for i in range(5):
    for i in range(5):
        t.left(144)
        t.forward(100)
    t.penup()
    j += 100
    t.goto(j,j)
    t.pendown()
t.penup()
t.goto(0,-200)
t.pendown()
for i in range(3):
    t.left(120)
    t.forward(100)
t.penup()
t.goto(0,-150)
t.pendown()
for i in range(3):
    t.left(-120)
    t.forward(100)