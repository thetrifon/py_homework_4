#  2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint
numbers = [] # формируем список чисел, длинну вводит пользователь
for i in range(int(input('Введите длину списка: '))):
    numbers.append(randint(0, 1000)) # у нашего списка чисел будет i элементов от 0 до 1000
print('Исходный список: ', numbers)

numbers_greater = [] # сюда будем писать числа, которые соотвуствуют условию
for i in range(len(numbers)):
    if numbers[i] > numbers[i-1]:
        numbers_greater.append(numbers[i])

print('Результат: ', numbers_greater)



