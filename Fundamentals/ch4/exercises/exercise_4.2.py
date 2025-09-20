import turtle
from xml.dom import minidom

def main():
    xmldoc = minidom.parse('file.xml')

    graphicsCommand = xmldoc.getElementsByTagName('GraphicsCommands')[0]
    commands = graphicsCommand.getElementsByTagName('Command')

    commandList = []
    xList = []
    yList = []
    widthList = []
    colorList = []
    radiusList = []

    attributeList = [xList, yList, widthList, colorList, radiusList]
    attributes = ['x', 'y', 'width', 'color', 'radius']

    for command in commands:
        commandList.append(command.firstChild.data.strip())
        attr = command.attributes
        # Recorrer lista de atributos por indice
        for i in range(len(attributes)):
            attr = command.attributes
            key = attributes[i]
            # Buscar llave en los atributos del comando
            if key in attr:
                attributeList[i].append(attr[key].value)
            else:
                attributeList[i].append(None)

    turtle_object = turtle.Turtle()
    screen = turtle_object.getscreen()
    screen.colormode(255)
    screen.tracer(0)

    for i in range(len(commandList)):
        command = commandList[i]
        if command == 'PenUp':
            turtle_object.penup()
        elif command == 'PenDown':
            turtle_object.pendown()
        elif command == 'GoTo':
            x = float(xList[i])
            y = float(yList[i])
            width = float(widthList[i])
            color = colorList[i]
            turtle_object.width(width)
            turtle_object.color(color)
            turtle_object.goto(x, y)
        elif command == 'Circle':
            radius = float(radiusList[i])
            width = float(widthList[i])
            color = colorList[i]
            turtle_object.width(width)
            turtle_object.color(width)
            turtle_object.circle(radius)
        elif command == 'BeginFill':
            color = colorList[i]
            turtle_object.color(color)
            turtle_object.begin_fill()
        elif command == 'EndFill':
            turtle_object.end_fill()
        else:
            print('Error. Unknown command: ', command)

    screen.update()
    screen.exitonclick()

if __name__ == '__main__':
    main()
