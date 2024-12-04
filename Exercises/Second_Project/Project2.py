from datetime import datetime


class ProjectManagement:
    def __init__(self):
        self.projects = {}

    def add_project(self, name):
        if name in self.projects:
            print("Project already exists.")
        else:
            self.projects[name] = []
            print(f"Project '{name}' added successfully.")

    def edit_project(self, old_name):
        if old_name in self.projects:
            print(f"enter the new name for the project {old_name} : ")
            new_name = input()
            self.projects[new_name] = self.projects.pop(old_name)
            print(f"Project renamed from '{old_name}' to '{new_name}'.")
        else:
            print("Project does not exist.")

    def delete_project(self, name):
        if name in self.projects:
            del self.projects[name]
            print(f"Project '{name}' deleted successfully.")
        else:
            print("Project does not exist.")

    def display_projects(self):
        for p, tasks in self.projects.items():
            print(f"Project: {p}")
            print(f"Number of tasks: {len(tasks)}")
            for task in tasks:
                print(
                    f"  - Task ID: {task['id']}, Name: {task['name']}, "
                    f"Status: {'Completed' if task['status'] else 'Not Completed'}"
                )

    def add_task_to_project(self, project_name, task):
        if project_name in self.projects:
            self.projects[project_name].append(task)
            print(f"Task '{task['name']}' added to project '{project_name}'.")
        else:
            print(f"Project '{project_name}' does not exist.")


class TaskManagement:
    def __init__(self):
        self.tasks = {}

    def add_task(self, project_manager):
        try:
            id_ = int(input("Enter Task ID: "))
            if id_ in self.tasks:
                print("Task already exists.")
                return

            name = input("Enter Task Name: ")
            description = input("Enter Task Description: ")
            status = False
            start_date = self.input_for_date("Enter Start Date (YYYY-MM-DD HH:MM): ")
            end_date = None
            project_name = input("Enter the Project Name to associate with this task: ")

            if project_name not in project_manager.projects:
                print(f"Project '{project_name}' does not exist. Please create it first.")
                return

            task = {
                "id": id_,
                "name": name,
                "description": description,
                "status": status,
                "start_date": start_date,
                "end_date": end_date,
                "duration": None,
                "project": project_name,
            }

            self.tasks[id_] = task
            project_manager.add_task_to_project(project_name, task)
            print(f"Task '{name}' added successfully to project '{project_name}'.")
            print(f"Start Date: {start_date}")

        except ValueError:
            print("Invalid input. Please ensure numbers are entired correct.")

    def mark_as_done(self, id_):
        if id_ in self.tasks:
            task = self.tasks[id_]
            if not task["status"]:
                task["status"] = True
                end_date = self.input_for_date("Enter End Date (YYYY-MM-DD HH:MM): ")
                if end_date > task["start_date"]:
                    task["end_date"] = end_date
                    duration = task["end_date"] - task["start_date"]
                    task["duration"] = self.calculate_duration(duration)
                    print(f"Task '{task['name']}' marked as complete.")
                    print(f"End Date: {task['end_date']}")
                    print(f"Duration: {task['duration']}")
                else:
                    print("End Date should be greater than Start Date.")
            else:
                print("Task is already completed.")
        else:
            print("Task not found.")

    def input_for_date(self, prompt):
        while True:
            try:
                date_input = input(prompt)
                return datetime.strptime(date_input, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid date format. Please enter in 'YYYY-MM-DD HH:MM' format.")

    def calculate_duration(self, duration):
        total_seconds = int(duration.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)
        if months > 12:
            years, months = divmod(months, 12)
            return f"{years} years {months} months {days} days {hours} hours {minutes} minutes"
        else:
         return f"month {months} days {days} hour {hours} minute {minutes}"

    def edit_task(self, id_):
        if id_ in self.tasks:
            task = self.tasks[id_]
            print("Choose your option to edit:")
            print("1. Name")
            print("2. Description")
            print("3. Status")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                task["name"] = input("Enter new name: ")
            elif choice == 2:
                task["description"] = input("Enter new description: ")
            elif choice == 3:
                status_input = input("Is the task done? (yes/no): ").strip().lower()
                new_status = True if status_input in ["yes", "y"] else False
                if new_status and not task["status"]:
                    self.mark_as_done(id_)
                else:
                    task["status"] = new_status
                    print("Status updated.")
            else:
                print("Invalid option.")
        else:
            print("Task does not exist.")

    def delete_task(self, id_):
        if id_ in self.tasks:
            del self.tasks[id_]
            print(f"Task with ID {id_} deleted successfully.")
        else:
            print("Task does not exist.")

    def search_task(self, id_):
        if id_ in self.tasks:
            print("Task found:")
            task = self.tasks[id_]
            print(
                f"ID: {task['id']}, Name: {task['name']}, Status: {'Completed' if task['status'] else 'Not Completed'}, "
                f"Start Date: {task['start_date']}, End Date: {task['end_date']}, Duration: {task['duration']}, "
                f"Description: {task['description']}, Project: {task['project']}"
            )
        else:
            print("Task not found.")



def main():
    project_manager = ProjectManagement()
    task_manager = TaskManagement()

    while True:
        print("\nMenu:")
        print("1. Add Project")
        print("2. Edit Project")
        print("3. Delete Project")
        print("4. Add Task")
        print("5. Edit Task")
        print("6. Mark Task as Complete")
        print("7. Delete Task")
        print("8. Search Task")
        print("9. Display Projects and Tasks")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            project_name = input("Enter Project Name: ")
            project_manager.add_project(project_name)

        elif choice == "2":
            old_name = input("Enter the name of the project to edit: ")
            project_manager.edit_project(old_name)

        elif choice == "3":
            project_name = input("Enter the name of the project to delete: ")
            project_manager.delete_project(project_name)

        elif choice == "4":
            task_manager.add_task(project_manager)

        elif choice == "5":
            try:
                task_id = int(input("Enter Task ID to edit: "))
                task_manager.edit_task(task_id)
            except ValueError:
                print("Invalid Task ID.")

        elif choice == "6":
            try:
                task_id = int(input("Enter Task ID to mark as complete: "))
                task_manager.mark_as_done(task_id)
            except ValueError:
                print("Invalid Task ID.")

        elif choice == "7":
            try:
                task_id = int(input("Enter Task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid Task ID.")

        elif choice == "8":
            try:
                task_id = int(input("Enter Task ID to search: "))
                task_manager.search_task(task_id)
            except ValueError:
                print("Invalid Task ID.")

        elif choice == "9":
            project_manager.display_projects()

        elif choice == "10":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
