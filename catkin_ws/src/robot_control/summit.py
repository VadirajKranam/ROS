from robot_control_class import RobotControl

rc=RobotControl()

def myMethod(a,b,c):
    list1=[]
    list1.append(rc.get_laser_summit(a))
    list1.append(rc.get_laser_summit(b))
    list1.append(rc.get_laser_summit(c))
    return list1
