from graphics import *
from button import Button

class Instructions:
    def __init__(self):
        self.win = win = GraphWin("Instructions", 1000, 1000)
        win.setCoords(0,0,10,10)
        win.setBackground("orange")

        self.exit = exit = Button(win, Point(9,9), 0.25, 0.25, "Exit")

        self.heading = heading = Text(Point(8.5,5) , "Welcome to Blocks the Productivity App!")
        heading.setSize(30)
        heading.setStyle("bold")

        self.body = body = Text(Point(4,5), "At the beginning of the week input all of your tasks/n/ for school, work, etc. manually or by adding a file. /n/ Then let our app create a curated schedule for your week.")
        body.setSize(24)

        self.enter = enter = Button(win, Point(1,5), 1, 0.25, "Let's Begin!")


    def AppClose(self):
        if exit.clicked():
            win.close()

    def AppStart(self):
        if enter.clicked():
            AppMain()

def main():
    Instructions()


main()
