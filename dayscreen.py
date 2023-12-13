import pickle
from graphics import *
from button import Button
from inputdialog import InputDialog

#This program opens a window for a chosen day of the week and takes user
#input to create a personalized schedule

class DayScreen:
    #Open graphics window
    def __init__(self, header, day_of_week):
        self.day_of_week = day_of_week
        self.win = GraphWin(f'{day_of_week} Chart', 800, 800)
        self.win.setBackground('orange')
        self.win.setCoords(0, 0, 20, 20)

        #Create labels for hours
        self.sevenam = Text(Point(4, 17.75), '7am').draw(self.win)
        self.eightam = Text(Point(4, 16.75), '8am').draw(self.win)
        self.nineam = Text(Point(4, 15.75), '9am').draw(self.win)
        self.tenam = Text(Point(4, 14.75), '10am').draw(self.win)
        self.elevenam = Text(Point(4, 13.75), '11am').draw(self.win)
        self.twelvepm = Text(Point(4, 12.75), '12pm').draw(self.win)
        self.onepm = Text(Point(4, 11.75), '1pm').draw(self.win)
        self.twopm = Text(Point(4, 10.75), '2pm').draw(self.win)
        self.threepm = Text(Point(4, 9.75), '3pm').draw(self.win)
        self.fourpm = Text(Point(4, 8.75), '4pm').draw(self.win)
        self.fivepm = Text(Point(4, 7.75), '5pm').draw(self.win)
        self.sixpm = Text(Point(4, 6.75), '6pm').draw(self.win)
        self.sevenpm = Text(Point(4, 5.75), '7pm').draw(self.win)
        self.eightpm = Text(Point(4, 4.75), '8pm').draw(self.win)
        self.ninepm = Text(Point(4, 3.75), '9pm').draw(self.win)

        self.input_dialogs = []
        self.buttons = []

        # Load saved data (text and colors)
        self.saved_data = self.load_data()

        # Create InputDialogs without time slots
        for i in range(15):
            position = Point(5, 18 - i)
            saved_text = self.saved_data[i]["text"] if i < len(self.saved_data) else ""
            saved_color = self.saved_data[i]["color"] if i < len(self.saved_data) else ""

            input_dialog = InputDialog(self.win, position, saved_text=saved_text)
            input_dialog.selected_color = saved_color
            input_dialog.setColor(saved_color, saved_color)
            self.input_dialogs.append(input_dialog)

        self.buttons = [Button(self.win, Point(18, 19), 1, 0.5, "Exit")]

        #Header
        title = Text(Point(10, 19.5), header)
        title.draw(self.win)
        title.setSize(26)
        title.setFace('courier')

        #Checking activation of buttons
        for button in self.buttons:
            button.setColor('moccasin', 'black')
            button.activate()

    #Getting button info
    def getButton(self):
        while True:
            p = self.win.getMouse()
            for button in self.buttons:
                if button.clicked(p):
                    return button.getLabel()

            #Toggling between colors for dialog boxes
            for input_dialog in self.input_dialogs:
                if input_dialog.clicked(p):
                    input_dialog.toggleColor(['red', 'green', 'blue', 'yellow', 'moccasin'])

    def run(self):
        while True:
            choice = self.getButton()
            if choice == "Exit":
                # Save text and colors before closing
                self.save_data()
                self.win.close()
                break

    #Input file
    def load_data(self):
        try:
            filename = f"{self.day_of_week.lower()}_data.pkl"
            with open(filename, 'rb') as infile:
                saved_data = pickle.load(infile)

            # Ensure saved_data is a list of dictionaries
            if not isinstance(saved_data, list):
                saved_data = []

            # Ensure each dictionary has 'text' and 'color' keys
            saved_data = [{"text": str(item["text"]), "color": str(item["color"])}
                          for item in saved_data if isinstance(item, dict)]
        except FileNotFoundError:
            saved_data = [{"text": "", "color": ""} for _ in range(15)]

        return saved_data


    def save_data(self):
        filename = f"{self.day_of_week.lower()}_data.pkl"
        with open(filename, "wb") as outfile:
            pickle.dump(
                [{"text": input_dialog.entry.getText(), "color": input_dialog.selected_color}
                 for input_dialog in self.input_dialogs], outfile)

#Customized window for each day
def main():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days_of_week:
        screen = DayScreen(day, day_of_week=day)
        screen.run()

if __name__ == '__main__':
    main()
