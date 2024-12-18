#! /usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header
from sensor_msgs.msg import JointState
from intera_core_msgs.srv import SolvePositionFK, SolvePositionFKRequest

def fk_service_client(angles):
    service_name = "ExternalTools/right/PositionKinematicsNode/FKService"
    fk_service_proxy = rospy.ServiceProxy(service_name, SolvePositionFK)
    fk_request = SolvePositionFKRequest()
    joints = JointState()
    joints.name = ['right_j0', 'right_j1', 'right_j2', 'right_j3','right_j4', 'right_j5', 'right_j6']
<<<<<<< HEAD:lab5/src/ik/src/fk.py
    joint_input = angles
    joints.position = joint_input
=======
    # YOUR CODE HERE
    joint_input = []
    
>>>>>>> 063b531c051e78ca50b48336fa26c4ca7ae43c93:lab5/fk.py
    # Add desired pose for forward kinematics
    joints.position = joint_input
    fk_request.configuration.append(joints)
    # Request forward kinematics from base to "right_hand" link
    fk_request.tip_names.append('right_hand')

    try:
        rospy.wait_for_service(service_name, 5.0)
        response = fk_service_proxy(fk_request)
    except (rospy.ServiceException, rospy.ROSException) as e:
        rospy.logerr("Service call failed: %s" % (e,))
        return 

    # Check if result valid
    if (response.isValid[0]):
        rospy.loginfo("SUCCESS - Valid Cartesian Solution Found")
        rospy.loginfo("\nFK Cartesian Solution:\n")
        rospy.loginfo("------------------")
        rospy.loginfo("Response Message:\n%s", response)
        print(response)
    else:
        rospy.logerr("INVALID JOINTS - No Cartesian Solution Found.")
        return 

    return True


def main():
    rospy.init_node("fk_service_client")
    angles = input('commoa separated 7 joint angles\n')
    angles = angles.split(',')
    angles = [float(angle) for angle in angles]

    fk_service_client(angles)

if __name__ == '__main__':
    main()
