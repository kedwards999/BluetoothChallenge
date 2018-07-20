#include <SoftwareSerial.h>
SoftwareSerial BTserial(3, 4);
char dataBuffer[81]; 
String stringBuffer;
int pirPin = 8;               // choose the input pin (for PIR sensor)

void setup(){
  BTserial.begin(9600);
  Serial.begin(9600);
  pinMode(pirPin, OUTPUT);     // declare sensor as input
  ClearBuffer();
  digitalWrite(pirPin,HIGH);   
  while (!BTserial.available())
  {
    // Wait for a connected message from the HHS Controller
  } // if(!BTserial.available())
      BTserial.readBytes(dataBuffer,80);
      delay(10000);
   
} // End setup()

void loop(){

  CheckForMessage();
         
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

void ProcessRequest()
{
  // Source_Adapter_Id Destination_ Adapter_Id Max_Transmission_Count Status Data
  // 000               002                     02                     0/1
  
  if(stringBuffer.substring(0,3) == "000" && stringBuffer.substring(3,6) == "002")
  {
    if(stringBuffer.substring(8,9) == "0")
    {
      digitalWrite(pirPin,LOW);
    }
    else
    {
      digitalWrite(pirPin,HIGH);
    } // End if(stringBuffer.substring(8,9) == "0")
    Serial.println(stringBuffer);
  } // End if(stringBuffer.substring(0,3) == "000" && stringBuffer.substring(3,6) == "002")
} // End ProcessRequest()
