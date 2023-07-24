def print_pi(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_pi(name="KADI", age=34, city="Marrakech")
