# Задание №1
def greet(name: str):
    return f'Hello, {name}!'

def square(number):
    return number*number

def max_of_two(x, y):
    return max(x, y)

# Задание №2
def describe_person(name, age=30):
    return f'Name is {name}, age is {age}'


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

