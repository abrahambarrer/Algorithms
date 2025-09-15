import turtle

def main():
    t = turtle.Turtle()
    screen = t.getscreen()

    for i in range(4):
        t.forward(25)
        t.left(90)

if __name__ == '__main__':
    main()