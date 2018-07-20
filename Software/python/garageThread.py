import Adafruit_BBIO.GPIO as GPIO
import time
import bluetoothSockets
import common
import parseData

def garageDoor(socket):
  GPIO.setup("P8_11", GPIO.OUT)
  GPIO.setup("P8_17", GPIO.OUT)
  GPIO.output("P8_17", GPIO.LOW)
  while(1==1):
    bluetoothSockets.ReceiveData(socket)
    if (common.GDD_status == "1"):
      GPIO.output("P8_11", GPIO.HIGH)
    else:
      GPIO.output("P8_11", GPIO.LOW)
    common.garageDoorData = ""
    time.sleep(5)
