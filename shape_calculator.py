class Rectangle:

    def __init__(self, width, height):
        'create rectangle'
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width < 50 and self.height < 50:
            return ("*"*self.width + '\n')*self.height
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __str__(self):
        if self.width == self.height:
            return f'Square(side={self.height})'
        else:
            return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        self.set_height(side)
        self.set_width(side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)


