import tkinter

"""
Practice 6.1 Write a Tkinter program that 
creates a main window with a menu that says 
Help. Within the Help menu item should be 
another menu item that says About. When the 
About menu is selected, your program should 
print “About was Selected” to the screen.
"""

def main():
    root = tkinter.Tk()

    root.title('Help!')

    # Help function
    def ask_help():
        print("About was selected...")

    bar = tkinter.Menu(root)
    filemenu = tkinter.Menu(bar, tearoff=0)
    filemenu.add_command(label='About', command=ask_help)
    bar.add_cascade(label='Help', menu=filemenu)

    root.config(menu=bar)

if __name__ == '__main__':
    main()
    tkinter.mainloop()