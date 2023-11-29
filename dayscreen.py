from graphics import *
from button import Button

class DayScreen:
    def __init__(self):
        self.win = win = GraphWin('Day Chart',500,500)
        win.setBackground('orange')
        win.setCoords(0,0,100,100)

        #box for day
        daybox = Rectangle(Point(25,7.5), Point(80,87.5))
        daybox.setFill('white')
        daybox.setOutline('black')
        daybox.draw(win)

        #Add Time ticks
        self.sixam = Text(Point(20,85), '6am').draw(win)
        self.sevenam = Text(Point(20,80), '7am').draw(win)
        self.eightam = Text(Point(20,75), '8am').draw(win)
        self.nineam = Text(Point(20,70), '9am').draw(win)
        self.tenam = Text(Point(20,65), '10am').draw(win)
        self.elevenam = Text(Point(20,60), '11am').draw(win)
        self.twelvepm = Text(Point(20,55), '12pm').draw(win)
        self.onepm = Text(Point(20,50), '1pm').draw(win)
        self.twopm = Text(Point(20,45), '2pm').draw(win)
        self.threepm = Text(Point(20,40), '3pm').draw(win)
        self.fourpm = Text(Point(20,35), '4pm').draw(win)
        self.fivepm = Text(Point(20,30), '5pm').draw(win)
        self.sixpm = Text(Point(20, 25), '6pm').draw(win)
        self.sevenpm = Text(Point(20,20), '7pm').draw(win)
        self.eightpm = Text(Point(20,15), '8pm').draw(win)
        self.ninepm = Text(Point(20,10), '9pm').draw(win)

        self.buttons = []

        #Exit button
        self.buttons.append(Button(win, Point(90,90), 7.5, 7.5, "Exit"))


        #Day header

    def drag(self):
        pass

    def run(self):
        p = self.win.getMouse()

def main():
    day = DayScreen()
    day.run()

main()
