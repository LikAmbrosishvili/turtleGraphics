import turtle

def draw_star(size):
    window = turtle.Screen()
    window.bgcolor("white")

    star = turtle.Turtle()
    star.speed(1)
    for i in range(5):
        star.forward(size)
        star.right(144)  # Angle to turn to create a star

    window.exitonclick()

draw_star(100)  # Draw a star with each side of length 100 units
