# ============================================
# PYTHON TO-DO LIST APPLICATION
# Complete Working Code (Fixed Save Issue)
# ============================================

import os  

tasks = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks.txt")

# ============= FILE OPERATIONS =============
def load_tasks():
    global tasks
    try:
        with open(FILE_NAME, 'r',encoding='utf-8') as file:   
            tasks = [line.strip() for line in file.readlines()]
            if tasks:
                print("Previous tasks loaded!")
    except FileNotFoundError:
        tasks = []
        print("Starting with a new task list")

def save_tasks():
    with open(FILE_NAME, 'w', encoding='utf-8') as file:  
        for task in tasks:
            file.write(task + '\n')
    print("Tasks saved to file!")

# ============= TASK OPERATIONS =============
def add_task(task_name):
    tasks.append(task_name)
    print(f"Task added: {task_name}")
    save_tasks()

def view_tasks():
    if not tasks:
        print("\nNo tasks yet! Add one to get started.\n")
        return
    
    print("\n" + "="*45)
    print("           YOUR TO-DO LIST")
    print("="*45)
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("="*45 + "\n")

def delete_task(task_number):
    try:
        removed = tasks.pop(task_number - 1)
        print(f"Task deleted: {removed}")
        save_tasks()
    except IndexError:
        print("Invalid task number!")

def update_task(task_number, new_name):
    try:
        old_task = tasks[task_number - 1]
        tasks[task_number - 1] = new_name
        print(f"Task updated: '{old_task}' → '{new_name}'")
        save_tasks()
    except IndexError:
        print("Invalid task number!")

def mark_complete(task_number):
    try:
        if not tasks[task_number - 1].startswith("✓"):
            print(f"Task marked as complete!")
            save_tasks()
        else:
            print("Task already completed!")
    except IndexError:
        print("Invalid task number!")

def clear_all_tasks():
    global tasks
    if not tasks:
        print("No tasks to clear!")
        return
    
    confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ").strip().lower()
    if confirm == 'yes':
        tasks = []
        save_tasks()
        print("All tasks cleared!")
    else:
        print("Clear operation cancelled.")

# ============= MENU DISPLAY =============
def display_menu():
    print("\n" + "="*50)
    print("TO-DO LIST MANAGER")
    print("="*45)
    print("1. View All Tasks       2. Add New Task")
    print("3. Delete Task          4. Update Task ")
    print("5. Mark Task Complete   6. Clear All Tasks")
    print("7. Exit ")
    print("="*45)

# ============= MAIN PROGRAM =============
def main():
    load_tasks()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            view_tasks()
        
        elif choice == '2':
            task_name = input("Enter task name: ").strip()
            if task_name:
                add_task(task_name)
            else:
                print("Task name cannot be empty!")
        
        elif choice == '3':
            if not tasks:
                print("No tasks to delete!")
            else:
                view_tasks()
                try:
                    task_num = int(input("Enter task number to delete: "))
                    delete_task(task_num)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '4':
            if not tasks:
                print("No tasks to update!")
            else:
                view_tasks()
                try:
                    task_num = int(input("Enter task number to update: "))
                    new_name = input("Enter new task name: ").strip()
                    if new_name:
                        update_task(task_num, new_name)
                    else:
                        print("Task name cannot be empty!")
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '5':
            if not tasks:
                print("No tasks to mark complete!")
            else:
                view_tasks()
                try:
                    task_num = int(input("Enter task number to mark complete: "))
                    mark_complete(task_num)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '6':
            clear_all_tasks()
        
        elif choice == '7':
            print("\n" + "="*45)
            print("Goodbye! Your tasks have been saved.")
            print("="*45 + "\n")
            break
        
        else:
            print("Invalid choice! Please enter 1-7.")

# ============= START PROGRAM =============
if __name__ == "__main__":
    main()