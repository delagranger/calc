import json
import os
from pathlib import Path

def create_history_file():
    app_dir = Path.home() / "AppData" / "Roaming" / "calc" # получение пути
    app_dir.mkdir(parents=True, exist_ok=True) 
    # создает папку по заданному пути
    # parents = True - создает дополнительные папки, указанные в пути, 
    # если они не существуют
    # exist_ok = True - если папка существует, то ничего не создает

    history_file = app_dir / "history.json" 

    if not history_file.exists(): # проверяет наличие файла в директории
        with open(history_file, "w", encoding="utf-8") as f:
            json.dump([], f)


def check_history_file():
    history_file = Path.home() / "AppData" / "Roaming" / "calc" / "history.json"

    if not history_file.exists():
        create_history_file()
    
    return history_file


def show_history():
    history_file = check_history_file()

    with open(history_file, "r", encoding="utf-8") as f:
        history = json.load(f)

    for operation in history:
        print(json.dumps(operation, indent=4, ensure_ascii=False))
        print("-" * 40)
    

def update_history(expression, last_result):
    history_file = check_history_file()
    new_data = {"Выражение": expression, "Результат": last_result}

    with open(history_file, "r", encoding="utf-8") as f:
        history = json.load(f)

    history.append(new_data)

    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)