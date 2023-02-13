from robot_control_class import RobotControl

number=int(input("Enter any number between 0 and 719"))

rc=RobotControl()

ans=rc.get_laser(number)

print("The distance for given number is %f" % ans)