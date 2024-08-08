# test_to_do.py

import unittest  # Import the unittest module for creating tests.
from to_do import ToDoApp  # Import the ToDoApp class from our to-do application.

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        """Set up a new ToDoApp instance for each test."""
        # This method runs before each test, initializing a fresh instance of ToDoApp.
        self.app = ToDoApp()

    def test_add_task(self):
        """Test adding a task to the list."""
        # Add a task to the list and then check if the length of the tasks list is 1.
        self.app.add_task("Task 1")
        self.assertEqual(len(self.app.tasks), 1)

    def test_view_tasks(self):
        """Test viewing tasks."""
        # Add a task and then check if viewing tasks returns a list with that task.
        self.app.add_task("Task 1")
        tasks = self.app.view_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Task 1")

    def test_complete_task(self):
        """Test completing a task."""
        # Add a task, complete it, and then check if the task's 'completed' field is True.
        self.app.add_task("Task 1")
        result = self.app.complete_task(0)
        self.assertTrue(result)  # Check if the function returns True indicating success.
        self.assertTrue(self.app.tasks[0]["completed"])  # Check if the task is marked as completed.

    def test_delete_task(self):
        """Test deleting a task."""
        # Add a task, delete it, and then check if the tasks list is empty.
        self.app.add_task("Task 1")
        result = self.app.delete_task(0)
        self.assertTrue(result)  # Check if the function returns True indicating success.
        self.assertEqual(len(self.app.tasks), 0)  # Check if the task list is empty after deletion.

if __name__ == "__main__":
    # This runs the tests when the script is executed directly.
    unittest.main()
