#!/usr/bin/python3
from module1 import sayHi, add
count = 10

sayHi("Mohamed")
add(45,10)

def myd(a):
    global count
    count = count + 1
    print(count+a)
    return

myd(10)
# to Reload a module
# import img
# imp.reload(modulename)

