import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [task.strip() for task in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet!")
        return
    print("\n📝 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: [1] Add [2] Remove [3] View [4] Quit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("✅ Task added.")
        elif choice == "2":
            display_tasks(tasks)
            try:
                idx = int(input("Enter task number to remove: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"❌ Removed: {removed}")
                else:
                    print("⚠️ Invalid number.")
            except ValueError:
                print("⚠️ Enter a valid number.")
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
