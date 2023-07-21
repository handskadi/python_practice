class Rectangle:


    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @classmethod
    def swear(cls, name):
        print(f"Fuck you mother fucker {name}")
    
    @staticmethod
    def capi(word):
        return word.upper()

    def rect_area(self):
        print(f"Area of rectangle: {self.__width * self.__height}")

    def get_rec(self):
        return self.__width * self.__height

    def set_rec(self, new_W, new_H):
        self.__width = new_W
        self.__height = new_H
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            raise ValueError("Radius must be greater than 0.")
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            raise ValueError("Radius must be greater than 0.")

    @property
    def area(self):
        return self.__width * self.__height

rec = Rectangle(20, 12)
rec.rect_area()
print(rec.get_rec())
rec.set_rec(5,5)
print(rec.get_rec())

print(" ____ ")
print(rec.area)
print(Rectangle.capi("Mohamed"))
Rectangle.swear("!!")
