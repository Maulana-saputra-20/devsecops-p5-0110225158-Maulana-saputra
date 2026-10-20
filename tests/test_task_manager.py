
import unittest

from src.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Belajar DevSecOps")

        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "Belajar DevSecOps")
        self.assertFalse(task["completed"])

    def test_reject_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        task = self.manager.add_task("Mengerjakan tugas")

        result = self.manager.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(task["completed"])

    def test_unknown_task_id(self):
        self.assertFalse(self.manager.complete_task(999))


if __name__ == "__main__":
    unittest.main()
