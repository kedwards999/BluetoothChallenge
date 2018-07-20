import Adafruit_BBIO.GPIO as GPIO
import time
import bluetoothSockets
import processRequest

def range(socket):
  GPIO.setup("P8_15", GPIO.IN)
  while(1==1):
    if GPIO.input("P8_15"):
       sendcount=socket.send("000007021$")
    else:
       sendcount=socket.send("000007020$")
    time.sleep(5)
