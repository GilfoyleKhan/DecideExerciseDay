days="""
    1.monday
    2.tuesday
    3.wednesday
    4.thrusday
    5.friday
    6.saturday
    7.sunday
    """
week=int(input("How many week ?     >"))
print(days)
day=int(input("what day is today(insert number) ?     >"))

import evenodd
decide_week=evenodd.even_odd(week)
decide_day=evenodd.even_odd(day)

if decide_week==True:#odd week
    if decide_day==True:#odd day
        print("Train your body")
    else:
        print("Train your leg")
else:#even week
    if decide_day==True:#odd day
        print("Train your leg")
    else:
        print("Train your body")

