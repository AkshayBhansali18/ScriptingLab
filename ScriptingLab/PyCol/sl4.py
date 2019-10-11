import datetime
def AgeConvert(num):
    now = datetime.datetime.now()
    str=[]
    str=num.split("-")
    year=int(str[2])
    age=now.year-year
    print("Age is",age)
AgeConvert("28-02-1992")

