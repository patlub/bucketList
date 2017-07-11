import unittest
from classes.app import App
from classes.user import User


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.user = User('patrick@gmail.com', 'password', 'Patrick')

    def test_creation_of_app_obj(self):
        self.assertIsInstance(self.app, App,
                              msg="Object not instance of App")

    def test_sign_up_to_app(self):
        """Should test if user successfully signs up to app"""
        self.app.sign_up(self.user)
        index = len(self.app.all_users) - 1
        self.assertEqual(self.app.all_users[index].name,
                         'Patrick')
        self.assertEqual(self.app.all_users[index].email,
                         'patrick@gmail.com')
        self.assertEqual(self.app.all_users[index].password,
                         'password')

    def test_sign_in_to_app(self):
        self.app.sign_up(self.user)
        self.assertTrue(self.app.sign_in(self.user),
                        msg='Should return True for sign in')


if __name__ == '__main__':
    unittest.main()
