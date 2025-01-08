"""Recursive Turtle Drawing!"""

__author__: str = "730659778"

from turtle import Turtle, colormode, done
colormode(255)

pen: Turtle = Turtle()


def draw_square(pen: Turtle, x: int, y: int) -> None:
    """Draws a square."""
    pen.penup()
    pen.goto(x, y)
    pen.color("brown")
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(178, 34, 34)
    for i in range(4):
        pen.forward(300) 
        pen.left(90)
    pen.end_fill()


def draw_roof(pen: Turtle, x: int, y: int) -> None:
    """Draws a triangle as the roof."""
    pen.penup()
    pen.goto(x, y + 300)
    pen.color("red")
    pen.pendown()
    pen.begin_fill()
    for i in range(3):
        pen.forward(300)
        pen.left(120)
    pen.end_fill()


def draw_windows(pen: Turtle, x: int, y: int, index: int) -> None:
    """Draws three windows using recursion."""
    if index == 0:
        return
    pen.penup()
    pen.goto(x + 50, y + 200)
    pen.color("blue")
    pen.pendown()
    pen.begin_fill()
    for i in range(4):
        pen.forward(50)
        pen.left(90)
    pen.end_fill()
    draw_windows(pen, x + 70, y, index - 1)
 

def draw_sol(pen: Turtle, x: int, y: int) -> None:
    """Draws the actual sun."""
    pen.penup()
    pen.goto(x, y)
    pen.color("yellow")
    pen.pendown()
    pen.begin_fill()
    for i in range(360):
        pen.forward(2)
        pen.left(1)
    pen.end_fill()
    

def main() -> None:
    """Building the scene."""
    pen.speed(200)
    draw_square(pen, -300, -250)
    draw_roof(pen, -300, -250)
    draw_windows(pen, -300, -250, 3)
    draw_sol(pen, 100, 100)
    done()
    

if __name__ == "__main__":
    main()