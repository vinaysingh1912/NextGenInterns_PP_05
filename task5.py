class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def __str__(self):
        status = "✔" if self.completed else "❌"
        return f"{status} {self.title}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added to the to-do list.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Task '{self.tasks[index].title}' marked as completed.")
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.title}' removed from the to-do list.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

    def run(self):
        while True:
            print("\nTo-Do List Application")
            print("1. Add task")
            print("2. Mark task as completed")
            print("3. Remove task")
            print("4. View all tasks")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter task title: ")
                self.add_task(title)
            elif choice == '2':
                self.view_tasks()
                try:
                    index = int(input("Enter task number to mark as completed: ")) - 1
                    self.mark_completed(index)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '3':
                self.view_tasks()
                try:
                    index = int(input("Enter task number to remove: ")) - 1
                    self.remove_task(index)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                self.view_tasks()
            elif choice == '5':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


# Run the To-Do List Application
todo_list = TodoList()
todo_list.run()
