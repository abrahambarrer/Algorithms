import turtle

# Feedback IA
def draw_axes(t):
    t.speed(0)
    t.color("gray")
    t.pensize(1)

    # Eje X
    t.penup()
    t.goto(-20, 0)
    t.pendown()
    t.goto(20, 0)

    # Eje Y
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.goto(0, 20)

    # Marcas en los ejes
    t.penup()
    for i in range(-20, 21):
        # Marcas en eje X
        t.goto(i, 0)
        t.dot(3, "black")
        # Marcas en eje Y
        t.goto(0, i)
        t.dot(3, "black")

def polynom(x):
    return x**4 / 4 - x**3 / 3 - 3 * x**2

def main():
    turtle_object = turtle.Turtle()

    screen = turtle_object.getscreen()
    screen.setworldcoordinates(-20, -20, 20, 20)
    screen.tracer(0)

    draw_axes(turtle_object)

    turtle_object.penup()
    turtle_object.pensize(3)
    turtle_object.goto(-20, polynom(-20))
    turtle_object.pendown()

    values = [i / 10 for i in range(-200, 201)] # Corregido espacio lineal a partir de [-200, 200]

    for x in values:
        turtle_object.goto(x, polynom(x))

    screen.update()
    screen.exitonclick()

if __name__ == '__main__':
    main()