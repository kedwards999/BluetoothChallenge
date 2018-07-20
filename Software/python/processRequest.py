import alert
import Adafruit_BBIO.GPIO as GPIO

def PirSensor(status):
  if (status == "1"):
     alert.speak("S Warning! Warning! a intruder has been detected!")
     alert.speak("S Warning! Warning! a intruder has been detected!")
     alert.speak("S Warning! Warning! a intruder has been detected!")
     GPIO.output("P8_16", GPIO.HIGH)
  else:
     alert.speak("S The intruder alert has been cleared!")
     GPIO.output("P8_16", GPIO.LOW)

def CoSensor(status):
  if (status == "1"):
     alert.speak("S Warning! Warning! a Carbon Monoxide leak has been detected!")
     alert.speak("S Warning! Warning! a Carbon Monoxide leak has been detected!")
     alert.speak("S Warning! Warning! a Carbon Monoxide leak has been detected!")
     GPIO.output("P8_14", GPIO.HIGH)
  else:

  else:
     alert.speak("S The Carbon Monoxide leak alert has been cleared!")
     GPIO.output("P8_14", GPIO.LOW)


def GasSensor(status):
  if (status == "1"):
     alert.speak("S Warning! Warning! a Natural Gas leak has been detected!")
     alert.speak("S Warning! Warning! a Natural Gas leak has been detected!")
     alert.speak("S Warning! Warning! a Natural Gas leak has been detected!")
     GPIO.output("P8_15", GPIO.HIGH)
  else:
     alert.speak("S The Natural Gas leak alert has been cleared!")
     GPIO.output("P8_15", GPIO.LOW)


  else:
     alert.speak("S The Carbon Monoxide leak alert has been cleared!")
     GPIO.output("P8_14", GPIO.LOW)


def GasSensor(status):
  if (status == "1"):
     alert.speak("S Warning! Warning! a Natural Gas leak has been detected!")
     alert.speak("S Warning! Warning! a Natural Gas leak has been detected!")
     alert.speak("S Warning! Warning! a Natural Gas leak has been detected!")
     GPIO.output("P8_15", GPIO.HIGH)
  else:
     alert.speak("S The Natural Gas leak alert has been cleared!")
     GPIO.output("P8_15", GPIO.LOW)

