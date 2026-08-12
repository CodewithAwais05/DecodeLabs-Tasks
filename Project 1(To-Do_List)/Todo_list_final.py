"""
Project 1: The To-Do List
DecodeLabs - Python Programming Internship (Batch 2026)

Goal:
Build a program where users can add tasks to a list and view them.

Concepts applied from the training deck:
- Storage: a list holds multiple tasks in a single variable (my_tasks = [])
- Each task is a dictionary {"id": ..., "task": ...} -> like one row of a database table
- Process: append() to add, enumerate() for professional index + value access
- Decoupling: Model (data logic) is kept separate from View (user interface)
- Persistence: RAM is volatile, so tasks are saved to a JSON file on disk
  (Serialization) so data survives after the program closes
"""

import json
import os

DATA_FILE = "tasks.json"


# ------------------- MODEL (Data Logic) -------------------

def load_tasks():
    """Read tasks from disk (Storage) into memory (RAM)."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(my_tasks):
    """Write the in-memory list to disk so data is not lost (Persistence)."""
    with open(DATA_FILE, "w") as file:
        json.dump(my_tasks, file, indent=4)


def add_task(my_tasks, task_name):
    """Add a new task as a dictionary (like a database row)."""
    new_id = my_tasks[-1]["id"] + 1 if my_tasks else 1
    my_tasks.append({"id": new_id, "task": task_name})
    save_tasks(my_tasks)


def remove_task(my_tasks, task_id):
    """Remove a task by its id (Primary Key)."""
    for task in my_tasks:
        if task["id"] == task_id:
            my_tasks.remove(task)
            save_tasks(my_tasks)
            return True
    return False


# ------------------- VIEW (User Interface) -------------------

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")


def view_tasks(my_tasks):
    print("\n--- Your Tasks ---")
    if not my_tasks:
        print("No tasks yet. Add one!")
        return
    # enumerate() gives both index (position) and value (data) together
    for index, task in enumerate(my_tasks, start=1):
        print(f'{index}. [ID {task["id"]}] {task["task"]}')


def prompt_add(my_tasks):
    task_name = input("Enter the task you want to add: ").strip()
    if task_name == "":
        print("Task cannot be empty!")
        return
    add_task(my_tasks, task_name)
    print(f'"{task_name}" has been added and saved.')


def prompt_remove(my_tasks):
    view_tasks(my_tasks)
    if not my_tasks:
        return
    try:
        task_id = int(input("\nEnter the task ID to remove: "))
        if remove_task(my_tasks, task_id):
            print("Task removed and saved.")
        else:
            print("No task found with that ID.")
    except ValueError:
        print("Please enter a valid number.")


# ------------------- MAIN (Program Entry Point) -------------------

def main():
    my_tasks = load_tasks()  # Load previously saved tasks from disk on startup

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            prompt_add(my_tasks)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            prompt_remove(my_tasks)
        elif choice == "4":
            print("Goodbye! Your tasks are safely saved in tasks.json.")
            break
        else:
            print("Invalid option. Please choose between 1-4.")


if __name__ == "__main__":
    main()