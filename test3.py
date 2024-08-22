class Person:
    num = 20

    def __init__(self, name):
        self.name = name
    
    def run(self, num):
        print('run' * num)

    def say_something(self):
        print(f'こんにちは、私は{self.name}です')
        self.run(10)

class Athlete(Person):
    def run(self,num):
        print('run'*num,'Jump')
athlete = Athlete('Ryoichi')
athlete.say_something()
