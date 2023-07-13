class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model} is starting the engine.")

my_car = Car("Ford", "Festa")
my_car.start_engine()
