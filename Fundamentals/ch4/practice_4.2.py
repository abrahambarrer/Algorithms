import turtle
CIRCUMFERENCE = 360

class Polygon:
    def __init__(self, number_sides, turtle_object):
        self.number_sides = number_sides
        self.angle = CIRCUMFERENCE / number_sides
        self.turtle_object = turtle_object

    def draw(self):
        screen = self.turtle_object.getscreen()

        for i in range(self.number_sides):
            self.turtle_object.forward(25)
            self.turtle_object.left(self.angle)

        screen.exitonclick()

def get_value():
    return int(input('Number of sides: '))

def main():
    t = turtle.Turtle()

    polygon1 = Polygon(get_value(), t)

    polygon1.draw()

if __name__ == '__main__':
    main()