# Interactive Fractal Tree

import turtle
import math
import random

def draw_branch(t, length, angle, depth, max_depth):
    if depth == 0:
        return
        
    # Change color based on depth
    change_color_by_depth(t, depth, max_depth)

    # Draw the current branch  
    t.forward(length)

    # Save current position and heading
    pos = t.position()
    heading = t.heading()

    # Draw left branch
    t.left(angle)
    new_length = length * (0.7 + random.uniform(-0.1, 0.1))
    draw_branch(t, new_length, angle * 0.8, depth - 1, max_depth)

    # Draw right branch
    t.setposition(pos)
    t.setheading(heading)
    t.right(angle)
    new_length = length * (0.7 + random.uniform(-0.1, 0.1))
    draw_branch(t, new_length, angle * 0.8, depth - 1, max_depth)

    # Return to previous position and heading
    t.setposition(pos)
    t.setheading(heading)

def setup_turtle():
    t = turtle.Turtle()
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    return t

def change_color_by_depth(t, depth, max_depth):
    # color gradient brown at bottom green at top
    ratio = depth / max_depth
    if ratio < 0.3:
        t.pencolor("saddlebrown")
    elif ratio < 0.6:
        t.pencolor("darkgreen")
    else:
        t.pencolor("limegreen")

def main():
    print("Welcome To The Fractal Tree Generator!")
    depth = int(input("Enter tree depth(5-10 recommended): "))
    angle = float(input("Enter branch angle in degrees(20-40 recommended): "))

    screen = turtle.Screen()
    screen.title("Fractal Tree")
    screen.bgcolor("lightblue")

    t = setup_turtle()
    t.pensize(3)

    # Draw trunk
    t.pencolor("saddlebrown")
    t.pensize(max(1, depth))
    draw_branch(t, 150, angle, depth, depth)

    # Add fun message
    t.penup()
    t.goto(0, -300)
    t.write("Your Fractal Tree is Complete!", align="center", font=("Arial", 16, "bold"))

    screen.exitonclick()

if __name__ == "__main__":
    main()                    