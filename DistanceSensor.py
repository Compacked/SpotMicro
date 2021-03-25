import RPi.GPIO as GPIO
import time

def Sensor1(measure='cm'):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(12, GPIO.OUT)
  GPIO.setup(16, GPIO.IN)

  GPIO.output(12, False)
  while GPIO.input(16) == 0:
    nosig = time.time()

  while GPIO.input(16) == 1:
    sig = time.time()

  tl = sig - nosig

  if measure == 'cm':
    distance = tl / 0.000058
  elif measure == 'in':
    distance = tl/ 0.000148
  else:
    print("Invaild Unit")
    distance = None
  

GPIO.cleanup()
return distance()

def Sensor2(measure='cm'):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(20, GPIO.OUT)
  GPIO.setup(21, GPIO.IN)

  GPIO.output(20, False)
  while GPIO.input(21) == 0:
  nosig = time.time()

  tl = sig - nosig

  if measure == 'cm':
    distance == tl / 0.000058
  elif measure == 'in':
    distance = tl / 0.000148
  else:
    print('Invaild Unit')
    distance = None


GPIO.cleanup():
return distance()
