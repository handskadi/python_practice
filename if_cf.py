print("Is it raingin: \n 1: yes \n 2: no \n")
raining = int(input())
print("Who are you: \n woman \n man")
gender = input()

if raining == 1:
    print("I am raining")
    print("Take your umbrella with you")
    if gender == "woman":
        print("pls madam")
    else:
        print("You rock man")
else:
    print("It's good day")
    
