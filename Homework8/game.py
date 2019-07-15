# Модуль с игрой
def game():
    import random

    print('Игра "Загадай число"')
    print('Загадайте число в диапазоне от 1 до 100')

    # Задаем первичный диапазон генерации чисел

    diap1 = 1
    diap2 = 100


    while True:
        # Генерируем число.
        number = random.randint(diap1, diap2)
        # Вывод команд
        print('Ваше число {}?'.format(number))
        print('Если число угадано, нажмите 1.')
        print('Если ваше число больше, нажмите 2.')
        print('Если ваше число меньше, нажмите 3.')
        print('Нажмите любую другую цифру для выхода.')
        # Проверка числа
        command = int(input(':'))
        if command == 1:
            print('Ура! Я угадал!')
            break
        elif command == 2:
            # Если загаданное число больше сгенерированного,
            # то в качестве верхней границы генератора задаем сгенерированное число, увеличенное на 1
            diap1 = number+1

        elif command == 3:
            # Если загаданное число больше сгенерированного,
            # то в качестве верхней границы генератора задаем сгенерированное число, уменьшенное на 1
            diap2 = number-1

        else:
            # Для тех, кому надоест играть
            print('Выход')
            break

