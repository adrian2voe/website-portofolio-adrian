import turtle

t = turtle.Turtle()
t.speed(0)

# Merah
t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.left(90)
    t.forward(75)
    t.left(90)
t.end_fill()

t.penup()
t.goto(0, -75)
t.pendown()

# Putih
t.fillcolor("white")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.left(90)
    t.forward(75)
    t.left(90)
t.end_fill()

turtle.done()
