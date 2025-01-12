# Задание №1
def f(choice='full'):
    if choice == 'full':
        with open('example.txt', 'r', encoding='UTF-8') as example:
            print(example.read())
    elif choice == 'linewise':
        with open('example.txt', 'r', encoding='UTF-8') as example:
            for line in example:
                print(line[:-1])


# Задание №2
'''
with open('user_input.txt', 'a', encoding='UTF-8') as file:
    print(input('Введите текст для записи в файл: '), file=file)
'''

# Задание №3

def f3(file, choice='full'):
    if choice == 'full':
        with open(file, 'r', encoding='UTF-8') as example:
            print(example.read())
    elif choice == 'linewise':
        with open(file, 'r', encoding='UTF-8') as example:
            for line in example:
                print(line[:-1])
    else:
        return print('Не существующий способ ')

try:
    f3(input('Введите имя файла :'))

except FileNotFoundError:
    print('Вы ввели не правильное имя файла')



