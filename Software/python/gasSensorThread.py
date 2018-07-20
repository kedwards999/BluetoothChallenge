import Adafruit_BBIO.GPIO as GPIO
import time
import common
import parseData
import processRequest
import bluetoothSockets

def gas(socket):
  GPIO.setup("P8_15", GPIO.OUT)
  while(1==1):
    bluetoothSockets.ReceiveData(socket)
    if (common.GAS_status == "1" and common.gasSensorStatus == "0"):
       GPIO.output("P8_15", GPIO.HIGH)
       processRequest.CoSensor(common.GAS_status)
    if GPIO.input("P8_15"):
       common.gasSensorStatus = "1"
    else:
       if (common.gasSensorStatus == "1"):
          processRequest.gasSensor("0")
          common.gasSensorStatus = "0"
    common.gasSensorData = ""
    time.sleep(5)
