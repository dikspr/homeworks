# 3. Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
#
#     Примечание: Список с целыми числами создайте вручную в начале файла.
# Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

import math

# Определяем функцию
def new_list(old_list):
    # создаем копию принятого списка
    fun_list = old_list[:]
    # генерируем возвращаемый список согласно условиям
    return [math.sqrt(num) if num > 0 else num for num in fun_list]


old_list = [1, -3, 4]
# применяем функцию и выводим результат
print(new_list(old_list))
print(old_list)
