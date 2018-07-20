#include <SoftwareSerial.h>
SoftwareSerial BTserial(3, 4);
char dataBuffer[81]; 
String stringBuffer;
int pirPin = 8;               
int pirPinVal = LOW; 
int countHeart = 0;

boolean alertSent = false;

void setup(){
  BTserial.begin(9600);
  Serial.begin(9600);
  pinMode(pirPin, INPUT);     // declare sensor as input
  digitalWrite(pirPin,LOW);
  ClearBuffer();
  while (!BTserial.available())
  {
    // Wait for a connected message from the HHS Controller
  } // if(!BTserial.available())
      BTserial.readBytes(dataBuffer,80);
      delay(10000);
      ClearBuffer();
} // End setup()

void loop(){

  CheckForMessage();
  if(alertSent)
    {
      DelaySensorCheck();
      alertSent = false;
    }
    else
    {
      CheckSensor();
      SendHeartbeat();
      delay(10000);
    }
         
} // End loop()

void ClearBuffer()
{
  for (int i = 0; i < 80; i++)
  { 
    dataBuffer[i] = 0; 
  } // End for (int i = 0; i < 80; i++)
} // End ClearBuffer()

void CheckForMessage()
{
  if( BTserial.available()) 
  {
    BTserial.readBytes(dataBuffer,80); 
    stringBuffer = dataBuffer;
    ProcessRequest();
    ClearBuffer();
  } // End if( BTserial.available())
} // End CheckForMessage()

void CheckSensor()
{
    pirPinVal = digitalRead(pirPin);  // read input value
    
    if (pirPinVal == HIGH) // check if the input is HIGH
    {            
       SendAlert();
       alertSent = true;   
    } // End if (pirPinVal == HIGH)  
} // End CheckSensor()

void DelaySensorCheck()
{
  for (int i=1;i<6;i++)
  {
   delay(6000);
   SendHeartbeat(); 
  } // End for (int i=1;i<6;i++)
} // End DelaySensorCheck()

void ProcessRequest()
{
  // Source_Adapter_Id Destination_ Adapter_Id Max_Transmission_Count Status Data
  // 000               001                     02                     0/1
  
  if(stringBuffer.substring(0,3) == "000" && stringBuffer.substring(3,6) == "001")
  {
    if(stringBuffer.substring(8,9) == "0")
    {
      alertSent = false;
    }
    else
    {
      alertSent = true;
    } // End if(stringBuffer.substring(8,9) == "0")
  } // End if(stringBuffer.substring(0,3) == "000" && stringBuffer.substring(3,6) == "001")
} // End ProcessRequest()

void SendAlert()
{
  // Source_Adapter_Id Destination_ Adapter_Id Max_Transmission_Count Status Data
  // 001               000                     02                     1
  BTserial.print("001000021$");
}

void SendAllClear()
{
  BTserial.print("001000020$");
  // Source_Adapter_Id Destination_ Adapter_Id Max_Transmission_Count Status Data
  // 001               000                     02                     0
  BTserial.print("001000020$");
} // End SendAllClear()

void SendHeartbeat()
{
  //ClearBuffer();
  // Source_Adapter_Id Destination_ Adapter_Id Max_Transmission_Count Status Data
  // 001               000                     02                     H
  BTserial.print("00100002H$");
  countHeart = countHeart +1;
} // End SendAllClear()
