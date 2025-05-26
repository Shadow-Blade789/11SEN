from graphics import *

def main():
    win = GraphWin("flàgo", 2000, 1000)
    r = Rectangle(500, 500)
    r.setFill('White')
    r.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()