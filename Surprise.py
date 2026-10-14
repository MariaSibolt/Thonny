import turtle
import math

# Heart shape equations
def syda1(k):
    return 15 * math.sin(k) ** 3

def syda2(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Setup turtle screen
window = turtle.Screen()
window.setup(800, 600)
window.bgcolor("black")
window.tracer(0, 0)  # Turn off auto-drawing for speed

# Setup turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

# Draw the heart efficiently
for i in range(600):
    # Normalize i to radians between 0 and 2π
    k = i * math.pi * 2 / 600
    x = syda1(k) * 20
    y = syda2(k) * 20

    pen.goto(x, y)

    # Color animation
    r = abs(math.sin(i / 30))
    g = abs(math.sin(i / 20))
    b = abs(math.sin(i / 10))
    pen.pencolor(r, g, b)

    pen.pendown()

# Finish drawing the heart
pen.penup()

# Write text below the heart
pen.goto(0, -250)
pen.color("white")
pen.write("I love you!", align="center", font=("Arial", 24, "normal"))

# Write second message slightly below the first
pen.goto(0, -260)
pen.write("Hope this makes you feel better <3", align="center", font=("Satisfy", 13, "normal"))

# Update screen once at the end
window.update()

# Keep the window open
turtle.done()