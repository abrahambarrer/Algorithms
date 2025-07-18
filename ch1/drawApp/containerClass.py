import turtle

class GoToCommand:
    def __init__(self, x, y, width=1, color='black'):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)

    def __str__(self):
        return '<Command x="' + str(self.x) + '" y="' + str(self.y) + '" width="' + \
                str(self.width) + '" color="' + self.color + '">GoTo</Command>'

class CircleCommand:
    def __init__(self, radius, width=1, color='black'):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)

    def __str__(self):
        return '<Command radius="' + str(self.radius) + '" width="' + str(self.width) + \
                '" color="' + str(self.color) + '">Circle</Command>'

class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        return '<Command color="' + str(self.color) + '">BeginFill</Command>'

class EndFillCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.end_fill()

    def __str__(self):
        return '<Command>EndFill</Command>'

class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()

    def __str__(self):
        return '<Command>PenUp</Command>'

class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        return '<Command>PenDown</Command>'

class PyList():
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    def removeLast(self):
        self.items = self.items[-1]

    def __iter__(self):
        for c in self.items:
            yield c

    def __len__(self):
        return len(self.items)
# def main():
#     filename = '../data/command2.txt'
#
#     t = turtle.Turtle()
#     screen = t.getscreen()
#
#     file = open(filename, "r")
#
#     graphicsCommands = PyList()
#
#     command = file.readline().strip()
#
#     while command != "":
#         if command == "goto":
#             x = float(file.readline())
#             y = float(file.readline())
#             width = float(file.readline())
#             color = file.readline().strip()
#             cmd = GoToCommand(x, y, width, color)
#         elif command == "circle":
#             radius = float(file.readline())
#             width = float(file.readline())
#             color = file.readline().strip()
#             cmd = CircleCommand(radius, width, color)
#         elif command == "beginfill":
#             color = file.readline().strip()
#             cmd = BeginFillCommand(color)
#         elif command == "endfill":
#             cmd = EndFillCommand()
#         elif command == "penup":
#             cmd = PenUpCommand()
#         elif command == "pendown":
#             cmd = PenDownCommand()
#         else:
#             raise RuntimeError("Unknown Command: " + command)
#
#         graphicsCommands.append(cmd)
#
#         command = file.readline().strip()
#
#     for cmd in graphicsCommands:
#         cmd.draw(t)
#
#     file.close()
#     t.ht()
#     screen.exitonclick()
#     print('Program Execution Completed')
#
# if __name__ == '__main__':
#     main()