import unittest
from src.my_project.interviews.top_150_questions_round_5.\
merge_sorted_array import Solution

class MergeSortedArrayTestCase(unittest.TestCase):

    def test_merge_sorted_array(self):
        solution = Solution()
        target = [1,2,2,3,5,6]
        output = solution.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
        for k,v in enumerate(target):
            self.assertEqual(v, output[k])