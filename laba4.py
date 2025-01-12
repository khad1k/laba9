# Задание №1
from math import sqrt
import datetime


print(sqrt(16), sqrt(64))

print(datetime.datetime.now())


# Задание №2
from my_module import *

print(summ(7, 3))
print(mult(2, 3))


# Задание №3
from my_package.str_module import count_word
from my_package.num_module import *


print(count_word('Hello БВТ2404!'))

print(square(5))
print(is_prime(11), is_prime(12))




