day=1
month=1
year=1900
week=1
sum=0
sum1=0
month_tab={1:31,3:31,5:31,7:31,8:31,10:31,12:31,9:30,4:30,6:30,11:30}
months=range(1,13)
del months[1]
while year<=2000:
    if week>7:
        week=week-7
    if month==2:
        if (year==2000) or (year%100!=0 and year%4==0):
            if day>29:
                day=day-29
                month=month+1
        else:
            if day>28:
                day=day-28
                month=month+1                        
    if month in months:
        if day >month_tab.get(month):
            day=day-month_tab.get(month)
            month=month+1
            if month>=13:
                month=month-12
                year=year+1
    if week==7 and day==1 and year>=1901 and year<=2000:
        sum=sum+1
    day=day+1
    week=week+1
print sum

