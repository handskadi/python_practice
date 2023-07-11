""" Inhertance"""

class Person(object):
    """ Prent class """
    def __init__(self, name, id):
        """ Constructor """
        self.name = name
        self.id = id

    def getName(self):
        """ To get name of  employee """
        return self.name

    def isEmployee(self):
        """ Check if person is employee """
        return False

class Emp(Person):
    """child class"""
    def isEmployee(self):
        """ Set if the person is employee or not """
        return True


"""Excutable code"""
emp_detail = Emp("KADI", 1988)
print(emp_detail.getName(), emp_detail.isEmployee())

emp = Person("mohza", 23)
print(emp.getName(),emp.isEmployee())

