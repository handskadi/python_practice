#!/usr/bin/python3

while True:
    try:
        x = int(input("Please Enter a Number: "))
        break;
    except ValueError:
        print("Oops! That was no valid number. Try again ...")
