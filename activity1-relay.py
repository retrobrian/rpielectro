#Basic on/off relay control
#Expecting Python 3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
status = False
try:
    while True:
        GPIO.output(24, status)
        input('Press [Enter] to toggle relay ' + ('Off' if status else 'On'))
        status = not status
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
