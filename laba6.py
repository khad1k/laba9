# Задание №1
class UserAccount:

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        return self.password == password



user = UserAccount('Andrey Khodikyan', 'andreytv@icloud.com', '1_Love_Python')

print(user.username, user.email, user.password)

user.set_password('1_Love_C++')

print(user.check_password('ojskdhf'))
print(user.check_password('1_Love_C++'))
print(user.password)


# Задание №2
class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return self.make, self.model


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return super().get_info(),  self.fuel_type



car1 = Car(1, 2, 3)

print(car1.get_info())







