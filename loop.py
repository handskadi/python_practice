import random

# For Loop
print("# This s a For Loop:")
for i in [2, 4, 6, 8, 10]:
    print( "i = " , i)

#for range
print("# This is a for loop + range:")
for i in range(10): # it will not include value passed to it
    print("i = ", i)

# First Problem:
print("#Challenge 1:")
for i in range(21):
    if i % 2 == 0:
        print(i)
# Challenge 2:
print("Challenge 2")
inva = input("Enter your Investment amount: ")
exint = input("Enter your Expected interest: ")
inva = float(inva) 
exint = float(exint) * .01 # this will conver to percentage

for i in range(10):
    inva = inva + (inva * exint)
    # print(f"Year: {i} : {(inva + inva_h * exint)}")
else:
    print("Year 10 yrs:  {:.2f}".format( inva))

rand_num = random.randrange(1, 51)
if (rand_num % 2):
    print(f"{rand_num} is even.") 
else:
    print(f"{rand_num} is odd.")
