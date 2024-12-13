import unittest
from app import add_task, get_tasks, app, tasks  

class TestToDoList(unittest.TestCase):

    def setUp(self):
        """Reset tasks before each test."""
        tasks.clear()  

    def test_add_task(self):
        """Test adding a task."""
        add_task("Buy groceries")
        self.assertIn("Buy groceries", get_tasks())

    def test_get_tasks(self):
        """Test retrieving tasks."""
        add_task("Clean the house")
        self.assertEqual(get_tasks(), ["Clean the house"])

    def test_add_task_route(self):
        """Test the /add-task route."""
        with app.test_client() as client:
            response = client.post('/add-task', data={'task': 'Walk the dog'})
            self.assertEqual(response.status_code, 302)  # Check for redirect
            self.assertIn('Walk the dog', get_tasks())

if __name__ == '__main__':
    unittest.main()