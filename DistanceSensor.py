import RPi.GPIO as GPIO
import time

def distance(measure='cm'):
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
    distance] = tl/ 0.000148
  else:
    print("No unit")
    distance = None
  

GPIO.cleanup()
return distance()
