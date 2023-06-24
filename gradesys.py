print("Enter mark: ", end =" ");
mark = int(input())
if mark >= 90:
    print("A grade")
elif mark >= 80 and  mark < 90:
    print("B grade")
elif mark >= 70 and mark < 80:
    print("C grade")
elif mark >= 60 and mark < 70:
    print("D grade")
else:
    print("E grade")
