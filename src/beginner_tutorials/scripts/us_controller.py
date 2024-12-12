import rospy
from std_msgs.msg import String

dist = None

def callback(data):
    global dist
    try:
        dist = float(data.data)
        rospy.loginfo(f"Received dist: {dist}")
    except ValueError:
        rospy.logwarn(f"Invalid dist value received: {data.data}")

def logic(pub):
    global dist
    if dist is not None:
        if dist < 10:
            command = "left"
        else:
            command = "straight"
        rospy.loginfo(f"Publishing command: {command}")
        pub.publish(command)
    else:
        rospy.loginfo("No valid dist value received yet.")

def translate():
    rospy.init_node('listener', anonymous=True)
    pub = rospy.Publisher('motor_cmd', String, queue_size=10)
    rospy.Subscriber("dist", String, callback)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        logic(pub)
        rate.sleep()

if __name__ == '__main__':
    try:
        translate()
    except rospy.ROSInterruptException:
        pass
