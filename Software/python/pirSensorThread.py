import Adafruit_BBIO.GPIO as GPIO
import time
import common
import parseData
import processRequest
import bluetoothSockets

def pir(socket):
  GPIO.setup("P8_16", GPIO.OUT)
  while (1 == 1):
     bluetoothSockets.ReceiveData(socket)
     if (common.PSD_status != "H"):
       if (common.PSD_status == "1"):
         processRequest.PirSensor(common.PSD_status)

     if GPIO.input("P8_16"):
        common.pirSensorStatus = "1"
     else:
       if (common.pirSensorStatus == "1"):
           processRequest.PirSensor("0")
           common.pirSensorStatus = "0"
     common.pirSensorData = ""
