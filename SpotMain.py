import keyboard as keyboard
import time
from SpotDistance import Sensor1
from SpotDistance import Sensor2
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()


servo_min = 150
servo_max = 600

Sensor1 = distance('cm')
Sensor2 = distance('cm')

pwm.set_pwm_freq(60)


def Wake_up():
        if keyboard.is_pressed('s'):
           pwm.set_pwm(1, 0, servo_min)
           pwm.set_pwm(2, 0, servo_min)
           pwm.set_pwm(3, 0, servo_min)
           pwm.set_pwm(4, 0, servo_min)


def Forward():
    while True:
        if keyboard.is_pressed('1'):
            pwm.set_pwm(9, 0, servo_min)
            pwm.set_pwm(9, 0, servo_max)
            time.sleep(1)
            pwm.set_pwm(10, 0, servo_min)
            pwm.set_pwm(10, 0, servo_max)
            time.sleep(1)
            pwm.set_pwm(11, 0, servo_min)
            pwm.set_pwm(11, 0, servo_max)
            time.sleep(1)
            pwm.set_pwm(12, 0, servo_min)
            pwm.set_pwm(12, 0, servo_max)
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
            pwm.set_pwm(9, 0, servo_max)
            pwm.set_pwm(9, 0, servo_min)
            time.sleep(1)
            pwm.set_pwm(10, 0, servo_max)
            pwm.set_pwm(10, 0, servo_min)
            time.sleep(1)
            pwm.set_pwm(11, 0, servo_max)
            pwm.set_pwm(11, 0, servo_min)
            time.sleep(1)
            pwm.set_pwm(12, 0, servo_max)
            pwm.set_pwm(12, 0, servo_min)
        elif curDis < 15:
            Forward()
        elif keyboard.is_pressed('q'):
            Sleep()
            break

def Right():
    while True:
        if keyboard.is_pressed('3'):
            pwm.set_pwm(6, 0, servo_min)
            time.sleep(1)
            pwm.set_pwm(6, 0, servo_max)

def Left():
    while True:
        if keyboard.is_pressed('4'): 
            pwm.set_pwm(5, 0, servo_min)
            time.sleep(1)
            pwm.set_pwm(5, 0, servo_max)
            
        
def Look_up():
    while True:
        if keyboard.is_pressed('5'):
           pwm.set_pwm(7, 0, servo_min)
           pwm.set_pwm(8, 0, servo_min)
        elif keyboard.is_pressed('q'):
            Sleep()
            break

def Look_Down():
    while True:
        if keyboard.is_pressed('6'):
            pwm.set_pwm(5, 0, servo_min)
            pwm.set_pwm(6, 0, servo_min)
        elif keyboard.is_pressed('q'):
            Sleep()
            break

def Up_Stairs():
    while True:
        if keyboard.is_pressed('7'):
           pwm.set_pwm(7, 0, servo_min)
           pwm.set_pwm(8, 0, servo_min)
        while True:
           pwm.set_pwm(9, 0, servo_min)
           pwm.set_pwm(9, 0, servo_max)
           time.sleep(1)
           pwm.set_pwm(10, 0, servo_min)
           pwm.set_pwm(10, 0, servo_min)
           time.sleep(1)
           pwm.set_pwm(11, 0, servo_min)
           pwm.set_pwm(11, 0, servo_max)
           time.sleep(1)
           pwm.set_pwm(12, 0, servo_min)
           pwm.set_max(12, 0, servo_max)

def Down_Stairs():
    pwm.set_pwm(5, 0, servo_min)
    pwm.set_pwm(6, 0, servo_min)
while True:
    pwm.set_pwm(9, 0, servo_min)
    pwm.set_pwm(9, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(10, 0, servo_min)
    pwm.set_pwm(10, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(11, 0, servo_min)
    pwm.set_pwm(11, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(12, 0, servo_min)
    pwm.set_pwm(12, 0, servo_max)



def Sleep():
    while True:
        if keyboard.is_pressed('o'):
            pwm.set_pwm(1, 0, servo_max)
            pwm.set_pwm(2, 0, servo_max)
            pwm.set_pwm(3, 0, servo_max)
            pwm.set_pwm(4, 0, servo_max)
            
while True:
    Wake_up()
    Forward()
    Backward()
    Right()
    Left()
    Sleep()
    Look_up()
    Look_Down()
