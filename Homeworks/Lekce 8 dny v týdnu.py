def num_days(date1, date2):
    if date1 > date2:
        date1, date2 = date2, date1
    num_days= 0

    while date1 < date2:
        date1 = increase(date1)
        num_days += 1
    return num_days

def increase(date):
    y,m,d = date
    if m == 2 and d in [28, 29]:
        if is_leap(y) and d == 28:
            date = (y,m,d+1) 
        else:
            date = (y,m+1,d)
    elif m in [1,3,5,7,8,10] and d == 31:
        date = (y,m+1,1)
    elif m == 12 and d == 31:
        date = (y+1,1,1)
    else:
        date = (y,m,d+1)
    
    return date

def is_leap(y):
    return ((y % 400 == 0) or (y % 4 ==0 and y % 100 != 0))
    


def weekday(date,relative_date=(1970,1,1),relative_weekday=4):
    if date < relative_date:
        return -1
     
    elif not is_leap(date[0]) and date[1:] == (2,29):
        print("Neexistující datum!")
        return 0
    
    days = num_days(relative_date, date)
    weekday = (days + relative_weekday)%7
    print(weekday)
    return weekday

date = (1970,1,2)
weekday(date)