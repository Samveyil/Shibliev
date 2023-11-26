# TODO решите задачу
import json
import os.path


def task(file_path) -> float:
    with open(file_path) as file:
        num = json.load(file)
    sum_ = sum(item['score'] * item['weight'] for item in num)
    return round(sum_, 3)


path = os.path.abspath('input.json')

print(task(path))
