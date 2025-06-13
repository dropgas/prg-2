import datetime
def current_date():
    from datetime import time
    print(datetime.datetime.now())
def enter_date():
    y=int(input("enter the year"))
    m=int(input("enter the month"))
    d=int(input("enter the day"))
    z=print(z)
def time_diff():
    d1=datetime.datetime.now.strpttime(x,"%y-%-m-%d")
    y=int(input("enter the year"))
    m=int(input("enter the month"))
    d=int(input("enter the day"))
    d2=datetime.datetime.strpttime(x,"%y-%-m-%d")
    diff=abs(d2-d1)
    print(diff)
while True:
    print("1.)current date,2.enter date,3.time difference from current date")
    y=int(input("enter your option:"))
    if y==1:
        current_date()
    elif y==2:
        enter_date()
    elif y==3:
        time_diff()
    else:
        print("error")
