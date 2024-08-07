# to_do.py

class ToDoApp:
    def __init__(self):
        """Initialize the to-do list."""
        # The tasks list will store all tasks as dictionaries with 'task' and 'completed' keys.
        self.tasks = []

    def add_task(self, task):
        """Add a task to the to-do list."""
        # Append a new task to the tasks list with 'completed' initially set to False.
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        """View all tasks."""
        # Return the entire list of tasks, allowing the user to see what tasks are pending or completed.
        return self.tasks

    def complete_task(self, task_index):
        """Mark a task as complete by its index."""
        # Check if the given index is within the range of tasks.
        if 0 <= task_index < len(self.tasks):
            # If it is, mark the task as completed by setting 'completed' to True.
            self.tasks[task_index]["completed"] = True
            return True  # Return True indicating the task was successfully completed.
        return False  # Return False if the task index was out of range.

    def delete_task(self, task_index):
        """Delete a task by its index."""
        # Check if the given index is within the range of tasks.
        if 0 <= task_index < len(self.tasks):
            # If it is, remove the task from the list using the del statement.
            del self.tasks[task_index]
            return True  # Return True indicating the task was successfully deleted.
        return False  # Return False if the task index was out of range.
