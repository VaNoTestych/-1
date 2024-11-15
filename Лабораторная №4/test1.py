# TODO решите задачу
import json #Импортируем модуль джля работы json файлами

def task() -> float:
    with open("input.json", 'r') as file: #Используем менеджер контекста with, чтобы нечаянно не забыть закрыть файл. Открываем файл в формате чтения
        json_data = json.load(file) #Десериализуем файл

    return round(sum([dictionary["score"] * dictionary["weight"] for dictionary in json_data]), ndigits=3)
    #С помощью list comprehension сразу же считаем сумму произведения значений из словарей по ключам score и weight и округляем согласно заданию

print(task())
