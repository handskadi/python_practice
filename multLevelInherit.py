class Base():
    def __init__(self, name):
        self.name = name

    def  getName(self):
        return self.name

class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age  = age

    def getAge(self):
        return self.age

class GrandChild(Child):
    def __init__(self, name, age, job):
        Child.__init__(self, name, age)
        self.job = job

    def getJob(self):
        return self.job

g = GrandChild("KADI", 1988, "Software Engineer")
print(g.getName(), g.getAge(), g.getJob())
