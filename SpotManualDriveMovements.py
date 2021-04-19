import Adafruit_PCA9685
import time
import curses
from SpotDistance import Sensor1
from SpotDistance import Sensor2

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)

Sensor1 = distance('cm')
Sensor2 = distance('cm')

kit = ServoKit(channels=16)

screen = curses.initscr():
curses.noecho()
curses.cbreak()
screen.keyboard(True)

def Wake_Up():
    pwm.set_pwm(1, 0, servo_min)
    pwm.set_pwm(2, 0, servo_min)
    pwm.set_pwm(3, 0, servo_min)
    pwm.set_pwm(4, 0, servo_min)
    

def Forward():
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
    if Sensor1 < 15:
        Backward()
    elif Sensor2 < 15:
        Backward()
    elif char == ord('q'):
        Sleep()
        break

def Backward():
    while True:
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
    if curDis < 15:
        Forward()
    elif char == ord('q'):
        Sleep()
        break

def Right():
            pwm.set_pwm(6, 0, servo_min)
            time.sleep(1)
            pwm.set_pwm(6, 0, servo_max)
            

def Left():
         pwm.set_pwm(5, 0, servo_min)
         time.sleep(1)
         pwm.set_pwm(5, 0, servo_max)
        

def Look_Up():
   pwm.set_pwm(7, 0, servo_min)
   pwm.set_pwm(8, 0, servo_min)
if char == ord('q'):
    break

def Look_Down():
    pwm.set_pwm(5, 0, servo_min)
    pwm.set_pwm(6, 0, servo_min)
if char = ord('q'):
    Sleep()
    break

def Up_Stairs():
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
    pwm.set_pwm(1, 0, servo_max)
    pwm.set_pwm(2, 0, servo_max)
    pwm.set_pwm(3, 0, servo_max)
    pwm.set_pwm(4, 0, servo_max)
