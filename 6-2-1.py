class Cylinder():
    '''円柱'''
    pi = 3.14

    def __init__(self,radius=1, height=1):
        self.radius = radius
        self.height = height

    def calc_base_area(self):
        pi = Cylinder.pi
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        pi = Cylinder.pi
        r = self.radius
        h = self.height
        return 2 * pi * r * h

    def calc_surface_area(self):
        c = self.calc_base_area()
        s = self.calc_side_area()
        return 2 * c + s

    def calc_volume(self):
        c = self.calc_base_area()
        h = self.height
        return h * c

    def show_results(self):
        r = self.radius
        h = self.height
        s = self.calc_surface_area()
        v = self.calc_volume()
        print('半径:{},高さ:{},底面積:{},表面積:{}'.format(r,h,s,v))

c1 = Cylinder()
c1.show_results()

c2 = Cylinder(1,3)
c2.show_results()
