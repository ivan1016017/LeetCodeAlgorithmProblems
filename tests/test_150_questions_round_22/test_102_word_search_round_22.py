import unittest
from src.my_project.interviews.top_150_questions_round_22\
    .ex_102_word_search import Solution


class WordSearchTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1_abcced(self):
        """Test Example 1: word ABCCED exists in the board"""
        board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]]
        word = "ABCCED"
        self.assertTrue(self.solution.exist(board, word))
    
    def test_example_2_see(self):
        """Test Example 2: word SEE exists in the board"""
        board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))
    
    def test_example_3_abcb(self):
        """Test Example 3: word ABCB does not exist (cannot reuse cells)"""
        board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]]
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word))
    
    def test_single_cell_match(self):
        """Test single cell board with matching character"""
        board = [["A"]]
        word = "A"
        self.assertTrue(self.solution.exist(board, word))
    
    def test_single_cell_no_match(self):
        """Test single cell board with non-matching character"""
        board = [["A"]]
        word = "B"
        self.assertFalse(self.solution.exist(board, word))
    
    def test_word_longer_than_board(self):
        """Test word that is longer than total board cells"""
        board = [["A","B"]]
        word = "ABC"
        self.assertFalse(self.solution.exist(board, word))
    
    def test_zigzag_path(self):
        """Test word requiring zigzag path"""
        board = [["A","B","C"],
                ["D","E","F"],
                ["G","H","I"]]
        word = "ABEDGH"
        self.assertTrue(self.solution.exist(board, word))
    
    def test_spiral_path(self):
        """Test word requiring spiral movement"""
        board = [["A","B","C"],
                ["F","E","D"],
                ["G","H","I"]]
        word = "ABCDEFGHI"
        self.assertTrue(self.solution.exist(board, word))
    
    def test_backtracking_needed(self):
        """Test case where backtracking is necessary"""
        board = [["C","A","A"],
                ["A","A","A"],
                ["B","C","D"]]
        word = "AAB"
        self.assertTrue(self.solution.exist(board, word))


if __name__ == '__main__':
    unittest.main()