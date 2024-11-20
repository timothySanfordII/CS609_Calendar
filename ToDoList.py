# Task Manager for To-Do List
#The to-do list will allow users to:

#Add Tasks: Users can input tasks with optional details (e.g., deadlines, priorities).
#Mark Tasks as Completed: Users can track progress by marking tasks as done.
#Delete Tasks: Remove completed or canceled tasks.
#(Optional): Integrate reminders for high-priority tasks or deadlines.
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=None, deadline=None, priority="Low"):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "deadline": deadline,
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task)
        return task

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        return self.tasks

    def get_tasks(self, show_completed=False):
        if show_completed:
            return self.tasks
        return [task for task in self.tasks if not task["completed"]]


# Example Usage
if __name__ == "__main__":
    manager = TaskManager()

    # Add Tasks
    manager.add_task("Finish Project", "Complete the calendar app project", "2024-11-30", "High")
    manager.add_task("Prepare Presentation", "Slides for Thursday's review", "2024-11-23", "Medium")

    # Display Tasks
    print("To-Do List:")
    for task in manager.get_tasks():
        print(f"[ ] {task['title']} (Priority: {task['priority']}, Deadline: {task['deadline']})")

    # Mark a Task as Completed
    manager.mark_completed(1)

    # Display Updated Tasks
    print("\nUpdated To-Do List:")
    for task in manager.get_tasks():
        print(f"[ ] {task['title']} (Priority: {task['priority']}, Deadline: {task['deadline']})")
    print("\nCompleted Tasks:")
    for task in manager.get_tasks(show_completed=True):
        if task["completed"]:
            print(f"[x] {task['title']} (Completed)")
