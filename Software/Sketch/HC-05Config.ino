#include <SoftwareSerial.h>
SoftwareSerial mySerial(3, 4); // RX, TX

// Unplug HC-05, Hold Reset Button while pluging the HC-05 in.
// mySerial should be 38400
// Serial Monitor - Both NL & CR
// RX -> TX, TX -> RX

void setup() {
Serial.begin(9600);
pinMode(2,OUTPUT); digitalWrite(2,HIGH);
Serial.println("Enter AT commands:");

mySerial.begin(38400);
}

void loop()
{
if (mySerial.available())
   Serial.write(mySerial.read());
if (Serial.available())
   mySerial.write(Serial.read());
}
