import unittest
from app.models import User, Quote, Comment ,Posts

class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = '123456')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('123456'))

class QuoteTest(unittest.TestCase):
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.quote = Quote("Vector", "Passion is the cost for success")

    def test_instance(self):
        self.assertTrue(isinstance(self.quote, Quote))

    def test_init(self):
        self.assertEqual(self.quote.author, "Vector")
        self.assertEqual(self.quote.quote,"Passion is the cost for success")

class PostTest(unittest.TestCase):
    
    def setUp(self):
    
        self.new_post = Post(title = "Chelsea",
                            post = " chelsea likely to come top this season",
                            author = "vector")
    

    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_post, Posts))

    def test_init(self):
        self.assertEqual(self.new_post.title, "Chelsea")
        self.assertEqual(self.new_post.post,"chelsea likely to come top this season")
        self.assertEqual(self.new_post.author, "Vector")
   