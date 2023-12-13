from graphics import *
from button import Button
from mainscreen import mainScreen

#This program opens the instructions window for the user
class Instructions:
    #Open graphics window
    def __init__(self):
        self.win = win = GraphWin("Instructions", 600, 600)
        win.setCoords(0,0,10,10)
        win.setBackground("orange")

        self.Buttons = []
        self.Buttons.append(Button(win, Point(9,9), 1, 1, "X"))

        #Header
        self.heading = heading = Text(Point(5,7) , " Welcome to Blocks \n the Productivity App! ")
        heading.setFace('courier')
        heading.setFill('black')
        heading.setSize(22)
        heading.draw(win)

        #Instructions for user
        self.body = body = Text(Point(5,4.5), "At the beginning of the week, \n"
        "input all of your tasks for school, work, etc. \n Click on the text boxes "
        "to color code your schedule. \n AND JUST LIKE THAT! \n A customized schedule, just for you!")
        body.setSize(14)
        body.setFace('courier')
        body.setFill('black')
        body.draw(win)

        #Button to launch mainScreen window to display all days of the week
        self.Buttons.append(Button(win, Point(5,1), 5, 1.25, "Let's Begin!"))

        #Activate buttons
        for button in self.Buttons:
            button.setColor('moccasin', 'red')
            button.activate()

    #Get info from buttons
    def getButton(self):
            while True:
                p = self.win.getMouse()
                for B in self.Buttons:
                    if B.clicked(p):
                        return B.getLabel()
    def run(self):
        p = self.win.getMouse()

    #Launching action with button info
    def getChoice(self):
        choice = self.getButton()
        if choice == "Let's Begin!":
            self.win.close()
            screen = mainScreen()
            screen.getChoice()
        if choice == 'X':
            self.win.close()

##Code used to test if window was working
# def main():
#     instr = Instructions()
#     instr.getChoice()
#
# main()
