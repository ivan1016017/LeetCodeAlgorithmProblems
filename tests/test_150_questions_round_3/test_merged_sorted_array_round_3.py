import unittest
from src.my_project.interviews.top_150_questions_round_3.\
merged_sorted_array import Solution

class MergeSortedArrayTestCase(unittest.TestCase):

    def test_sorted_array(self):
        solution = Solution()
        output = solution.merge(nums1=[1,2,3,0,0,0], 
                                m=3, 
                                nums2=[2,5,6], 
                                n=3)
        test_lst = [1,2,2,3,5,6]

        for i in range(len(test_lst)):
            self.assertEqual(test_lst[i], output[i])