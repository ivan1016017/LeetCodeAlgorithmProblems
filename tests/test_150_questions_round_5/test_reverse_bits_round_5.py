import unittest
from src.my_project.interviews.top_150_questions_round_5.\
reverse_bits import Solution

class RerverseBitsTestCase(unittest.TestCase):

    def test_reverse_bits(self):
        solution = Solution()
        output = solution.reverseBits(n=7)
        self.assertEqual(3758096384, output)

def sample1():
    pass 

def sample2():
    pass 