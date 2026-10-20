
from src.validators import validate_task_title


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if not validate_task_title(title):
            raise ValueError("Judul tugas tidak valid")

        task = {
            "id": self.next_id,
            "title": title.strip(),
            "completed": False,
        }

        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return self.tasks.copy()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True

        return False
