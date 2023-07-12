class Parent():
    def __init__(self):
        self.c = 21
        self.__d = 43

class Child():
    def __init__(self):
        self.e = 84
        Parent.__init__(self)

obj = Child()
print(obj.c)
print(obj.__d)
