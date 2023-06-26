#!/usr/bin/python3

try:
    myFile = open("data.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("File not found!")
    print(ex.args)
else:
    print("File :", myFile.read())
    myFile.close()
finally:
    print("### This will be printed no matter what ###")
