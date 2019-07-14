import os


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



if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_dir('new_f')
