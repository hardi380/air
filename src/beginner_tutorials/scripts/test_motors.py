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

#Test
print("vorwärts links - 1s")
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.HIGH)
GPIO.output(pin4, GPIO.LOW)
time.sleep(1)

print("vorwärts rechts - 1s")
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.HIGH)
GPIO.output(pin4, GPIO.LOW)
time.sleep(3)

print("vorwärts - 1s")
GPIO.output(pin1, GPIO.HIGH)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.HIGH)
GPIO.output(pin4, GPIO.LOW)
time.sleep(1)
    
print("stop 2s")
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)
time.sleep(2)
    
print("rückwärts - 1s")
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.HIGH)
GPIO.output(pin3, GPIO.LOW)
GPIO.output(pin4, GPIO.HIGH)
time.sleep(1)

print("stop")
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)
time.sleep(1)

print("ende full speed")
GPIO.cleanup()

print("(soft) pwm Ansteuerung über Pins 16 und 19 (1 Motor)")
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
pwm=GPIO.PWM(pin1, 50)  # Frequenz [Hz]
pwm.start(0)		# Initialer Duty Cycle

print("PWM duty cycle neu: 50%")
pwm.ChangeDutyCycle(50)
time.sleep(2)

print("PWM duty cycle neu: 30%")
pwm.ChangeDutyCycle(30)
time.sleep(2)

pwm.stop()
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)

print("ende PWM Ansteuerung")
GPIO.cleanup()

