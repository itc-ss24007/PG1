class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration()
        value = self.data[self.index]
        self.index+=1
        return value

itr = MyIterator("wang")
for char in itr:
    print(char,end=" ")

class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index-=1
        value = self.data[self.index]
        return value

rev = Reverse("spam")
for char in rev:
    print(char,end=" ")

def reverse(data):
    ret = []
    for index in range(len(data)-1,-1,-1):
        ret.append(data[index])
    return ret

for char in reverse("golf"):
    print(char,end=" ")
        
