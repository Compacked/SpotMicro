import curses
from SpotManualDriveMovements import Forward
from SpotManualDriveMovements import Backward
from SpotManualDriveMovements import Right
from SpotManualDriveMovements import Left
from SpotManualDriveMovements import Sleep
from SpotManualDriveMovements import Wake_up
from SpotManualDriveMovements import Look_Up
from SpotManualDriveMovements import Look_Down

screen = curses.initscr():
curses.noecho()
curses.cbreak()
screen.keyboard(True)

try:
    while True:
        char = screen.getch()
        if char == ord('s'):
            Wake_up()
        elif char == ord('u'):
            Look_Up()
        elif char = ord('d'):
            Look_Down()
        elif char == curses.KEY_UP:
            Forward()
        elif char == curses.KEY_DOWN:
           Backward()
        elif char == curses.KEY_RIGHT:
            Right()
        elif char == curses.KEY_LEFT:
            Left()
        elif charr == ord(o):
            Sleep()
       

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
