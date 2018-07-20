import Adafruit_BBIO.GPIO as GPIO
import time
import bluetoothSockets
import processRequest

def light1(socket):
  GPIO.setup("P8_9", GPIO.IN)
  while(1==1):
    if GPIO.input("P8_9"):
       sendcount=socket.send("000002021$")
    else:
       sendcount=socket.send("000002020$")
    time.sleep(5)

def light2(socket):
  GPIO.setup("P8_10", GPIO.IN)
  while(1==1):
    if GPIO.input("P8_10"):
       sendcount=socket.send("000003021$")
    else:
       sendcount=socket.send("000003020$")
    time.sleep(5)
