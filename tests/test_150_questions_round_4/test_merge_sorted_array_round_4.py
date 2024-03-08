import unittest
from src.my_project.interviews.top_150_questions_round_4.\
merge_sorted_array import Solution

class MergeTestCase(unittest.TestCase):

    def test_merge_sorted_arrays(self):
        solution = Solution()
        output = solution.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
        test_lst = [1,2,2,3,5,6]
        for k, v in enumerate(test_lst):
            self.assertEqual(v, output[k])
        