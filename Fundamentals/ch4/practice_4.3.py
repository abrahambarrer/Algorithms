import turtle

def draw_circle(turtle_object):
    turtle_object.color('black')
    turtle_object.begin_fill()
    turtle_object.circle(20)
    turtle_object.end_fill()


def main():
    t = turtle.Turtle()
    screen = t.getscreen()

    t.color('black', 'yellow')
    t.begin_fill()

    t.forward(80)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(45)
    t.forward(56)
    t.left(45)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(120)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(180)

    t.end_fill()

    t.right(180)
    draw_circle(t)
    t.forward(110)
    draw_circle(t)
    screen.exitonclick()

if __name__ == '__main__':
    main()