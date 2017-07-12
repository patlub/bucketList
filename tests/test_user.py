import unittest
from classes.user import User
from classes.bucket import Bucket
from classes.item import Item


class UserCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.user = User('patrick@gmail.com', 'password', 'Patrick')
        self.bucket = Bucket('travel', 'cities', 2)
        self.item = Item('Kampala')

    def test_user_created(self):
        """Should test that user is created successfully"""
        self.assertTrue(self.user)

    def test_create_bucket(self):
        """Should succesfully create a bucket"""
        self.user.create_bucket(self.bucket)
        index = len(self.user.buckets) - 1
        self.assertEqual(self.user.buckets[index].name, 'travel')
        self.assertEqual(self.user.buckets[index].description, 'cities')

    def test_create_bucket_that_already_exists(self):
        """Should return false if bucket name already exists"""
        self.user.create_bucket(self.bucket)
        self.assertFalse(self.user.create_bucket(self.bucket))

    def test_edit_bucket_functionality(self):
        """Should test for edit bucket name and description"""
        self.user.create_bucket(self.bucket)
        new_bucket_name = 'food'
        new_bucket_description = 'food types'
        self.user.edit_bucket(self.bucket.name,
                              new_bucket_name, new_bucket_description)
        self.assertEqual(self.bucket.name, new_bucket_name)
        self.assertEqual(self.bucket.description, new_bucket_description)

    def test_get_user_buckets(self):
        """Should check that a user can fetch all their buckets"""
        self.bucket1 = Bucket('travel', 'cities', 2)
        self.bucket2 = Bucket('food', 'test foods', 3)
        self.user.create_bucket(self.bucket)
        self.user.create_bucket(self.bucket2)
        self.assertIsInstance(self.user.get_buckets(), list)
        self.assertEqual(len(self.user.get_buckets()), 2)

    def test_get_single_bucket(self):
        """Should check getting a single bucket"""
        self.bucket1 = Bucket('travel', 'cities', 2)
        self.user.create_bucket(self.bucket)
        bucket = self.user.get_single_bucket('travel')
        self.assertEqual(bucket.name, 'travel')
        self.assertEqual(bucket.description, 'cities')
        self.assertEqual(bucket.id, 2)

    def test_delete_bucket(self):
        """Should check if bucket is deleted by user"""
        self.bucket1 = Bucket('travel', 'cities', 2)
        self.bucket2 = Bucket('food', 'test foods', 3)
        self.user.create_bucket(self.bucket1)
        self.user.create_bucket(self.bucket2)
        self.assertEqual(len(self.user.get_buckets()), 2)
        self.user.delete_bucket('travel')
        self.assertEqual(len(self.user.get_buckets()), 1)

    def test_user_add_item_to_bucket(self):
        """Should check if item is successfully added to bucket"""
        bucket_name = 'travel'
        self.user.create_bucket(self.bucket)
        self.user.add_item(bucket_name, self.item)
        index = len(self.bucket.items) - 1
        self.assertEqual(self.bucket.items[index].name, 'Kampala')

    def test_user_edit_item_in_bucket(self):
        """Should check if an item in a bucket is successfully edited """
        bucket_name = 'travel'
        item_name = 'Kampala'
        new_item_name = 'NewYork'
        self.user.create_bucket(self.bucket)
        self.user.add_item(bucket_name, self.item)
        index = len(self.bucket.items) - 1
        self.assertEqual(self.bucket.items[index].name, 'Kampala')
        self.user.edit_item(bucket_name, item_name, new_item_name)
        self.assertEqual(self.bucket.items[index].name, 'NewYork')

    def test_get_items_in_bucket(self):
        """Should check if bucket items are well fetched"""
        bucket_name = 'travel'
        item1 = Item('Kampala')
        item2= Item('Nairobi')

        self.user.create_bucket(self.bucket)
        self.user.add_item(bucket_name, item1)
        self.user.add_item(bucket_name, item2)
        items = self.user.get_items(bucket_name)
        self.assertIsInstance(items, list)
        self.assertEqual(len(items), 2)


if __name__ == '__main__':
    unittest.main()
