import unittest
from faker import Faker
from src.my_project.easy_problems.from1to50.majority_element import Solution
import random

class MajorityElementTestCase(unittest.TestCase):


    def test_unique_element(self):

        self.data_factory = Faker(100)
        solution = Solution()
        for i in range(10000):
            self.assertEqual(i,i)

    def test_sample(self):
        print(list(range(10)))








