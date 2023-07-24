def sum_num(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_num(2,3,4,5)
print(result)
