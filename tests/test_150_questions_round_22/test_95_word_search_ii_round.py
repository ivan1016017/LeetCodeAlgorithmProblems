import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_95_word_search_ii import Solution


class WordSearchIITestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
               words = ["oath","pea","eat","rain"]
        Output: ["eat","oath"]
        """
        solution = Solution()
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"]
        ]
        words = ["oath", "pea", "eat", "rain"]
        result = solution.findWords(board, words)
        self.assertEqual(sorted(result), sorted(["eat", "oath"]))
    
    def test_example_2(self):
        """
        Input: board = [["a","b"],["c","d"]], words = ["abcb"]
        Output: []
        """
        solution = Solution()
        board = [["a", "b"], ["c", "d"]]
        words = ["abcb"]
        result = solution.findWords(board, words)
        self.assertEqual(result, [])
    
    def test_single_cell(self):
        """
        Test with single cell board
        """
        solution = Solution()
        board = [["a"]]
        words = ["a", "b"]
        result = solution.findWords(board, words)
        self.assertEqual(result, ["a"])
    
    def test_no_words_found(self):
        """
        Test when no words are found
        """
        solution = Solution()
        board = [["a", "b"], ["c", "d"]]
        words = ["xyz", "pqr"]
        result = solution.findWords(board, words)
        self.assertEqual(result, [])