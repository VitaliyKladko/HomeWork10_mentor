import json
from candidate import Candidate


def load_candidates(filename):
    """
    Функция загружает данные из файла, в качестве аргумента принимает файл
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_all(data):
    """
    Функция возвращает всех кандидатов (В ЭТОЙ ФУНКЦИИ RETURN ОТДАЕТ СПИСОК ОБЪЕКТОВ КЛАССА Candidate)
    """
    arr = []
    for item in data:
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        arr.append(candidate)
    return arr

# ВАЖНО! Аргументами данной функции являются pk - int, data - список объектов класса Candidate
def get_by_pk(pk, data):
    """
    Функция вовращает кандидата по его номеру PK
    """
    for item in data:
        if item.pk == pk:
            return item

# ВАЖНО! Аргументами данной функции являются skill_name - str; data - список объектов класса Candidate
def get_by_skill(skill_name, data):
    """
    Функция возвращает кандидатов по навыка (по совпадениям)
    """
    arr = []
    for item in data:
        if skill_name.lower() in item.skills.lower():
            arr.append(item)
    return arr
