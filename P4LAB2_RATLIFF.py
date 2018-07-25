import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(500)

t.pencolor("blue")

for i in range (0, 12):
    t.left(90)
    t.forward(100)
    t.forward(-40)
    t.left(40)
    t.forward(30)
    t.forward(-30)
    t.right(80)
    t.forward(30)
    t.forward(-30)
    t.left(40)
    t.forward(-60)

    t.right(60)
