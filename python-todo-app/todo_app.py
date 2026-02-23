import os

# Filename to save data
TODO_FILE = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            for line in file:
                try:
                    task, status = line.strip().split("|")
                    tasks.append({"task": task, "completed": status == "True"})
                except ValueError:
                    continue
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for item in tasks:
            file.write(f"{item['task']}|{item['completed']}\n")

def display_tasks(tasks):
    if not tasks:
        print("\n[!] There are no tasks yet.")
        return

    print("\n--- Your To-Do List ---")
    for i, item in enumerate(tasks):
        status = "✓" if item["completed"] else " "
        print(f"{i + 1}. [{status}] {item['task']}")
    print("-----------------------")

def add_task(tasks):
    task_description = input("Enter new task: ").strip()
    if task_description:
        tasks.append({"task": task_description, "completed": False})
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Error: Task description cannot be empty.")

def mark_completed(tasks):
    display_tasks(tasks)
    if not tasks: return
    try:
        num = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter numbers only.")

def delete_task(tasks):
    display_tasks(tasks)
    if not tasks: return
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks(tasks)
            print(f"'{removed['task']}' has been deleted.")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter numbers only.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks | 2. Add | 3. Complete | 4. Delete | 5. Exit")
        choice = input("Choice: ")
        if choice == '1': display_tasks(tasks)
        elif choice == '2': add_task(tasks)
        elif choice == '3': mark_completed(tasks)
        elif choice == '4': delete_task(tasks)
        elif choice == '5': break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()