# from graphics import *
# from button import Button
# from dayscreen import DayScreen
#
# # This program displays each day of the week for the user to input their schedule
# class mainScreen:
#     # Open a graphics window
#     def __init__(self):
#         self.win = win = GraphWin("Main Page", 900, 450)
#         win.setCoords(0, 0, 10, 10)
#         win.setBackground("orange")
#
#         title = Text(Point(5,7), 'Blocks: The Productivity App')
#         title.draw(win)
#         title.setSize(26)
#         title.setFace('courier')
#
#         self.__createButtons()
#
#     # Create buttons (location, label)
#     def __createButtons(self):
#         bSpecs = [('Monday', 1.25, 5), ('Tuesday', 2.5, 5), ('Wednesday', 3.75, 5),
#                   ('Thursday', 5, 5), ('Friday', 6.25, 5), ('Saturday', 7.5, 5), ('Sunday', 8.75, 5)]
#         self.buttons = []
#
#         # Add buttons to screen
#         for (label, cx, cy) in bSpecs:
#             self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
#
#         # Add unique buttons
#         self.buttons.append(Button(self.win, Point(5, 3), 2, 1, 'Exit'))
#
#         # Activate buttons
#         for button in self.buttons:
#             button.setColor('moccasin', 'red')
#             button.activate()
#
#     # Get button info
#     def getButton(self):
#         while True:
#             p = self.win.getMouse()
#             for button in self.buttons:
#                 if button.clicked(p):
#                     return button.getLabel()
#
#     # Take action based on button info
#     def getChoice(self):
#         choice = self.getButton()
#         if choice in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
#             self.win.close()
#             day = DayScreen(header=choice, day_of_week=choice)
#             day.run()
#
#         elif choice == 'Exit':
#             self.win.close()
#
# def main():
#     mainscreen = mainScreen()
#     mainscreen.getChoice()
#
# if __name__ == '__main__':
#     main()
# main_screen.py

from graphics import *
from button import Button
from dayscreen import DayScreen

class mainScreen:
    def __init__(self):
        self.win = win = GraphWin("Main Page", 900, 450)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("orange")

        title = Text(Point(5,7), 'Blocks: The Productivity App')
        title.draw(win)
        title.setSize(26)
        title.setFace('courier')

        self.__createButtons()
        self.saved_texts = [""] * 7  # Initialize an empty list for saved texts

    def __createButtons(self):
        bSpecs = [('Monday', 1.25, 5), ('Tuesday', 2.5, 5), ('Wednesday', 3.75, 5),
                  ('Thursday', 5, 5), ('Friday', 6.25, 5), ('Saturday', 7.5, 5), ('Sunday', 8.75, 5)]
        self.buttons = []

        for (label, cx, cy) in bSpecs:
            self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))

        self.buttons.append(Button(self.win, Point(5, 3), 2, 1, 'Exit'))

        for button in self.buttons:
            button.setColor('moccasin', 'red')
            button.activate()

    def getButton(self):
        while True:
            p = self.win.getMouse()
            for button in self.buttons:
                if button.clicked(p):
                    return button.getLabel()

    def getChoice(self):
        choice = self.getButton()
        if choice in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            self.win.close()
            day_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(choice)
            day = DayScreen(header=choice, day_of_week=choice, saved_texts=self.saved_texts[day_index])
            day.run()

        elif choice == 'Exit':
            self.win.close()

def main():
    mainscreen = mainScreen()
    mainscreen.getChoice()

if __name__ == '__main__':
    main()
