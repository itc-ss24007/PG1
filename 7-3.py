import sys

class MyValueLimitError(Exception):
    def __init__(self, x1, x2, limit_num):
        self.x1 = x1
        self.x2 = x2
        self.limit_num = limit_num

    def __str__(self):
        return '値の範囲を超えていま{} {} {}'.format(self.x1,self.x2,self.limit_num)

def multiplication_limit(x1,x2,limit_num):
    try:
        x = x1 * x2
        if x > limit_num:
            raise MyValueLimitError(x1, x2, limit_num)
        return x
    except MyValueLimitError as vle:
        print(vle)
        return limit_num
    except:
        print('Unexpected Error:',sys.exc_info())
        return None

limit_num = 10000
multiplication_limit(100,101,limit_num)
