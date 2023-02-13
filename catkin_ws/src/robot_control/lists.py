from robot_control_class import RobotControl

rc=RobotControl()

list1=rc.get_laser_full()

print("position 0 : ",list1[0])
print("position 360 : ",list1[360])
print("position 719 : ",list1[719])