import bluetooth
import time
import common
import parseData

def CreateSocket():
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  return sock

def ConnectSocket(sock, serverAddr, port):
  sock.connect((serverAddr, port))
  sendcount=sock.send("Hello Bluetooth Device!!!")

def ReceiveData(socket):
    receiveBuffer = ""
    bluetoothData = ""
    dataNotReceived = True

    while (dataNotReceived):
       receiveBuffer = socket.recv(80)
       bluetoothData = bluetoothData + receiveBuffer
       if (receiveBuffer.endswith("$")):
          dataNotReceived = False
       if (dataNotReceived):
         x = 1
       else:
         parseData.parseBluetoothData(bluetoothData)
         populateBluetoothRecord(bluetoothData)

def populateBluetoothRecord(bluetoothData):
  if (common.destination_Adapter_Id == "000" and common.source_Adapter_Id == "001"):
    parseData.parsePirSensorData(bluetoothData)
    common.pirSensorData = bluetoothData

  if (common.destination_Adapter_Id == "000" and common.source_Adapter_Id == "004"):
    parseData.parseGarageDoorData(bluetoothData)

    common.garageDoorData = bluetoothData

  if (common.destination_Adapter_Id == "000" and common.source_Adapter_Id == "005"):
    parseData.parseCoSensorData(bluetoothData)
    common.coSensorData = bluetoothData

  if (common.destination_Adapter_Id == "000" and common.source_Adapter_Id == "006"):
    parseData.parseGasSensorData(bluetoothData)
    common.gasSensorData = bluetoothData

