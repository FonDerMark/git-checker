import os
import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
current_folder_path = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(current_folder_path, 'commit_info.json')


def create_commit_info(commit_message):
    '''
    Тут просто создаю json, что с ним делать каждый решает сам, от простого ендпоинта для чтения
    или создания кастомного контент-процессора для студентов на темплейтах и до кеширования и
    прочих рабостей в момент бинда wsgi и т.д.
    '''
    data = {
        "commit_message": commit_message,
        "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z'),
        "path": FILE_PATH
    }

    with open(FILE_PATH, 'w') as f:
        json.dump(data, f)

    print(f"Создан commit_info.json с данными: {data}")


if __name__ == "__main__":
    import sys
    commit_message = sys.argv[1]
    create_commit_info(commit_message)
