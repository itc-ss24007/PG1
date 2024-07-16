def number_to_day(num=0):
    if num ==0:
        day = "今日"
    elif num == -1:
        day ='昨日'
    elif num == 1:
        day ='明日'
    else:
        day='今日より１日超えて外れた日'
    return day
