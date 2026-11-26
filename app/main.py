from app.storage import load_tasks, save_tasks
from app.task_manager import add_task, get_tasks


def main():
    # Load previously saved tasks when application starts
    tasks = load_tasks()

    while True:
        print("\n===== DevTask Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")

            try:
                task = add_task(tasks, title)
                save_tasks(tasks)

                print(f"Task added successfully: {task['title']}")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            all_tasks = get_tasks(tasks)

            if not all_tasks:
                print("No tasks available.")

            for task in all_tasks:
                status = "Completed" if task["completed"] else "Pending"
                print(f"{task['id']}. {task['title']} - {status}")

        elif choice == "3":
            print("Thank you for using DevTask Manager!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
