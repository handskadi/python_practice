num = [1, 2, 3, 4, 5]
name = input("Enter your name: ")
age = eval(input("Enter Your age: "))
for i in num:
    print(i)
    if i == 3:
        continue
else:
    print("I come to an end")

def my_func(name):
    print("Hello, " + name + "!")
    bd =  2023 - age
    print("You was born in {}.".format(bd))

for i in range(0, 37, 6):
    print(i)
open_str = "My name is {} & I\'m {}."
print(open_str.format(name, age))
my_func(name)

# we only can convert from int to float
# if we want intger  we add> field_name:conversion > {0:.0f}
# Padding Variable Substitutions
#   > < ^    : to align left right and center
print("I am sorry {fn:>10}, we only have {pn:.2f} places".format(fn = "Moha", pn = 4))

#format filler with chars
# 5 x 4byte = 20
print("{} {:*^20} {}".format("#" ," Content ", "#"))

# Organizing Data:
for i in range(3,13):
    print(i, i*i, i*i*i)
# Here is how we can organize them
# d3 d4 d5 : is 5 of integer (space of 5 interger will be given)
for i in range(3,13):
    print("{:3d} {:>4d} {:<5d}".format(i, i*i, i*i*i))

