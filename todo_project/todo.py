tasks = []

def show_menu():
    print("\n==== TO-DO LIST ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    
    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")
