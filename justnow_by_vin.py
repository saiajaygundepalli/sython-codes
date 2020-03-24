import datetime
from datetime import datetime
def updated_post(x,y):
    a=datetime.strptime(x,'%a %d %b %Y %H:%M:%S %z')
    b=datetime.strptime(y,'%a %d %b %Y %H:%M:%S %z')
    d=b-a
    time=d.total_seconds()
    days=time//86400
    if time < 60:
        print('just now')
    elif time >=60 and time < 3600:
        min_1=time//60
        if min_1==1:
            print('{} minute ago'.format(int(min_1)))
        else:   
            print('{} minutes ago'.format(int(min_1)))
    elif time >= 3600 and time < 86400:
        hours = time//3600
        if hours==1:
            print('{} hour ago'.format(int(hours)))
        else:
            print('{} hours ago'.format(int(hours)))
    elif days==1:
         print('{} day ago'.format(int(days)))
    elif days > 1 and days < 7 :
        print('{} days ago'.format(int(days)))
    elif days >= 7 and days < 31:
        week = days//7
        if week == 1:
            print(int(week),"week ago")
        else:
            print(int(week),"weeks ago")
    elif days >= 31 and days < 365:
        month = days//31
        if month == 1:
            print(int(month),"month ago")
        else:
            print(int(month),"months ago")
    elif days >= 365:
        year = days//365
        if year == 1:
            print(int(year),"year ago")
        else:
            print(int(year),"years ago")
t=int(input())
for i in range(t):
    arr1=input()
    arr2=input()
    updated_post(arr1,arr2)
    
