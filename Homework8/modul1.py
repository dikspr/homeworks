import os
import shutil
import datetime


# Создание файла

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# Создание директории
def create_dir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


# получение списка директорий
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# удаление файла или директории
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# копирование файла или директории
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)
# запись лога
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_dir('new_f')
    get_list(True)
