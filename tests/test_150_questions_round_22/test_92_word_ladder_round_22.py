import pytest
from src.my_project.interviews.top_150_questions_round_22.ex_92_word_ladder import Solution


class TestWordLadder:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test Example 1: Standard transformation sequence"""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        assert result == 5, "Should return 5 for the sequence: hit -> hot -> dot -> dog -> cog"
    
    def test_example_2(self):
        """Test Example 2: endWord not in wordList"""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        assert result == 0, "Should return 0 when endWord is not in wordList"
    
    def test_single_transformation(self):
        """Test single transformation"""
        beginWord = "hot"
        endWord = "dot"
        wordList = ["hot", "dot"]
        
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        assert result == 2, "Should return 2 for direct transformation"
    
    def test_no_transformation_needed(self):
        """Test when begin and end are same"""
        beginWord = "hot"
        endWord = "hot"
        wordList = ["hot"]
        
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        assert result == 1, "Should return 1 when beginWord equals endWord"
    
    def test_no_path_exists(self):
        """Test when no valid path exists"""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "tog"]
        
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        assert result == 0, "Should return 0 when no valid transformation sequence exists"
    
    def test_longer_words(self):
        """Test with longer words"""
        beginWord = "teach"
        endWord = "place"
        wordList = ["teach", "peach", "peace", "place", "reach"]
        
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        assert result == 4, "Should return 4 for: teach -> peach -> peace -> place"
    
    def test_multiple_paths(self):
        """Test when multiple paths exist"""
        beginWord = "red"
        endWord = "tax"
        wordList = ["ted", "tex", "red", "tax", "tad", "rex"]
        
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        assert result == 4, "Should return 4 for shortest path: red -> ted -> tex -> tax"
    
    def test_empty_word_list(self):
        """Test with empty wordList"""
        beginWord = "hit"
        endWord = "cog"
        wordList = []
        
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        assert result == 0, "Should return 0 when wordList is empty"
