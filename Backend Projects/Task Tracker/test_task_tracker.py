import unittest
import os
import json
from datetime import datetime
from task_tracker import (
    TASK_FILE, load_tasks, save_tasks, add_task, update_task,
    delete_task, mark_status, list_tasks
)

class TestTaskCLI(unittest.TestCase):

    def setUp(self):
        # Backup existing task file if present
        if os.path.exists(TASK_FILE):
            os.rename(TASK_FILE, TASK_FILE + '.bak')
        # Start with a clean slate
        save_tasks([])

    def tearDown(self):
        # Clean up test file
        if os.path.exists(TASK_FILE):
            os.remove(TASK_FILE)
        # Restore original file if backed up
        if os.path.exists(TASK_FILE + '.bak'):
            os.rename(TASK_FILE + '.bak', TASK_FILE)

    def test_add_task(self):
        add_task("Test task")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Test task")
        self.assertEqual(tasks[0]['status'], "todo")

    def test_update_task(self):
        add_task("Initial task")
        update_task(1, "Updated task")
        tasks = load_tasks()
        self.assertEqual(tasks[0]['description'], "Updated task")

    def test_delete_task(self):
        add_task("Task to delete")
        delete_task(1)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_mark_in_progress(self):
        add_task("Progress task")
        mark_status(1, "in-progress")
        tasks = load_tasks()
        self.assertEqual(tasks[0]['status'], "in-progress")

    def test_mark_done(self):
        add_task("Done task")
        mark_status(1, "done")
        tasks = load_tasks()
        self.assertEqual(tasks[0]['status'], "done")

    def test_list_tasks(self):
        add_task("Task A")
        add_task("Task B")
        mark_status(2, "done")
        all_tasks = load_tasks()
        done_tasks = [t for t in all_tasks if t['status'] == 'done']
        todo_tasks = [t for t in all_tasks if t['status'] == 'todo']
        self.assertEqual(len(all_tasks), 2)
        self.assertEqual(len(done_tasks), 1)
        self.assertEqual(len(todo_tasks), 1)

if __name__ == '__main__':
    unittest.main()
