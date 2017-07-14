import unittest
from time import strftime, gmtime

from classes.item import Item

class ActivityTestCase(unittest.TestCase):
    def setUp(self):
        date_added = strftime("%Y-%m-%d", gmtime())
        self.activity = Item('Try chinese food', date_added)

    def test_activity_created(self):
        """Should test if activity has been created successfully"""
        self.assertIsInstance(self.activity, Item)

if __name__ == '__main__':
    unittest.main()
