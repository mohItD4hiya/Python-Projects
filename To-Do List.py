todo_list=[]
def show_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

print("Welcome to the To-Do List Application!")
print("You can add, remove, and view your tasks.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '3':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '4':
            print("\nExiting the To-Do List application. \nThank you for using it!")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
# To-Do List Application
# This script allows users to manage a simple to-do list with options to show, add,
# and remove tasks. The tasks are stored in a list, and the user can interact with
# the application through a menu-driven interface.
# The application runs in a loop until the user chooses to exit.
# The tasks are displayed with their index, and the user can add or remove tasks by
# entering the task name. The application provides feedback on the actions performed.
# The script is designed to be simple and user-friendly, making it easy to manage daily tasks.