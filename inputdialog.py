from graphics import *

#This program creates the input dialog boxes for the DayScreen window
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
