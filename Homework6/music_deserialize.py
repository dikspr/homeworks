# 2: Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.

import pickle
import json

# читаем из файла group.pickle

with open('group.pickle', 'rb') as f:
    my_favourite_group_pickle = pickle.load(f)

# читаем из файла group.json

with open('group.json', 'r') as f1:
    my_favourite_group_json = json.load(f1)

# выводим результат

print(my_favourite_group_pickle)
print(my_favourite_group_json)
