import RPi.GPIO as GPIO
import time

#GPIO Pins zuweisen (in bcm numbering)
pin1 = 16
pin2 = 19
pin3 = 26
pin4 = 20


# GPIO-Modus festlegen Motor
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM) # use bcm numbering for pins
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

print("vorwärts rechts - 1s")
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.HIGH)
GPIO.output(pin4, GPIO.LOW)
time.sleep(3)
