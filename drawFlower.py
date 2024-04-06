import random
from turtle import *
from turtleCircles import *

def random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


# --------------------- Draw the flower ----------------------------
# reset the turtle state
reset()

# we want the turtle to go as fast as possible
delay(delay=0)
reset()

moveToNextLayer(400)

# the turtle look to the top of the screen and moove forward of the first radius without drawing
for i in range(10):
    fillCircle(200 - i * 20, resolution = 90, borderColor = random_color(), fillColor = random_color())
    moveToNextLayer(32)
    drawFilledCircleOnCircle(250 + i * 20, 16, 15, 90, borderColor = random_color(), fillColor = random_color())
    moveToNextLayer(-32)


done()
