
from turtle import *
from math import floor, ceil
from .geo import perimeter, area, sin, cos 

# -------------------- My drawing functions ---------------------------

def drawCircle(radius, resolution = 360):
    """ draw a circle with the turtle environment with a given resolution

    Keyword arguments:
    radius -- the radius of the circle
    resolution -- the number of lines used to draw the circle (must be lower or equals to 360)
    """
    p = perimeter(radius)

    # The circle is drawn as a regular polygon of "resolution" sides
    for i in range(resolution):
            left(360/resolution)
            forward(p / resolution) # we accept a small error due to resolution


def fillCircle(radius, resolution = 360, borderColor = "red", fillColor = "yellow"):
    """ draw a circle filled with a given color with the turtle environment with a given resolution

    Keyword arguments:
    radius -- the radius of the circle
    resolution -- the number of lines used to draw the circle (must be lower or equals to 360)
    borderColor -- the color of the border of the circle
    fillColor -- the color used to fill the circle

    """
    color(borderColor, fillColor)
    begin_fill()
    drawCircle(radius, resolution)
    end_fill()

def drawFilledCircleOnCircle(mainRadius, nbCircles, circlesRadius, resolution = 360, borderColor = "red", fillColor = "yellow"):
    """ draw a set of colored circles around a circle shape with the turtle environment with a given resolution

    Keyword arguments:
    mainRadius -- the radius of the leading circle
    nbCircles -- the number of circles to be drawn (must be lower or equals to 360)
    radius -- the radius of the circles
    resolution -- the number of lines used to draw the circle (must be lower or equals to 360)
    borderColor -- the color of the border of the circle
    fillColor -- the color used to fill the circle

    """
    p = perimeter(mainRadius)

    for i in range(nbCircles):
        # draw a circle
        pendown()
        fillCircle(circlesRadius, resolution, borderColor, fillColor)

        # move to the next one
        penup()
        for j in range(int(360/nbCircles)) :
            left((360./nbCircles)/int(360./nbCircles)) # we must do the rounding correction automatically
            forward(p / 360.) # we accept a small error that is respect to resolution

# move to the next layer of circles
def moveToNextLayer(dist):
    penup()
    right(90)
    forward(dist)
    left(90)



reset()

# we want the turtle to go as fast as possible
delay(delay=0)

# the turtle looks to the top of the screen and moove forward of the first radius without drawing
moveToNextLayer(80)


# draw the central circle
pendown()
fillCircle(80, resolution = 45, borderColor = '#00bdeb', fillColor = '#00b0db')

# move to the first layer of circlest
moveToNextLayer(150)

# draw the circles of the first layer
drawFilledCircleOnCircle(230, 8, 30, resolution = 45, borderColor = '#009ec9', fillColor = '#0096bf')


# move to the second circumference
moveToNextLayer(150)

# draw the circles of the second layer
drawFilledCircleOnCircle(380, 16, 20, resolution = 45, borderColor = '#0087ac', fillColor = '#007fa2')

done()