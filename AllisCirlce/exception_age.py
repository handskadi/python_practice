try:
    age = int(input("Enter a age:"))
    if not isinstance(age, int):
        raise ValueError("there must be digits")

    elif age < 18:
        raise ValueError("Your must be at least 18")
    else:
        print("Welcome boss!")
except ValueError as err:
    print(str(err))
