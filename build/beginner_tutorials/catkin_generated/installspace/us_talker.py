#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
 
#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#GPIO Pins zuweisen
GPIO_TRIGGER = 5
GPIO_ECHO = 6
 
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

 
def distanz():
    pub = rospy.Publisher('dist', String, queue_size=10)
    rospy.init_node('distanz', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartZeit = time.time()
    StopZeit = time.time()
 
    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()
 
    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()
 
    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz = (TimeElapsed * 34300) / 2
    distanzStr = str(distanz)

    while not rospy.is_shutdown():
        rospy.loginfo(distanzStr)
        pub.publish(distanzStr)
        rate.sleep()

print('start')
if __name__ == '__main__':
    try:
        distance()
    except rospy.ROSInterruptException:
        pass
