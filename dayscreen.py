from graphics import *
from button import Button

class DayScreen:
    def __init__(self):
        self.win = win = GraphWin('Day Chart',800,800)
        win.setBackground('orange')
        win.setCoords(0, 0, 10, 10)

        #box for day
        daybox = Rectangle(Point(3,1), Point(8.5,9))
        daybox.setFill('moccasin')
        daybox.setOutline('black')
        daybox.draw(win)

        #Add Time ticks
        self.sixam = Text(Point(2,1.25), '6am').draw(win)
        self.sevenam = Text(Point(2,1.75), '7am').draw(win)
        self.eightam = Text(Point(2,2.25), '8am').draw(win)
        self.nineam = Text(Point(2,2.75), '9am').draw(win)
        self.tenam = Text(Point(2,3.25), '10am').draw(win)
        self.elevenam = Text(Point(2,3.75), '11am').draw(win)
        self.twelvepm = Text(Point(2,4.25), '12pm').draw(win)
        self.onepm = Text(Point(2,4.75), '1pm').draw(win)
        self.twopm = Text(Point(2,5.25), '2pm').draw(win)
        self.threepm = Text(Point(2,5.75), '3pm').draw(win)
        self.fourpm = Text(Point(2,6.25), '4pm').draw(win)
        self.fivepm = Text(Point(2,6.75), '5pm').draw(win)
        self.sixpm = Text(Point(2, 7.25), '6pm').draw(win)
        self.sevenpm = Text(Point(2,7.75), '7pm').draw(win)
        self.eightpm = Text(Point(2,8.25), '8pm').draw(win)
        self.ninepm = Text(Point(2,8.75), '9pm').draw(win)

        #add grid lines for hourly schedule
        


        self.buttons = []

        #Exit button
        self.buttons.append(Button(win, Point(90,90), 7.5, 7.5, "Exit"))


        #Day header


        #add buttons
        for button in self.buttons:
            button.setColor('moccasin', 'red')
            button.activate()

    def drag(self):
        pass

    def run(self):
        p = self.win.getMouse()

def main():
    screen = DayScreen()
    screen.run()

if __name__ == '__main__':
    main()
#save name of day as a property
#list of lists to store times
#add color buttons
#save pre-exisiting information to be edited later
