#!/usr/bin/env python
import rospy
from std_msgs.msg import String
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


def callback(data):
    global cmd
    cmd = data.data
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    controll(cmd)

def controll(cmd):
    if cmd == "left":
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(pin3, GPIO.HIGH)
        GPIO.output(pin4, GPIO.LOW)
    elif cmd == "straight":
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(pin3, GPIO.HIGH)
        GPIO.output(pin4, GPIO.LOW)
        time.sleep(1)

    print("ende full speed")
    GPIO.cleanup()
   
def motor_controller():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('motor_controller', anonymous=True)

    rospy.Subscriber("motor_cmd", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()