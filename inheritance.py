""" Inhertance"""

class Person(object):
    """ Prent class """
    def __init__(self, name, id):
        """ Constructor """
        self.name = name
        self.id = id
    def Display(self):
        """ To check if this person is an employee """
        print(self.name, self.id)


class Emp(Person):
    """child class"""
    def Print(self):
        print("Emp class called")


"""Excutable code"""
emp_detail = Emp("KADI", 1988)
emp_detail.Display()
emp_detail.Print()

