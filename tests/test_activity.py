import unittest
from classes.item import Item

class ActivityTestCase(unittest.TestCase):
    def setUp(self):
        self.activity = Item('Try chinese food')

    def test_activity_created(self):
        """Should test if activity has been created successfully"""
        self.assertIsInstance(self.activity, Item)

if __name__ == '__main__':
    unittest.main()
