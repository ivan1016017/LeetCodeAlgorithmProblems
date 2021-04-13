import unittest
from faker import Faker
from src.my_project.easy_problems.from1to50.majority_element import Solution
import random

class MajorityElementTestCase(unittest.TestCase):



    def test_unique_element(self):

        self.data_factory = Faker(100)
        solution = Solution()
        for i in range(10000):
            self.assertEqual(solution.majorityElement([i]),i)


    def test_general_random_number(self):
        solution = Solution()
        n = 500
        m = int(n // 2)
        single_value = random.randint(1, 300)

        i = 1
        temp = None
        unique_list = list()
        unique_index = list()
        while i <= m:
            temp = random.randint(1, 300)
            if temp not in unique_list:
                unique_list.append(temp)
                i += 1

        i = 1
        while i <= n - m:
            temp = random.randint(0, n - 1)
            if temp not in unique_index:
                unique_index.append(temp)
                i += 1


        list_numbers = [None] * n
        for i in range(m):
            list_numbers[unique_index[i]] = single_value

        l = 0
        for i in range(len(list_numbers)):
            if list_numbers[i] is None:
                list_numbers[i] = unique_list[l]
                l += 1
        self.assertEqual(solution.majorityElement(list_numbers),single_value)











