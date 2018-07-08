import turtle

DIST = 100
for x in range(0,6):
    print "x", x
for y in range(1, 5):
    print "y", y

turtle.right(90)
turtle.forward(DIST)
turtle.left(90)
turtle.forward(DIST)
turtle.left(90)
turtle.forward(DIST)
turtle.left(90)
turtle.forward(DIST)

DIST += 20