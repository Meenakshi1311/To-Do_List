tasks = []


def add_task(task):
    tasks.append(task)


def view_tasks():
    print("Here are your tasks:\n")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
    else:
        print("Invalid task number")


while True:
    print("Options:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == "4":
        print("Aborting!")
        break
