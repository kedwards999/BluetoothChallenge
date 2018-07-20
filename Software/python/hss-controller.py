import Adafruit_BBIO.GPIO as GPIO
import serial
import bluetooth
import time
from threading import Thread
import alert
import bluetoothSockets
import pirSensorThread
import lightThread
import garageThread
import coSensorThread
import gasSensorThread
import rangeThread

pirSensorStatus = "0";
bluetoothAddress = ["00:14:03:06:68:26", # PIR Sensor
                    "00:14:03:06:68:93", # Light 1
                    "00:14:03:06:67:21", # Light 2
                    "00:14:03:06:65:0B", # Garage Door
                    "00:14:03:06:68:3D", # CO Sensor
                    "00:14:03:05:08:37", # GAS Sensor
                    "00:14:03:06:68:9A"] # Gas Range

pirSocket = bluetoothSockets.CreateSocket()
bluetoothSockets.ConnectSocket(pirSocket, bluetoothAddress[0], 1)
t1 = Thread(target=pirSensorThread.pir, args=(pirSocket,))
t1.start()

light1Socket = bluetoothSockets.CreateSocket()
bluetoothSockets.ConnectSocket(light1Socket, bluetoothAddress[1], 1)
t2 = Thread(target=lightThread.light1, args=(light1Socket,))
t2.start()

light2Socket = bluetoothSockets.CreateSocket()
bluetoothSockets.ConnectSocket(light2Socket, bluetoothAddress[2], 1)
t3 = Thread(target=lightThread.light2, args=(light2Socket,))
t3.start()

garageSocket = bluetoothSockets.CreateSocket()
bluetoothSockets.ConnectSocket(garageSocket, bluetoothAddress[3], 1)
t4 = Thread(target=garageThread.garageDoor, args=(garageSocket,))
t4.start()


coSocket = bluetoothSockets.CreateSocket()
bluetoothSockets.ConnectSocket(coSocket, bluetoothAddress[4], 1)
t5 = Thread(target=coSensorThread.coSendor, args=(coSocket,))
t5.start()

gasSocket = bluetoothSockets.CreateSocket()
bluetoothSockets.ConnectSocket(gasSocket, bluetoothAddress[5], 1)
t6 = Thread(target=gasSensorThread.gasSendor, args=(coSocket,))
t6.start()

rangeSocket = bluetoothSockets.CreateSocket()
bluetoothSockets.ConnectSocket(rangeSocket, bluetoothAddress[6], 1)
t7 = Thread(target=rangeThread.gasRange, args=(coSocket,))
t7.start()

while (1 == 1):
  time.sleep(10)
