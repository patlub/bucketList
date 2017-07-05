import unittest
from classes.activity import Activity

class ActivityTestCase(unittest.TestCase):
    def setUp(self):
        self.activity = Activity('Try chinese food')

    def test_activity_created(self):
        """Should test if activity has been created successfully"""
        self.assertIsInstance(self.activity, Activity)

if __name__ == '__main__':
    unittest.main()
