# Simple To-Do List Manager in Python

def display_tasks(tasks):
    print("\nYour To-Do List:")
    for i, (task, done) in enumerate(tasks.items(), 1):
        status = "✓ Done" if done else "⏳ Pending"
        print(f"{i}. {task} - {status}")

def main():
    tasks = {}
    while True:
        print("\nOptions: 1. Add  2. View  3. Mark Done  4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter new task: ")
            tasks[task] = False
            print("Task added!")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            task_num = int(input("Enter task number to mark done: ")) - 1
            if 0 <= task_num < len(tasks):
                task = list(tasks.keys())[task_num]
                tasks[task] = True
                print("Task marked as done!")
            else:
                print("Invalid task number!")

        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
