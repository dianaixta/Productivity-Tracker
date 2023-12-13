from graphics import *
#This program lets the user input text and change input dialog box colors to create a schedule

#Created a button class to ensure functionality of buttons
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
        self.active = True

    #Determining click inputs
    def clicked(self, p):
        return ((self.xmin <= p.getX() <= self.xmax) and
                (self.ymin <= p.getY() <= self.ymax) and
                self.active)

    #getting info from buttons
    def getLabel(self):
        return self.label.getText()

    #Determining if button is active
    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
        self.rect.setFill(self.color1)

    #Determining if button is inactive
    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        self.rect.setFill(self.color2)

    #Button colors depending on active status
    def setColor(self, color1, color2):
        self.color1, self.color2 = color1, color2
        self.rect.setFill(color1)

#Creating input dialog boxes
class InputDialog:
    def __init__(self, win, position, saved_text=""):
        self.selected_color = None

        self.rect = Rectangle(position, Point(position.getX() + 10, position.getY() - 0.5))
        self.rect.draw(win)

        # Entry field for user input
        self.entry = Entry(Point(position.getX() + 5, position.getY() - 0.25), 20)
        self.entry.draw(win)
        self.entry.setText(saved_text)

        self.color1, self.color2 = 'moccasin', 'red'
        self.activate()

    #Button clicks on input dialog boxes
    def clicked(self, p):
        return ((self.rect.getP1().getX() <= p.getX() <= self.rect.getP2().getX()) and
                (self.rect.getP2().getY() <= p.getY() <= self.rect.getP1().getY()))

    #Default color of dialog boxes
    def activate(self):
        self.rect.setWidth(0.5)
        self.rect.setFill(self.color1)
        self.entry.setFill('moccasin')

    def setColor(self, color1, color2):
        self.color1, self.color2 = color1, color2
        self.rect.setFill(color1)

    #Creating function to toggle input dialog colors
    def toggleColor(self, colors):
        if self.selected_color is None or self.selected_color not in colors:
            self.selected_color = colors[0]
        else:
            current_index = colors.index(self.selected_color)
            next_index = (current_index + 1) % len(colors)
            self.selected_color = colors[next_index]

        self.setColor(self.selected_color, self.selected_color)


class DayScreen:
    #open graphics windows
    def __init__(self, header):
        self.win = win = GraphWin('Day Chart', 800, 800)
        win.setBackground('orange')
        win.setCoords(0, 0, 20, 20)

        self.elements = []

        #Add time ticks
        for i, time in enumerate(['7am', '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm',
                                  '4pm', '5pm', '6pm', '7pm', '8pm', '9pm']):
            text = Text(Point(3.5, 17.75 - i), time).draw(win)
            self.elements.append(text)

        #Initializing with empty string
        self.buttons = []
        self.input_dialogs = []
        self.saved_texts = [""] * 15

        #Create input dialog boxes
        daybox = Rectangle(Point(4, 2), Point(16, 19))
        daybox.setFill('moccasin')
        daybox.setOutline('black')
        daybox.draw(win)

        self.days = []

        #Drawing dialog boxes
        for i in range(15):
            position = Point(5, 18 - i)
            saved_text = self.load_saved_text(i)
            input_dialog = InputDialog(win, position, saved_text)
            self.input_dialogs.append(input_dialog)
            self.days.append(input_dialog.entry.getText())

        #Buttons to exit, load or save files
        self.buttons.append(Button(win, Point(18, 19), 1, 0.5, "Exit"))
        self.buttons.append(Button(win, Point(2,2),2,0.5,"Input File"))
        self.buttons.append(Button(win, Point(18,2),2,0.5, "Save File"))

        #Header
        title = Text(Point(10, 19.5), header)
        title.draw(win)
        title.setSize(26)
        title.setFace('courier')

        #Making sure buttons are active
        for button in self.buttons:
            button.setColor('moccasin', 'red')
            button.activate()

    def getButton(self):
        while True:
            p = self.win.getMouse()

            for button in self.buttons:
                if button.clicked(p):
                    return button.getLabel()

            #Let user choose color for dialog box
            for input_dialog in self.input_dialogs:
                if input_dialog.clicked(p):
                    colors = []
                    input_dialog.toggleColor(['red', 'green', 'blue', 'yellow', 'moccasin'])
                    colors.append(input_dialog.selected_color)
                    self.days.append(colors[-1])
                    self.save_text(input_dialog)

    #Storing color inputs from dialog boxes
    def save_text(self, input_dialog):
        index = self.input_dialogs.index(input_dialog)
        self.saved_texts[index] = input_dialog.entry.getText()

    def load_saved_text(self, index):
        if 0 <= index < len(self.saved_texts):
            return self.saved_texts[index]
        else:
            return ""

    # #Adding function to buttons
    # def getChoice(self):
    #     choice = self.getButton()
    #
    #     if choice == "Exit":
    #         self.win.close()
    #
    #     if choice == "Input File":
    #         self.load_from_file()
    #         self.fname = input("Enter filename: ")
    #         self.infile = open(self.fname, "r")
    #         self.data = self.infile.read()
    #         self.tasks = self.data[::2]
    #         self.color = self.data.remove(self.tasks)
    #
    #     if choice == "Save File":
    #         self.save_to_file()
    #         self.outfileName = input("What file should your day be listed on? ")
    #         self.outfile = open(self.outfileName, "w")
    #         print(self.days, file=self.outfile)
    #         self.outfile.close()
    #         print("Day List has been written to", self.outfileName)
    #
    #     def load_from_file(self):
    #         self.fname = input("Enter filename: ")
    #         try:
    #             with open(self.fname, 'r') as infile:
    #                 self.saved_texts = infile.read().splitlines()
    #                 for i, input_dialog in enumerate(self.input_dialogs):
    #                     saved_text = self.load_saved_text(i)
    #                     input_dialog.entry.setText(saved_text)
    #         except FileNotFoundError:
    #             print(f'File {self.fname} not found.')
    #
    #
    #     def save_to_file(self):
    #         self.outfileName = input("What file should your day be listed on? ")
    #         with open(self.outfileName, "w") as outfile:
    #             for saved_text in self.saved_texts:
    #                 outfile.write(saved_text + "\n")
    #
    #         print("Day List has been written to", self.outfileName)

    # Adding funciton to buttons
    def getChoice(self):
        choice = self.getButton()

        if choice == "Exit":
            self.win.close()

        if choice == "Input File":
            self.fname = input("Enter filename: ")
            with open(self.fname, "r") as infile:
                self.data = infile.read()
                # Split the data into tasks and colors based on a delimiter (comma in this case)
                task_color_pairs = self.data.strip().split(',')

                # Extract tasks and colors from pairs
                self.tasks = [pair.split(':')[0].strip() for pair in task_color_pairs]
                self.colors = [pair.split(':')[1].strip() for pair in task_color_pairs]

                # Update the input dialogs with loaded tasks and colors
                for i, input_dialog in enumerate(self.input_dialogs):
                    input_dialog.entry.setText(self.tasks[i])
                    input_dialog.selected_color = self.colors[i]
                    input_dialog.setColor(self.colors[i], self.colors[i])

        if choice == "Save File":
            self.outfileName = input("What file should your day be listed on? ")
            with open(self.outfileName, "w") as outfile:
                # Save tasks and colors as pairs in the file
                pairs = [f"{task}: {color}" for task, color in zip(self.tasks, self.colors)]
                outfile.write(', '.join(pairs))

            print("Day List has been written to", self.outfileName)

def main():
    screen = DayScreen('Monday')
    screen.getChoice()

if __name__ == '__main__':
    main()
