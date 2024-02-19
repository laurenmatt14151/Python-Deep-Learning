tasks = []

#add a task
def add_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    tasks.append({"name": name, "description": description, "completed": False})
