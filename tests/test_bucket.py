import unittest
from classes.bucket import Bucket


class BucketTestCase(unittest.TestCase):
    def setUp(self):
        self.bucket = Bucket('Travel', 'Cities I must visit before 30', 1)

    def test_bucket_created(self):
        """Should test if bucket has been created successfully"""
        self.assertTrue(self.bucket)


if __name__ == '__main__':
    unittest.main()
