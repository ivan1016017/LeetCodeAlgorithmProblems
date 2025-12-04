import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_13_product_of_array_except_itself import Solution

class ProductExcetItselfTestCase(unittest.TestCase):

    def test_product_first_case(self):
        solution = Solution()
        output = solution.productExceptSelf(nums = [1,2,3,4])
        target = [24,12,8,6]
        self.assertEqual(output, target)

    def test_product_second_case(self):
        solution = Solution()
        output = solution.productExceptSelf(nums = [-1,1,0,-3,3])
        target = [0,0,9,0,0]
        self.assertEqual(output, target)           