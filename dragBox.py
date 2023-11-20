from graphics import *

win = GraphWin('Draw a box and save coordinates', 400, 400, autoflush=False)
p1 = None
rect = None

def checkState(p1, p2):
    if (p1 == None) & (p2 != None):
        return 'start'
    elif (p1 != None) & (p2 == None):
        # Currently never triggers end
        return 'end'
    elif (p1 == None) & (p2 == None):
        return 'empty'
    else:
        return 'drag'

while True:
    p2 = win.checkDrag()
    if checkState(p1, p2) == 'start':
        pStart = p2.clone()
    elif checkState(p1, p2) == 'drag':
        if rect:
            rect.undraw()
        rect = Rectangle(pStart, p2)
        rect.setFill('lightblue')
        rect.draw(win)
    elif checkState(p1, p2) in ['end', 'empty']:
        if p1:
            pEnd = p1.clone()
            rect.setFill('purple')
            rect.draw(pStart, pEnd)
        p1 = None
    update(10)
    print(checkState(p1, p2))
    if p2:
        p1 = p2.clone()

    # Close window if user hits q
    key = win.checkKey()
    if key == 'q':
        break
win.close()
