from turtle import *

def main():
    t = Turtle()
    screen = t.getscreen()

    t.forward(25)
    t.left(72.5)
    t.forward(25)
    t.left(72.5)
    t.forward(25)
    t.left(72.5) # Where is at the peak ? (12.04, 38.18)
    t.forward(25)
    t.left(72.5)
    t.forward(25)
    screen.exitonclick()

if __name__ == '__main__':
    main()