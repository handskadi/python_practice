class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        """ Invoking the __init__ of the parent class """
        Person.__init__(self, name, idnumber)

a = Employee('KADI', 19880408, 135779, "Webmaster")
a.display()

