class CalcTest:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calc(self):
        print(self.x * self.y)

instCal = CalcTest(2,3)
instCal.calc()

