#module

def sayHi(name):
    print(f"Hello, {name}! Welcome to Alx.")
    return

def add(a, b):
    print(f"{a} + {b} = {a+b}")
    return

def multipy(a, b):
    print(f"{a} * {b} = {a*b}")
    return

def sub(a, b):
    print(f"{a} - {b} = {a-b}")
    return

def div(a,b):
    print(f"{a} / {b} = {a/b}")
    return

def remainder(a,b):
    print(f"{a%b} is the raimder of {a} / {b}")
    return

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        print(sayHi(sys.argv[1]))
        print(len(sys.argv))
    else:
        print(sayHi("Engineer"))
        print(len(sys.argv))  
