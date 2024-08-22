from datetime import datetime
now = datetime.today()
print('now:',now)
print('year:',now.year)
print('month:',now.month)
print('day:',now.day)
print('hour:',now.hour)
print('minute:',now.minute)
print('second:',now.second)
print('microsecond:',now.microsecond)

mytime = datetime(2019,4,1,hour=15)
print(mytime)

dt = datetime.strptime("21/11/2006 16:30","%d/%m/%Y %H:%M")
print(dt)

dt2 = dt.strftime("%Y年%m月%d日 %H時%M分")
print(dt)
print(dt2)


