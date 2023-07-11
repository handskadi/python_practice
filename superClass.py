class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, dob):
        self.sName = name
        self.sAge = age
        self.dob = dob

        #inherting the properties of parent class
        super().__init__("Zizo", age)

    def displayInfo(self):
        print(self.sName, self.sAge, self.dob)


obj = Student("KADI", 35, "08-04-1988")
obj.display()
obj.displayInfo()
