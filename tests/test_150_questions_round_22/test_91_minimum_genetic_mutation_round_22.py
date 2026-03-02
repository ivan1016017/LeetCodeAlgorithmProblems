import unittest
from src.my_project.interviews.top_150_questions_round_22\
    .ex_91_minimum_genetic_mutation import Solution
from typing import Optional, List


class MinimumGeneticMutationTestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Example 1:
        Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
        Output: 1
        Explanation: One mutation from "AACCGGTT" to "AACCGGTA".
        """
        solution = Solution()
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        
        result = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """
        Example 2:
        Input: startGene = "AACCGGTT", endGene = "AAACGGTA", 
               bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        Output: 2
        Explanation: 
        "AACCGGTT" -> "AACCGGTA" -> "AAACGGTA"
        """
        solution = Solution()
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        expected = 2
        
        result = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(result, expected)

    def test_no_mutation_possible(self):
        """
        Test case where endGene is not in bank.
        Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA"]
        Output: -1
        Explanation: endGene is not in the bank, so mutation is impossible.
        """
        solution = Solution()
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA"]
        expected = -1
        
        result = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(result, expected)

    def test_start_equals_end(self):
        """
        Test case where start and end are the same.
        Input: startGene = "AACCGGTT", endGene = "AACCGGTT", bank = ["AACCGGTT"]
        Output: 0
        Explanation: No mutation needed as start equals end.
        """
        solution = Solution()
        startGene = "AACCGGTT"
        endGene = "AACCGGTT"
        bank = ["AACCGGTT"]
        expected = 0
        
        result = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(result, expected)

    def test_empty_bank(self):
        """
        Test case with empty bank.
        Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = []
        Output: -1
        Explanation: Bank is empty, so no valid mutations possible.
        """
        solution = Solution()
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = []
        expected = -1
        
        result = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(result, expected)

    def test_longer_path(self):
        """
        Test case with a longer mutation path.
        Input: startGene = "AAAAACCC", endGene = "AACCCCCC", 
               bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
        Output: 3
        """
        solution = Solution()
        startGene = "AAAAACCC"
        endGene = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        expected = 3
        
        result = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(result, expected)

    def test_multiple_paths(self):
        """
        Test case with multiple possible paths (BFS should find shortest).
        """
        solution = Solution()
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA", "AACCGCTT", "AAACGCTA"]
        # Shortest path: AACCGGTT -> AACCGGTA -> AAACGGTA (2 mutations)
        expected = 2
        
        result = solution.minMutation(startGene, endGene, bank)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
