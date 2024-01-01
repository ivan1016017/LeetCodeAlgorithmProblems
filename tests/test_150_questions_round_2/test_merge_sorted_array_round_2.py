import unittest
from src.my_project.interviews.top_150_questions_round_2.\
merge_sorted_array import Solution

class MergeSortedArrayTestCase(unittest.TestCase):

    def test_merge_sorted_array(self):
        solution = Solution()
        output = solution.merge(nums1=[1,2],m=2,nums2=[3,4,5],n=3)
        
        for i in range(5):
            self.assertEqual(i+1,output[i])