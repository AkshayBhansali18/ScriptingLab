import math
def HourMinute(num):
    hours=math.floor(num/60)
    mins=num%60
    print(hours,":",mins)
HourMinute(45)
