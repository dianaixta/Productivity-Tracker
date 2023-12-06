from graphics import *

win = GraphWin('Draw a box and save coordinates', 400, 400, autoflush=False)
p1 = None
rect = None

def samePoint(p1, p2):
    ptype = type(Point(200, 200))
    areSame = False
    if (type(p1) == ptype) & (type(p2) == ptype):
        sameX = p1.getX() == p2.getX()
        sameY = p1.getY() == p2.getY()
        if sameX & sameY:
            areSame = True
    return areSame

def currentlyDragging(p1, p2):
    ptype = type(Point(200, 200))
    dragging = False
    if (type(p1) == ptype) & (type(p2) == ptype):
        sameX = p1.getX() == p2.getX()
        sameY = p1.getY() == p2.getY()
        if not (sameX & sameY):
            dragging = True
    return dragging

def checkState(p1, p2):

    if (p1 == None) & (p2 != None):
        return 'start'
    elif samePoint(p1, p2):
        # Currently never triggers end
        return 'end'
    elif currentlyDragging(p1, p2):
        return 'drag'
    else:
        return 'empty'

while True:
    p2 = win.checkMouse()
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
            p1 = None
            try:
                rect.setFill('purple')
                rect.draw(pStart, pEnd)
            except:
                pass
    update(4)
    if p2:
        p1 = p2.clone()
    else:
        p1 = p2

    # Close window if user hits q
    key = win.checkKey()
    if key == 'q':
        break
win.close()


#add color for each category through user input
#make it stay
#make it easy to edit
