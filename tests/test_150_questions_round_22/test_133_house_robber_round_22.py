import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_133_house_robber import Solution


class HouseRobberTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test case: [1,2,3,1] -> 4"""
        nums = [1, 2, 3, 1]
        self.assertEqual(self.solution.rob(nums), 4)
    
    def test_example_2(self):
        """Test case: [2,7,9,3,1] -> 12"""
        nums = [2, 7, 9, 3, 1]
        self.assertEqual(self.solution.rob(nums), 12)
    
    def test_single_house(self):
        """Test case: Single house"""
        nums = [5]
        self.assertEqual(self.solution.rob(nums), 5)
    
    def test_two_houses(self):
        """Test case: Two houses"""
        nums = [1, 2]
        self.assertEqual(self.solution.rob(nums), 2)
    
    def test_all_same_value(self):
        """Test case: All houses have same value"""
        nums = [5, 5, 5, 5, 5]
        self.assertEqual(self.solution.rob(nums), 15)
    
    def test_ascending_values(self):
        """Test case: Ascending values"""
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.rob(nums), 9)


if __name__ == '__main__':
    unittest.main()