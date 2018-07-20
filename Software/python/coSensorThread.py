import Adafruit_BBIO.GPIO as GPIO
import time
import common
import parseData
import processRequest
import bluetoothSockets

def co(socket):
  GPIO.setup("P8_14", GPIO.OUT)
  while(1==1):
    bluetoothSockets.ReceiveData(socket)
    if (common.CO_status == "1" and common.coSensorStatus == "0"):
       GPIO.output("P8_14", GPIO.HIGH)
       processRequest.CoSensor(common.CO_status)
    if GPIO.input("P8_14"):
       common.coSensorStatus = "1"
    else:
       if (common.coSensorStatus == "1"):
          processRequest.coSensor("0")
          common.coSensorStatus = "0"
    common.coSensorData = ""
    time.sleep(5)
