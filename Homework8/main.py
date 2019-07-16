# 1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами
# (на уроке разбирали на примере одной функции).
# 2. Добавить возможность изменения текущей рабочей директории.
# 3. Добавить возможность развлечения в процессе работы с менеджером.
# Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.

import os
import sys
from modul1 import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_folder
from game import game

save_info('Старт')
# сохраняем текущее значение рабочей папки
start_folder=os.getcwd()

# Обработка ошибки ввода первого параметра
try:
    command = sys.argv[1]
except IndexError:
    print('Отсутсвует команда')
    os.chdir(r'{}'.format(start_folder))
    save_info('Отсутсвует команда')
else:
# обработка команды list
    if command == 'list':
        change_folder()
        get_list()
        os.chdir(r'{}'.format(start_folder))
        save_info('Был просмотрен список папок и файлов в рабочей папке')
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название файла')
            os.chdir(r'{}'.format(start_folder))
            save_info('Отсутсвует название файла')
        else:
            txt= sys.argv[3]
            change_folder()
            create_file(name, txt)
            os.chdir(r'{}'.format(start_folder))
            save_info('Создан файл в рабочей папке')

# Обработка команды create_folder
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название файла')
            os.chdir(r'{}'.format(start_folder))
            save_info('Отсутсвует название файла')
        else:
            change_folder()
            create_folder(name)
            os.chdir(r'{}'.format(start_folder))
            save_info('Создана папка в рабочей папке')

# Обработка команды delete
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название файла')
            os.chdir(r'{}'.format(start_folder))
            save_info('Отсутсвует название файла')
        else:
            change_folder()
            delete_file(name)
            os.chdir(r'{}'.format(start_folder))
            save_info('Удалена папка или файл в рабочей папке')

# Обработка команды copy
    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвует название исходного файла')
            save_info('Отсутсвует название исходного файла')
        else:
            try:
                new_name = sys.argv[3]
            except:
                print('Отсутсвует название для копии файла')
                save_info('Отсутсвует название для копии файла')
            else:
                change_folder()
                copy_file(name, new_name)
                os.chdir(r'{}'.format(start_folder))
                save_info('Скопирована папка или файл с новым именем в рабочей папке')

# Обработка команды game
    elif command == 'game':
        game()
        save_info('Была запущена игра')

# Обработка команды help
    elif command == 'help':
        print('list - Список файлов и папок')
        print('create_file - Создать файл')
        print('create_folder - Создать папку')
        print('delete - Удалить файл или папку')
        print('copy - Создать файл или папку')
        print('help - Помощь')

save_info('Стоп')
