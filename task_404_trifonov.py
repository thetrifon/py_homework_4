#  4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]


from random import randint # использовал конструкцию в задании 2
numbers = []
for i in range(int(input('Введите длину списка: '))):
    numbers.append(randint(0, 1000)) # у нашего списка чисел будет i элементов от 0 до 1000
print('Исходный список: ', numbers)

no_repeat = [i for i in numbers if numbers.count(i) == 1] # сюда будем писать числа, которые соотвуствуют условию

print('Результат: ', no_repeat)



