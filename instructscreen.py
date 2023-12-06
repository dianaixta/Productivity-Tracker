from graphics import *
from button import Button
from mainscreen import mainScreen

class Instructions:
    def __init__(self):
        self.win = win = GraphWin("Instructions", 500, 500)
        win.setCoords(0,0,10,10)
        win.setBackground("orange")

        self.Buttons = []

        self.Buttons.append(Button(win, Point(9,9), 1, 1, "X"))


        self.heading = heading = Text(Point(5,7) , " Welcome to Blocks \n the Productivity App! ")
        heading.setFace('courier')
        heading.setFill('black')
        heading.setSize(22)
        heading.draw(win)

        self.body = body = Text(Point(5,4), "At the beginning of the week, input all of \n your tasks for school, work, etc. Then, \n a curated  schedule for your week \n will be created for you!")
        body.setSize(14)
        body.setFace('courier')
        body.setFill('black')
        body.draw(win)

        self.Buttons.append(Button(win, Point(5,1), 5, 1.25, "Let's Begin!"))

        for button in self.Buttons:
            button.setColor('moccasin', 'red')
            button.activate()

    def getButton(self):
            while True:
                p = self.win.getMouse()
                for B in self.Buttons:
                    if B.clicked(p):
                        return B.getLabel()
    def run(self):
        p = self.win.getMouse()

    def getChoice(self):
        choice = self.getButton()
        if choice == "Let's Begin!":
            self.win.close()
            screen = mainScreen()
            screen.getChoice()
        if choice == 'X':
            self.win.close()

#def main():
    #instr = Instructions()
    #instr.getChoice()

#main()
