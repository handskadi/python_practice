#!/usr/bin/python3

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("( Initializing {} )".format(self.name))
        Robot.population = Robot.population + 1

    def die(self):
        print("{} is being destoryed!".format(self.name))
        Robot.population = Robot.population - 1

        if  Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            if Robot.population == 1:
                print("There is still {:d} robot working.".format(Robot.population))
            else:
                print("There are still {:d} robots working.".format(Robot.population))

    
    def say_hi(self):
        print("Greetings, my master call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d}. robots.".format(cls.population))

dihya = Robot("Dihya")
aksil = Robot("AKsil")
aksil = Robot("Sifaw")

dihya.say_hi()
aksil.say_hi()
Robot.how_many()
print()
aksil.die()
Robot.how_many()
