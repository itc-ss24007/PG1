import datetime
t_dalta = datetime.timedelta(days=1)
dt = datetime.datetime.strptime("21/11/06 16:30","%d/%m/%y %H:%M")
print(dt + t_dalta)