from typing import List
from project.task import Task

class Section:
    def __init__(self, name: int, ):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True
        return f"Completed task {task_name}"


    def clean_section(self):
        count_of_tasks = 0

        for task in self.tasks:
            if task.completed:
                count_of_tasks += 1
                self.tasks.remove(task)

        return f"Cleared {count_of_tasks} tasks."


    def view_section(self):
        tasks_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n" \
               f"{tasks_details}"


