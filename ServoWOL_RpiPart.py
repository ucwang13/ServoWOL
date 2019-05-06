# External module imports
from time import sleep
import RPi.GPIO as GPIO

# Pin Definitions
DaOnlyPin = 17 # GPIO17 BCM aka Pin 11

# Pin Setup
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(DaOnlyPin, GPIO.OUT) # set DaOnlyPin as output

# The Code
try:
    GPIO.output(DaOnlyPin, GPIO.HIGH) # set the pin to HIGH 3.3
    GPIO.output(DaOnlyPin, GPIO.LOW) # set it back to LOW 0V
except KeyboardInterrupt:
    print("Interrupted")
finally:
    GPIO.setup(DaOnlyPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #inputPullDown
    GPIO.cleanup() # always clean up after yourself
    print("Arduino activated")
