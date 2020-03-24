from datetime import datetime,timedelta

n = int(input())
t =  timedelta(minutes=1)

for i in range(n):

    t1=datetime.strptime(input(),"%a %d %b %Y %H:%M:%S %z")
    t2=datetime.strptime(input(),"%a %d %b %Y %H:%M:%S %z")

    time = int(abs(t2-t1).total_seconds())
    year=time//(365*24*60*60)
    month=time//(31*24*60*60)
    week=time//(7*24*60*60)
    day=time//(24*60*60)
    hour=time//(60*60)
    minute=time//60
    second=minute
    
    if year>0:
        print(year,end="")
        if year==1:
            print(" year ago")
        else:
            print(" years ago")
    elif month>0:
        print(month,end="")
        if month==1:
            print(" month ago")
        else:
            print(" months ago")
    elif week>0:
        print(week,end="")
        if week==1:
            print(" week ago")
        else:
            print(" weeks ago")

    elif day>0:
        print(day,end="")
        if day==1:
            print(" day ago")
        else:
            print(" days ago")

    elif hour>0:
        print(hour,end="")
        if hour==1:
            print(" hour ago")
        else:
            print(" hours ago")
    
    elif minute>0:
        print(minute,end="")
        if minute==1:
            print(" minute ago")
        else:
            print(" minutes ago")

    else:
        print("just now")
