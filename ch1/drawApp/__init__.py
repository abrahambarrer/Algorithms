import turtle
# Reading from one-line record
def main():
    filename = '../data/command.txt'  # input('Please enter drawing filename: ')

    t = turtle.Turtle()
    screen = t.getscreen()

    file = open(filename, 'r')

    for line in file:
        text = line.strip()

        commandList = [item.strip() for item in line.split(',')]
        command = commandList[0]

        if command == 'goto':
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == 'circle':
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == 'beginfill':
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == 'endfill':
            t.end_fill()
        elif command == 'penup':
            t.penup()
        elif command == 'pendown':
            t.pendown()
        else:
            print('Unkoun command found in file: ', command)

    file.close()

    t.ht()

    screen.exitonclick()

    print('Program Execution Completed.')
if __name__ == '__main__':
    main()