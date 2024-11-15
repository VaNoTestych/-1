# TODO импортировать необходимые молули
import json #Импортировал модуля для работы с json и csv
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file1: #Используя менеджер контекста with, открываю два файла
        with open(OUTPUT_FILENAME, 'w') as file2:
            data = [lines for lines in csv.DictReader(file1)] #Получаю список словарей data построчно считав и получив словари
            json.dump(data, file2, indent=4) #Переношу данные в формат json







if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
