from adafruit_servokit import ServoKit
import time
import curses
from SpotDistance import Sensor1
from SpotDistance import Sensor2

Sensor1 = distance('cm')
Sensor2 = distance('cm')

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
    

def Forward():
    while True:
        kit.servo[9].angle = 70
        time.sleep(1)
        kit.servo[10].angle = 70
        time.sleep(1)
        kit.servo[11].angle = 70
        time.sleep(1)
        kit.servo[12].angle = 70
    if Sensor1 < 15:
        Backward()
    elif Sensor2 < 15:
        Backward()
    elif char == ord('q'):
        Sleep()
        break

def Backward():
    while True:
        kit.servo[9].angle = 120
        time.sleep(1)
        kit.servo[10].angle = 120
        time.sleep(1)
        kit.servo[11].angle = 120
        time.sleep(1)
        kit.servo[12].angle = 120
    if curDis < 15:
        Forward()
    elif char == ord('q'):
        Sleep()
        break

def Right():
    while True:
            kit.servo[6].angle = 45
            

def Left():
    while True:
        kit.servo[5].angle = 145
        

def Look_Up():
   kit.servo[7].angle = 180
   kit.servo[8].angle = 180
if char == ord('q'):
    break

def Look_Down():
    kit.servo[5].angle = 180
    kit.servo[6].angle = 180
if char = ord('q'):
    Sleep()
    break

def Up_Stairs():
    kit.servo[7].angle = 180
    kit.servo[8].angle = 180
while True:
    kit.servo[9].angle = 70
    time.sleep(1)
    kit.servo[10].angle = 70
    time.sleep(1)
    kit.servo[11].angle = 70
    time.sleep(1)
    kit.servo[12].angle = 70

def Down_Stairs():
    kit.servo[5].angle = 180
    kit.servo[6].angle = 180
while True:
    kit.servo[9].angle = 70
    time.sleep(1)
    kit.servo[10].angle = 70
    time.sleep(1)
    kit.servo[11].angle = 70
    time.sleep(1)
    kit.servo[12].angle = 70

def Sleep():
    kit.servo[1].angle = 0
    kit.servo[2].angle = 0
    kit.servo[3].angle = 0
    kit.servo[4].angle = 0
