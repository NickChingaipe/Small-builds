# Simple To-Do List App
# Save this as todo.py and run with: python todo.py

tasks = []

def show_menu():
    print("\n====== TO-DO LIST ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"? '{task}' added to your list.")
def view_tasks():
    if not tasks:
        print("?? Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"? '{removed}' removed.")
        except (ValueError, IndexError):
            print("? Invalid input. Try again.")
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("?? Goodbye!")
        break
    else:
        print("? Invalid choice. Please try again.")