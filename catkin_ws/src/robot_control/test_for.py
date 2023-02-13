from robot_control_class import RobotControl

rc=RobotControl()

list1=rc.get_laser_full()

higher=-1

for values in list1:
    if(higher<values):
        higher=values
print("The highest value is %f" %higher)