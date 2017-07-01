import unittest
from classes.user import User


class UserCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.user = User()

    def test_user_created(self):
        """Should test that user is created successfully"""
        self.assertTrue(self.user)

    def test_user_sign_up(self):
        """Should test if sign up details are assigned to new user """
        name = 'Patrick'
        email = 'Patrick@gmail.com'
        password = 'patrick'
        self.user.sign_up(name, email, password)
        self.assertEqual(self.user.name, name)
        self.assertEqual(self.user.email, email)
        self.assertEqual(self.user.password, password)

    def test_user_sign_in(self):
        """Should test if user successfully signs in"""
        email = 'Patrick@gmail.com'
        password = 'patrick'
        self.user.sign_in(email, password)
        self.assertEqual(self.user.email, email)
        self.assertEqual(self.user.password, password)
        self.assertEqual(self.user.name, 'Patrick')

    def test_user_sign_out(self):
        """Should test if user is signed out successfully"""
        email = 'Patrick@gmail.com'
        password = 'patrick'
        self.user.sign_in(email, password)
        self.user.sign_out()
        self.assertIsNone(self.user.name)
        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.password)


if __name__ == '__main__':
    unittest.main()
