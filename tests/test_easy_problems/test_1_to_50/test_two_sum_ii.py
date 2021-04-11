from faker import Faker
import unittest

if __name__ == '__main__':

    class TestTwoNumbersTestCase(unittest.TestCase):

        def test_empty(self):
            self.assertEqual(1,1)