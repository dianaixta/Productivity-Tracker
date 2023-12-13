# from graphics import *
#
# class Button:
#     def __init__(self, win, center, width, height, label):
#         w, h = width/2, height/2
#         x, y = center.getX(), center.getY()
#         p1 = Point(x+w, y+h)
#         p2 = Point(x-w, y-h)
#         self.xmin, self.ymin = x-w, y-h
#         self.xmax, self.ymax = x+w, y+h
#         self.rect = Rectangle(p1, p2)
#         self.rect.draw(win)
#         self.label = Text(center, label)
#         self.label.draw(win)
#         self.color1, self.color2 = 'moccasin', 'red'
#         self.active = True
#
#     def clicked(self, p):
#         return ((self.xmin <= p.getX() <= self.xmax) and
#                 (self.ymin <= p.getY() <= self.ymax) and
#                 self.active)
#
#     def getLabel(self):
#         return self.label.getText()
#
#     def activate(self):
#         self.label.setFill('black')
#         self.rect.setWidth(2)
#         self.active = True
#         self.rect.setFill(self.color1)
#
#     def deactivate(self):
#         self.label.setFill('darkgrey')
#         self.rect.setWidth(1)
#         self.active = False
#         self.rect.setFill(self.color2)
#
#     def setColor(self, color1, color2):
#         self.color1, self.color2 = color1, color2
#         self.rect.setFill(color1)
#
# class InputDialog:
#     def __init__(self, win, position, saved_text=""):
#         self.selected_color = None
#
#         self.rect = Rectangle(position, Point(position.getX() + 10, position.getY() - 0.5))
#         self.rect.draw(win)
#
#         self.entry = Entry(Point(position.getX() + 5, position.getY() - 0.25), 20)
#         self.entry.draw(win)
#         self.entry.setText(saved_text)
#
#         self.color1, self.color2 = 'moccasin', 'red'
#         self.activate()
#
#     def clicked(self, p):
#         return ((self.rect.getP1().getX() <= p.getX() <= self.rect.getP2().getX()) and
#                 (self.rect.getP2().getY() <= p.getY() <= self.rect.getP1().getY()))
#
#     def activate(self):
#         self.rect.setWidth(0.5)
#         self.rect.setFill(self.color1)
#         self.entry.setFill('moccasin')
#
#     def setColor(self, color1, color2):
#         self.color1, self.color2 = color1, color2
#         self.rect.setFill(color1)
#
#     def toggleColor(self, colors):
#         if self.selected_color is None or self.selected_color not in colors:
#             self.selected_color = colors[0]
#         else:
#             current_index = colors.index(self.selected_color)
#             next_index = (current_index + 1) % len(colors)
#             self.selected_color = colors[next_index]
#
#         self.setColor(self.selected_color, self.selected_color)
#
# class DayScreen:
#     def __init__(self, header, day_of_week):
#         self.day_of_week = day_of_week
#         self.win = win = GraphWin(f'{day_of_week} Chart', 800, 800)
#         win.setBackground('orange')
#         win.setCoords(0, 0, 20, 20)
#
#         self.elements = []
#         self.buttons = []
#         self.input_dialogs = []
#         self.saved_texts = [""] * 15
#
#         self.days = []
#
#         self.load_from_file()
#         for i in range(15):
#             position = Point(5, 18 - i)
#             saved_text = self.load_saved_text(i)
#             input_dialog = InputDialog(win, position, saved_text)
#             self.input_dialogs.append(input_dialog)
#             self.days.append(input_dialog.entry.getText())
#
#         self.buttons.append(Button(win, Point(18, 19), 1, 0.5, "Exit"))
#
#         title = Text(Point(10, 19.5), header)
#         title.draw(win)
#         title.setSize(26)
#         title.setFace('courier')
#
#         for button in self.buttons:
#             button.setColor('moccasin', 'red')
#             button.activate()
#
#     def getButton(self):
#         while True:
#             p = self.win.getMouse()
#
#             for button in self.buttons:
#                 if button.clicked(p):
#                     return button.getLabel()
#
#             for input_dialog in self.input_dialogs:
#                 if input_dialog.clicked(p):
#                     colors = []
#                     input_dialog.toggleColor(['red', 'green', 'blue', 'yellow', 'moccasin'])
#                     colors.append(input_dialog.selected_color)
#                     self.days.append(colors[-1])
#                     self.save_text(input_dialog)
#
#     def save_text(self, input_dialog):
#         index = self.input_dialogs.index(input_dialog)
#         self.saved_texts[index] = input_dialog.entry.getText()
#
#     def load_saved_text(self, index):
#         if 0 <= index < len(self.saved_texts):
#             return self.saved_texts[index]
#         else:
#             return ""
#
#     def save_to_file(self):
#         filename = f"{self.day_of_week.lower()}_data.txt"
#         with open(filename, "w") as outfile:
#             for saved_text in self.saved_texts:
#                 outfile.write(saved_text + "\n")
#
#     def load_from_file(self):
#         try:
#             filename = f"{self.day_of_week.lower()}_data.txt"
#             with open(filename, 'r') as infile:
#                 self.saved_texts = infile.read().splitlines()
#                 for i, input_dialog in enumerate(self.input_dialogs):
#                     saved_text = self.load_saved_text(i)
#                     input_dialog.entry.setText(saved_text)
#         except FileNotFoundError:
#             print(f'File "{self.day_of_week.lower()}_data.txt" not found.')
#
#     def run(self):
#         choice = self.getButton()
#
#         if choice == "Exit":
#             self.save_to_file()
#             self.win.close()
#
# def main():
#     days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     for day in days_of_week:
#         screen = DayScreen(day, day_of_week=day)
#         screen.run()
#
# if __name__ == '__main__':
#     main()

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
        self.active = True

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
    def __init__(self, win, position, saved_text=""):
        self.selected_color = None

        self.rect = Rectangle(position, Point(position.getX() + 10, position.getY() - 0.5))
        self.rect.draw(win)

        self.entry = Entry(Point(position.getX() + 5, position.getY() - 0.25), 20)
        self.entry.draw(win)
        self.entry.setText(saved_text)

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
        if self.selected_color is None or self.selected_color not in colors:
            self.selected_color = colors[0]
        else:
            current_index = colors.index(self.selected_color)
            next_index = (current_index + 1) % len(colors)
            self.selected_color = colors[next_index]

        self.setColor(self.selected_color, self.selected_color)

