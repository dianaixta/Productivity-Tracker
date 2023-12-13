from graphics import *
from mainscreen import mainScreen
from instructscreen import Instructions
from dayscreen import *

#This program launches the Productivity app by opening the instructions screen, then the mainScreen, then the DayScreen
class ProductivityApp:
    def __init__(self):
        instr = Instructions()
        instr.getChoice()

ProductivityApp()
