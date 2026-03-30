class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks else []

    def add_task(self, title):
        self.tasks.append({
            "title": title,
            "done": False
        })
    def delete_task(self, index):
        if 0 <= index - 1 < len(self.tasks):
            del self.tasks[index - 1]
    def edit_task(self, index, new_title):
        if 0 <= index - 1 < len(self.tasks):
            self.tasks[index - 1]["title"] = new_title
    def show_tasks(self):
        if not self.tasks:
            print("brak zadań")
            return
        for i, task in enumerate(self.tasks, 1):
            status = "^" if task["done"] else "X"
            print(f"{i}. [{status}] {task['title']}")
    def filter_tasks(self,status):
        if status == "zrobione":
            filtered = [t for t in self.tasks if t["done"]]
        else:
            filtered = [t for t in self.tasks if not t["done"]]
        for i, task in enumerate(filtered, 1):
            status = "^" if task["done"] else "X"
            print(f"{i}. [{status}] {task['title']}")