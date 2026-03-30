import json

FILE_NAME = "tasks.json"

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
             return json.load(f)
    except FileNotFoundError:
        return []