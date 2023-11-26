# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, newline='') as file_:
        csv_reader = csv.DictReader(file_)
        json_data = json.dumps([row for row in csv_reader], indent=4)
        with open(OUTPUT_FILENAME, 'w') as file_:
            file_.write(json_data)
    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
