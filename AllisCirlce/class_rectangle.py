class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def rect_area(self):
        print(f"Area of rectangle: {int(self.width)* int(self.height)}")

rec = Rectangle("20", "12")
rec.rect_area()
