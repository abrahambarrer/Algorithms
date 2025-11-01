import sys
import tkinter

def main():
    root = tkinter.Tk()

    root.title('Reminder!')
    root.resizable(width=False, height=False)

    # Menu
    def quit():
        root.destroy()

    bar = tkinter.Menu(root)
    filemenu = tkinter.Menu(bar, tearoff=0)
    filemenu.add_command(label=" Exit ", command=quit)
    bar.add_cascade(label="File", menu=filemenu)
    root.config(menu=bar)

    root.mainloop() # Call the event dispatch loop




if __name__ == '__main__':
    main()