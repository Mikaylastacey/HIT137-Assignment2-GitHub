#import Turtle package
import turtle

#recursive function
def draw_fractal_edge(t, length, depth):
    """Draw one edge of the polygon recursively with inward indentation."""
    if depth == 0:
        t.forward(length)
        return

    L = length / 3.0

    # First third
    draw_fractal_edge(t, L, depth - 1)

    # Inward equilateral triangle: right 60°, left 120°, right 60°
    t.right(60)
    draw_fractal_edge(t, L, depth - 1)

    t.left(120)
    draw_fractal_edge(t, L, depth - 1)

    t.right(60)
    draw_fractal_edge(t, L, depth - 1)


# Draw full fractal polygon
def draw_fractal_polygon(sides, side_len, depth):
    # Setup turtle screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Recursive Fractal Polygon")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("cyan")
    pen.pensize(1)
    pen.hideturtle()
    turtle.tracer(False)

    # Move pen to starting position
    pen.penup()
    pen.goto(-side_len / 2.0, 0)
    pen.setheading(0)  # Facing right
    pen.pendown()

    # Draw all sides clockwise
    exterior_turn = 360 / sides
    for _ in range(sides):
        draw_fractal_edge(pen, side_len, depth)
        pen.right(exterior_turn)

    turtle.tracer(True)
    turtle.done()

# Main function
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of sides: "))
        L = float(input("Enter the side length (pixels): "))
        d = int(input("Enter the recursion depth: "))

        if n < 3 or d < 0:
            print("Number of sides must be >= 3 and recursion depth >= 0.")
        else:
            draw_fractal_polygon(n, L, d)

    except ValueError:
        print("Invalid input! Please enter numbers only.")#enter code path here
