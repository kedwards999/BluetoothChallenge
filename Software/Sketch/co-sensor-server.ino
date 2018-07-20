#include <SoftwareSerial.h>
SoftwareSerial BTserial(3, 4);

Chrono mqTime;
int heatTime = 60000; 
int measurementTime = 90000;
int pwmPower = 87;
int powerPin = 10;

char dataBuffer[81]; 
String stringBuffer;

const int AOUTpin=0; 
const int DOUTpin=8; 
int COlimit;
int COvalue;

void setup() {
  BTserial.begin(9600);
  Serial.begin(9600);
  ClearBuffer();
  
  while (!BTserial.available())
  {
    // Wait for a connected message from the HHS Controller
  } // if(!BTserial.available())
  BTserial.readBytes(dataBuffer,80);

pinMode(DOUTpin, INPUT); 
} // End setup()

void loop() {

  HeatingPhase();
  deplay(heatTime);
  MeasurementPhase();
  delay(measurementTime);
  COlimit = digitalRead(DOUTpin);
  COvalue = analogRead(AOUTpin); 
  SendStatus(); 
} // End loop()

void ClearBuffer()
{
  for (int i = 0; i < 80; i++)
  { 
    dataBuffer[i] = 0; 
  } // End for (int i = 0; i < 80; i++)
} // End ClearBuffer()

void HeatingPhase()
{
  analogWrite(powerPin, 255);
}

void MeasurementPhase()
{
  analogWrite(powerPin, pwmPower);
}


void SendStatus()
{
  // Source_Adapter_Id Destination_ Adapter_Id Max_Transmission_Count Status Data
  // 005               000                     02                     0/1
  if (COlimit == HIGH)
  {
    BTserial.print("005000021$");
  }
  else
  {
    BTserial.print("005000020$");
  }
  
} // End SendStatus()