class DayScreen:
    def __init__(self, header, day_of_week, saved_texts=""):
        self.day_of_week = day_of_week
        self.win = win = GraphWin(f'{day_of_week} Chart', 800, 800)
        win.setBackground('orange')
        win.setCoords(0, 0, 20, 20)

        self.elements = []
        self.buttons = []
        self.input_dialogs = []
        self.saved_texts = saved_texts.split("\n") if saved_texts else [""] * 15
        self.days = []

        for i in range(15):
            position = Point(5, 18 - i)
            saved_text = self.load_saved_text(i)
            input_dialog = InputDialog(win, position, saved_text=self.saved_texts[i])
            self.input_dialogs.append(input_dialog)
            self.days.append(input_dialog.entry.getText())

        self.buttons.append(Button(win, Point(18, 19), 1, 0.5, "Exit"))

        title = Text(Point(10, 19.5), header)
        title.draw(win)
        title.setSize(26)
        title.setFace('courier')

        for button in self.buttons:
            button.setColor('moccasin', 'red')
            button.activate()

        #loading saved texts into self.days after creating input dialogs
        self.days = [input_dialog.entry.getText() for input_dialog in self.input_dialogs]

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
                    self.save_text(input_dialog)

    def save_text(self, input_dialog):
        index = self.input_dialogs.index(input_dialog)
        self.saved_texts[index] = input_dialog.entry.getText()

    def load_saved_text(self, index):
        if 0 <= index < len(self.saved_texts):
            return self.saved_texts[index]
        else:
            return ""

    def save_to_file(self):
        filename = f"{self.day_of_week.lower()}_data.txt"
        with open(filename, "w") as outfile:
            for saved_text in self.saved_texts:
                outfile.write(saved_text + "\n")

    def load_from_file(self):
        try:
            filename = f"{self.day_of_week.lower()}_data.txt"
            with open(filename, 'r') as infile:
                self.saved_texts = infile.read().splitlines()
                for i, input_dialog in enumerate(self.input_dialogs):
                    saved_text = self.load_saved_text(i)
                    input_dialog.entry.setText(saved_text)
        except FileNotFoundError:
            print(f'File "{self.day_of_week.lower()}_data.txt" not found.')

    def run(self):
        choice = self.getButton()

        if choice == "Exit":
            self.save_to_file()
            self.win.close()

def main():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days_of_week:
        screen = DayScreen(day, day_of_week=day)
        screen.run()

if __name__ == '__main__':
    main()
