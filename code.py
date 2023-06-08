# this is a comment
num1, num2 = input("Enter two numbers: ").split()

num1 = int(num1)
num2 = int(num2)

add = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2

print(num1, "+",  num2, "=", add)
print("{} - {} = {}".format(num1, num2, sub))
print(f"{num1} * {num2} = {mult}")
