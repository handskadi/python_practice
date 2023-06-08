#!/usr/bin/python3
import my_module
import my_module as md
from my_module import add

#add = my_module.add 
#mult = my_module.mult

add(10,20)
md.mult(10,4)

print()
print(dir(my_module))
print()
