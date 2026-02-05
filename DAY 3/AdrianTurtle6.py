import turtle

def drawRectangle(ttl, x, y, width, height):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.penup()

def drawTriangle(ttl, x1, y1, x2, y2, x3, y3):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)
    ttl.penup()

def fillTriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    drawTriangle(ttl, x1, y1, x2, y2, x3, y3)
    ttl.end_fill()

# Setup screen
turtle.setup(1500, 1000)
screen = turtle.Screen()

# Colors (HEX)
myBlue = "#003882"
myYellow = "#FCD647"
myRed = "#D12421"
myGreen = "#007336"
myWhite = "#FFFFFF"

Joe = turtle.Turtle()
Joe.speed(0)

# Rectangle background
drawRectangle(Joe, 0, 300, 600, 300)

# Triangles (flag design)
fillTriangle(Joe, 0, 0, 300, 200, 300, 300, myBlue)
fillTriangle(Joe, 0, 0, 200, 300, 400, 300, myYellow)
fillTriangle(Joe, 0, 0, 400, 300, 600, 300, myRed)
fillTriangle(Joe, 0, 0, 600, 300, 600, 150, myWhite)
fillTriangle(Joe, 0, 0, 600, 150, 600, 0, myGreen)

Joe.hideturtle()

# Save to EPS
ts = turtle.getscreen()
tc = ts.getcanvas()
tc.postscript(file="SeychellesFlag.eps")

turtle.done()
