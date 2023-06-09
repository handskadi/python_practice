#!/usr/bin/python3

squares = [1, 4, 9 , 16, 25]
cubes = [1, 3, 4, 6, 8]
l = ['a', 'b', 'c', 'd']
n = [1, 2, 34, 5, 6]
print(squares)
print(squares[-3:])
print(squares[:])

#Add element to a list
squares += [11,234, 100, 250, 100]
print(squares)
print(cubes)

#reassign value to element
cubes[2] = 16
print(cubes)

# append  with: append()
cubes.append(1988)
print(cubes)

#clear List
cubes[2:3] = []
print(cubes)
squares[:] = []
print(squares)

print(len(cubes))

# Nested lists
group = [l, n]
print(group)
print(group[1][2])
