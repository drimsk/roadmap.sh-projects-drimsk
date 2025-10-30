import sys
import json
import os
from datetime import datetime

# Define the path for the tasks JSON file
TASK_FILE = 'tasks.json'

# Helper functions to load and save tasks
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

# Helper function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# Generate a unique ID for each task
def generate_id(tasks):
    # Find the maximum existing ID and increment it
    return max([task['id'] for task in tasks], default=0) + 1

# Core functionalities - add, update, delete, mark status, list tasks
def add_task(description):
    tasks = load_tasks()
    task = {
        'id': generate_id(tasks),
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task['id'] != task_id] # Filter out the task to be deleted
    if len(new_tasks) == len(tasks): # No task was deleted
        print("Task not found")
    else:
        save_tasks(new_tasks)
        print("Task deleted successfully")

def mark_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return
    print("Task not found")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    filtered = tasks if filter_status is None else [t for t in tasks if t['status'] == filter_status]
    if not filtered:
        print("No tasks found.")
        return
    for task in filtered:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    try:
        if command == 'add':
            add_task(sys.argv[2])
        elif command == 'update':
            update_task(int(sys.argv[2]), sys.argv[3])
        elif command == 'delete':
            delete_task(int(sys.argv[2]))
        elif command == 'mark-in-progress':
            mark_status(int(sys.argv[2]), 'in-progress')
        elif command == 'mark-done':
            mark_status(int(sys.argv[2]), 'done')
        elif command == 'list':
            if len(sys.argv) == 2:
                list_tasks()
            else:
                list_tasks(sys.argv[2])
        else:
            print("Unknown command")
    except IndexError:
        print("Missing arguments for command")
    except ValueError:
        print("Invalid task ID")

if __name__ == '__main__':
    main()

# python Task_Tracker.py add "Buy groceries"