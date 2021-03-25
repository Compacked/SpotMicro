from adafruit_servokit import ServoKit
import keyboard as keyboard
import time
from SpotDistance import Sensor1
from SpotDistance import Sensor2]

Sensor1 = distance('cm')
Sensor2 = distance('cm')


kit = ServoKit(channels=16)

def Wake_up():
        if keyboard.is_pressed('s'):
            kit.servo[1].angle = 90
            kit.servo[2].angle = 90
            kit.servo[3].angle = 90
            kit.servo[4].angle = 90


def Forward():
    while True:
        if keyboard.is_pressed('1'):
            kit.servo[9].angle = 70
            time.sleep(1)
            kit.servo[10].angle = 70
            time.sleep(1)
            kit.servo[11].angle = 70
            time.sleep(1)
            kit.servo[12].angle = 70
        elif curDis < 15:
            break
        elif Sensor1 > 15:
            Backward()
        elif Sensor2 > 15:
            Backward()
        elif keyboard.is_pressed('q'):
            Sleep()
            break

def Backward():
    while True:
        if keyboard.is_pressed('2'):
            kit.servo[9].angle = 120
            time.sleep(1)
            kit.servo[10].angle = 120
            time.sleep(1)
            kit.servo[11].angle = 120
            time.sleep(1)
            kit.servo[12].angle = 120
        elif curDis < 15:
            Forward()
        elif keyboard.is_pressed('q'):
            Sleep()
            break

def Right():
    while True:
        if keyboard.is_pressed('3'):
            kit.servo[6].angle = 45

def Left():
    while True:
        if keyboard.is_pressed('4'): 
            kit.servo[5].angle = 145
            
        
def Look_up():
    while True:
        if keyboard.is_pressed('5'):
           kit.servo[7].angle = 180
           kit.servo[8].angle = 180
        elif keyboard.is_pressed('q'):
            Sleep()
            break

def Look_Down():
    while True:
        if keyboard.is_pressed('6'):
            kit.servo[5].angle = 180
            kit.servo[6].angle = 180
        elif keyboard.is_pressed('q'):
            Sleep()
            break

def Up_Stairs():
    while True:
        if keyboard.is_pressed('7'):
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
    while True:
        if keyboard.is_pressed('o'):
            kit.servo[1].angle = 0
            kit.servo[2].angle = 0
            kit.servo[3].angle = 0
            kit.servo[4].angle = 0
            
while True:
    Wake_up()
    Forward()
    Backward()
    Right()
    Left()
    Sleep()
    Look_up()
    Look_Down()
    

    
