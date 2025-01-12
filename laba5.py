# Задание №1
class Book:
    title = 'name'
    author = 'author'
    year = 'year'

    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'


# Задание №2
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


obj = Circle(5)
print(obj.radius)

obj.set_radius(20)
print(obj.get_radius())