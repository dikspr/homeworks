# 1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами
# (на уроке разбирали на примере одной функции).
# 2. Добавить возможность изменения текущей рабочей директории.
# 3. Добавить возможность развлечения в процессе работы с менеджером.
# Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.

import sys
from modul1 import create_file, create_folder, get_list, delete_file, copy_file, save_info
from game import game

save_info('Старт')

# Обработка ошибки ввода первого параметра
try:
    command = sys.argv[1]
except IndexError:
    print('Отсутсвует команда')
    save_info('Отсутсвует команда')
else:
# обработка команды list
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название файла')
            save_info(f'{command}Отсутсвует название файла')
        else:
            create_file(name)
            save_info(f'Создан файл {name}')

# Обработка команды create_folder
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название файла')
            save_info(f'{command}Отсутсвует название файла')
        else:
            create_folder(name)
            save_info(f'Создана папка {name}')

# Обработка команды delete
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название файла')
            save_info(f'{command}Отсутсвует название файла')
        else:
            delete_file(name)
            save_info(f'Удалена папка или файл {name}')

# Обработка команды copy
    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название исходного файла')
            save_info(f'{command}Отсутсвует название исходного файла')
        else:
            try:
                new_name = sys.argv[3]
            except:
                print('Отсутсвует название для копии файла')
                save_info(f'{command}Отсутсвует название для копии файла')
            else:
                copy_file(name, new_name)
                save_info(f'Скопирована папка или файл {name} с новым именем {new_name}')

# Обработка команды game
    elif command == 'game':
        game()

# Обработка команды help
    elif command == 'help':
        print('list - Список файлов и папок')
        print('create_file - Создать файл')
        print('create_folder - Создать папку')
        print('delete - Удалить файл или папку')
        print('copy - Создать файл или папку')
        print('help - Помощь')

save_info('Стоп')
