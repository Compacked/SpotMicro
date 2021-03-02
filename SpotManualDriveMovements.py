from adafruit_servokit import ServoKit
import time
import curses

kit = ServoKit(channels=16)

screen = curses.initscr():
curses.noecho()
curses.cbreak()
screen.keyboard(True)

def Wake_Up():
    kit.servo[1].angle = 90
    kit.servo[2].angle = 90
    kit.servo[3].angle = 90
    kit.servo[4].angle = 90
    kit.servo[9].angle = 90
    kit.servo[10].angle = 90
    kit.servo[11].angle = 90
    kit.servo[12].angle = 90

def Forward():
    while True:
        kit.servo[5].angle = 70
        time.sleep(1)
        kit.servo[6].angle = 70
        time.sleep(1)
        kit.servo[7].angle = 70
        time.sleep(1)
        kit.servo[8].angle = 70
    if char == ord('q'):
        Sleep()
        break

def Backward():
    while True:
        kit.servo[5].angle = 120
        time.sleep(1)
        kit.servo[6].angle = 120
        time.sleep(1)
        kit.servo[7].angle = 120
        time.sleep(1)
        kit.servo[8].angle = 120
    if char == ord('q'):
        Sleep()
        break

def Right():
    while True:
            kit.servo[5].angle = 70
            time.sleep(1):
            kit.servo[6].angle = 70
            time.sleep(1)
            kit.servo[7].angle = 70
            time.sleep(1)
            kit.servo[8].angle = 70
            time.sleep(1)
            kit.servo[10].angle = 180
            time.sleep(1)
            kit.servo[6].angle = 70
            time.sleep(1)
            kit.servo[7].angle = 70
            time.sleep(1)
            kit.servo[8].angle = 70
            time.sleep(1)
            kit.servo[10].angle = 180
            time.sleep(1)
            kit.servo[6].angle = 70
            time.sleep(1)
            kit.servo[7].angle = 70
            time.sleep(1)
            kit.servo[8].angle = 70
        if char == ord('q'):
            Sleep()
            break

def Left():
    while True:
        kit.servo[5].angle = 70
        time.sleep(1):
        kit.servo[6].angle = 70
        time.sleep(1)
        kit.servo[7].angle = 70
        time.sleep(1)
        kit.servo[8].angle = 70
        time.sleep(1)
        kit.servo[10].angle = 180
        time.sleep(1)
        kit.servo[6].angle = 70
        time.sleep(1)
        kit.servo[7].angle = 70
        time.sleep(1)
        kit.servo[8].angle = 70
        time.sleep(1)
        kit.servo[10].angle = 180
        time.sleep(1)
        kit.servo[6].angle = 70
        time.sleep(1)
        kit.servo[7].angle = 70
        time.sleep(1)
        kit.servo[8].angle = 70
    if char == ord('q'):
        Sleep()
        break

def Look_Up():
   kit.servo[3].angle = 180
   kit.servo[4].angle = 180
if char == ord('q'):
    break

def Look_Down():
    kit.servo[1].angle = 180
    kit.servo[2].angle = 180
if char = ord('q'):
    Sleep()
    break

def Sleep():
    kit.servo[1].angle = 0
    kit.servo[2].angle = 0
    kit.servo[3].angle = 0
    kit.servo[4].angle = 0
    kit.servo[9].angle = 0
    kit.servo[10].angle = 0
    kit.servo[11].angle = 0
    kit.servo[12].angle = 0
