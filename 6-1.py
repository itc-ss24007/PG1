class Car:
    weight = 4000
    num_wheels = 4

    def __init__(self,car_name='NoName'):
        self.name = car_name

    def calc_weight_per_wheel(self):
        return self.weight/self.num_wheels

default_car = Car()

print(default_car.name)
default_car =Car('DeLorean')
print(default_car.name)
