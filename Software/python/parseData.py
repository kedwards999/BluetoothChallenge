import common


def parseBluetoothData(bluetoothData):
  common.source_Adapter_Id = bluetoothData[0:3]
  common.destination_Adapter_Id = bluetoothData[3:6]
  common.max_Transmission_Count = bluetoothData[6:8]
  common.status = bluetoothData[8:9]
 
def parseGarageDoorData(bluetoothData):
  common.GDD_source_Adapter_Id = bluetoothData[0:3]
  common.GDD_destination_Adapter_Id = bluetoothData[3:6]
  common.GDD_max_Transmission_Count = bluetoothData[6:8]
  common.GDD_status = bluetoothData[8:9]

def parseCoSensorData(bluetoothData):
  common.CO_source_Adapter_Id = bluetoothData[0:3]
  common.CO_destination_Adapter_Id = bluetoothData[3:6]
  common.CO_max_Transmission_Count = bluetoothData[6:8]
  common.CO_status = bluetoothData[8:9]

def parseGasSensorData(bluetoothData):
  common.GAS_source_Adapter_Id = bluetoothData[0:3]
  common.GAS_destination_Adapter_Id = bluetoothData[3:6]
  common.GAS_max_Transmission_Count = bluetoothData[6:8]
  common.GAS_status = bluetoothData[8:9]

def parseRangeSensorData(bluetoothData):
  common.RANGE_source_Adapter_Id = bluetoothData[0:3]
  common.RANGE_destination_Adapter_Id = bluetoothData[3:6]
  common.RANGE_max_Transmission_Count = bluetoothData[6:8]
  common.RANGE_status = bluetoothData[8:9]

def parsePirSensorData(bluetoothData):
  common.PSD_source_Adapter_Id = bluetoothData[0:3]
  common.PSD_destination_Adapter_Id = bluetoothData[3:6]
  common.PSD_max_Transmission_Count = bluetoothData[6:8]
  common.PSD_status = bluetoothData[8:9]
