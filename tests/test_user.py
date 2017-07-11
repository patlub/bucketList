import unittest
from classes.user import User
from classes.bucket import Bucket


class UserCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.user = User('patrick@gmail.com', 'password', 'Patrick')
        self.bucket = Bucket('travel', 'cities', 2)

    def test_user_created(self):
        """Should test that user is created successfully"""
        self.assertTrue(self.user)

    def test_create_bucket(self):
        """Should succesfully create a bucket"""
        self.user.create_bucket(self.bucket)
        index = len(self.user.buckets) - 1
        self.assertEqual(self.user.buckets[index].name, 'travel')
        self.assertEqual(self.user.buckets[index].description, 'cities')

    def test_create_bucket_that_already_exixsts(self):
        """Should return false if bucket name already exists"""
        self.user.create_bucket(self.bucket)
        self.assertFalse(self.user.create_bucket(self.bucket))




if __name__ == '__main__':
    unittest.main()
