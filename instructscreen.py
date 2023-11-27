from graphics import *
from button import Button

class Instructions:
    def __init__(self):
        self.win = win = GraphWin("Instructions", 500, 500)
        win.setCoords(0,0,10,10)
        win.setBackground("orange")

        self.exit = exit = Button(win, Point(9,9), 1, 1, "Exit")

        self.heading = heading = Text(Point(5,7) , " Welcome to Blocks \n the Productivity App! ")
        heading.setFace('courier')
        heading.setFill('black')
        heading.setSize(22)
        heading.setStyle("bold")
        heading.draw(win)

        self.body = body = Text(Point(5,4), "At the beginning of the week, input all of \n your tasks for school, work, etc. Then, \n a curated  schedule for your week \n will be created for you!")
        body.setSize(14)
        body.setFace('courier')
        body.setFill('black')
        body.draw(win)

        self.enter = enter = Button(win, Point(5,1), 5, 1.25, "Let's Begin!")


    def run(self):
        p = self.win.getMouse()


    def AppClose(self):
        p = self.win.getMouse()
        if exit.clicked(p):
            win.close()

    def AppStart(self):
        p = self.win.getMouse()
        if enter.clicked(p):
            AppMain()

def main():
    instr = Instructions()
    instr.run()

main()
