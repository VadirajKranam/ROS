from robot_control_class import RobotControl

rc=RobotControl()

list1=rc.get_laser_full()

dic1={}
dic1["p0"]=list1[0]
dic1["p100"]=list1[100]
dic1["p200"]=list1[200]
dic1["p300"]=list1[300]
dic1["p400"]=list1[400]
dic1["p500"]=list1[500]
dic1["p600"]=list1[600]
dic1["p719"]=list1[719]

print(dic1)

