class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture'

        lines = ''
        for i in range(self.height):
            lines += '*' * self.width + '\n'
        return lines

    def get_amount_inside(self, shape):
        input_area = shape.get_area()
        available_area = self.get_area()

        # the num of times a passed shape could fit inside the available shape.
        times_fit = 0
        while available_area >= input_area:
            available_area -= input_area

            times_fit += 1
        return times_fit

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)

    def set_side(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        return f'Square(side={self.height})'









rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))