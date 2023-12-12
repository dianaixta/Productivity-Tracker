from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        p1 = Point(x+w, y+h)
        p2 = Point(x-w, y-h)
        self.xmin, self.ymin = x-w, y-h
        self.xmax, self.ymax = x+w, y+h
        self.rect = Rectangle(p1, p2)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.color1, self.color2 = 'moccasin', 'red'
        self.active = True  # Set the button active by default

    def clicked(self, p):
        return ((self.xmin <= p.getX() <= self.xmax) and
                (self.ymin <= p.getY() <= self.ymax) and
                self.active)

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
        self.rect.setFill(self.color1)

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        self.rect.setFill(self.color2)

    def setColor(self, color1, color2):
        self.color1, self.color2 = color1, color2
        self.rect.setFill(color1)


class InputDialog:
    def __init__(self, win, position):
        self.selected_color = None  # Track the selected color

        self.rect = Rectangle(position, Point(position.getX() + 10, position.getY() - 0.5))
        self.rect.draw(win)

        # Entry field for user input
        self.entry = Entry(Point(position.getX() + 5, position.getY() - 0.25), 20)
        self.entry.draw(win)

        self.color1, self.color2 = 'moccasin', 'red'
        self.activate()

    def clicked(self, p):
        return ((self.rect.getP1().getX() <= p.getX() <= self.rect.getP2().getX()) and
                (self.rect.getP2().getY() <= p.getY() <= self.rect.getP1().getY()))

    def activate(self):
        self.rect.setWidth(0.5)
        self.rect.setFill(self.color1)
        self.entry.setFill('moccasin')

    def setColor(self, color1, color2):
        self.color1, self.color2 = color1, color2
        self.rect.setFill(color1)

    def toggleColor(self, colors):
        # Toggle between colors on each click
        if self.selected_color is None or self.selected_color not in colors:
            self.selected_color = colors[0]
        else:
            current_index = colors.index(self.selected_color)
            next_index = (current_index + 1) % len(colors)
            self.selected_color = colors[next_index]

        self.setColor(self.selected_color, self.selected_color)


class DayScreen:
    def __init__(self, header):
        self.win = win = GraphWin('Day Chart', 800, 800)
        win.setBackground('orange')
        win.setCoords(0, 0, 20, 20)

        # Add Time ticks
        self.sevenam = Text(Point(3.5, 17.75), '7am').draw(win)
        self.eightam = Text(Point(3.5, 16.75), '8am').draw(win)
        self.nineam = Text(Point(3.5, 15.75), '9am').draw(win)
        self.tenam = Text(Point(3.5, 14.75), '10am').draw(win)
        self.elevenam = Text(Point(3.5, 13.75), '11am').draw(win)
        self.twelvepm = Text(Point(3.5, 12.75), '12pm').draw(win)
        self.onepm = Text(Point(3.5, 11.75), '1pm').draw(win)
        self.twopm = Text(Point(3.5, 10.75), '2pm').draw(win)
        self.threepm = Text(Point(3.5, 9.75), '3pm').draw(win)
        self.fourpm = Text(Point(3.5, 8.75), '4pm').draw(win)
        self.fivepm = Text(Point(3.5, 7.75), '5pm').draw(win)
        self.sixpm = Text(Point(3.5, 6.75), '6pm').draw(win)
        self.sevenpm = Text(Point(3.5, 5.75), '7pm').draw(win)
        self.eightpm = Text(Point(3.5, 4.75), '8pm').draw(win)
        self.ninepm = Text(Point(3.5, 3.75), '9pm').draw(win)

        self.buttons = []

        self.days = []

        # Box for day
        daybox = Rectangle(Point(4, 2), Point(16, 19))
        daybox.setFill('moccasin')
        daybox.setOutline('black')
        daybox.draw(win)

        # Add Input Dialog boxes to the right
        self.input_dialogs = []

        for i in range(15):
            position = Point(5, 18 - i)
            input_dialog = InputDialog(win, position)
            self.input_dialogs.append(input_dialog)
            self.days.append(input_dialog.entry.getText())

        # Exit button
        self.buttons.append(Button(win, Point(18, 19), 1, 0.5, "Exit"))

        #Input file button
        self.buttons.append(Button(win, Point(2,2),2,0.5,"Input File"))

        #Save File button
        self.buttons.append(Button(win, Point(18,2),2,0.5, "Save File"))


        # Day header
        title = Text(Point(10, 19.5), header)
        title.draw(win)
        title.setSize(26)
        title.setFace('courier')

        for button in self.buttons:
            button.setColor('moccasin', 'red')
            button.activate()




    def getButton(self):
        while True:
            p = self.win.getMouse()

            for button in self.buttons:
                if button.clicked(p):
                    return button.getLabel()

            for input_dialog in self.input_dialogs:
                if input_dialog.clicked(p):
                    colors = []
                    input_dialog.toggleColor(['red', 'green', 'blue', 'yellow', 'moccasin'])
                    colors.append(input_dialog.selected_color)

            self.days.append(colors[-1])


    def getChoice(self):
        choice = self.getButton()

        if choice == "Exit":
            self.win.close()

        if choice == "Input File":
            self.fname = input("Enter filename: ")
            self.infile = open(fname, "r")
            self.data = infile.read()
            self.tasks = data[::2]
            self.color = data.remove(tasks)

            #for i in tasks:
                #input_dialog.insert(tasks)




        if choice == "Save File":
            self.outfileName = input("What file should your day be listed on? ")
            self.outfile = open(self.outfileName, "w")
            print(self.days, file=self.outfile)
            self.outfile.close()
            print("Day List has been written to", self.outfileName)




def main():
    screen = DayScreen('Monday')
    screen.getChoice()

if __name__ == '__main__':
    main()
