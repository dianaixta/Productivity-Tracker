from graphics import *
from button import Button

class mainScreen:
    #open a graphics window
    def __init__(self):
        self.win = win = GraphWin("Main Page", 900, 450)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("orange")

        title = Text(Point(5,7), 'BLOCKS: THE PRODUCTIVITY APP')
        title.draw(win)
        title.setSize(26)
        title.setFace('courier')

        self.__createButtons()

#create buttons (location, label)
    def __createButtons(self):
        bSpecs = [('Monday', 1.25, 5), ('Tuesday', 2.5, 5), ('Wednesday', 3.75, 5),
        ('Thursday', 5, 5), ('Friday', 6.25, 5), ('Saturday', 7.5, 5), ('Sunday', 8.75, 5)]
        self.buttons = []

#add buttons to screen
        for (label, cx, cy) in bSpecs:
            self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))

#add unique buttons
        self.buttons.append(Button(self.win, Point(5, 3), 2, 1, 'Close'))
        self.buttons.append(Button(self.win, Point(9,9), .5,.5, 'X'))

#activate buttons
        for button in self.buttons:
            button.setColor('moccasin', 'red')
            button.activate()
#getting button info
    def getButton(self):
        while True:
            p = self.win.getMouse()
            for button in self.buttons:
                if button.clicked(p):
                    return button.getLabel()

    def run(self):
        p = self.win.getMouse()

def main():
    screen = mainScreen()
    screen.run()

if __name__ == '__main__':
    main()
