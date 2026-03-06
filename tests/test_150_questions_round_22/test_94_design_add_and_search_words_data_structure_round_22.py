import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_94_design_add_and_search_words_data_structure import WordDictionary


class DesignAddAndSearchWordsDataStructureTestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
               [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
        Output: [null,null,null,null,false,true,true,true]
        
        Explanation:
        WordDictionary wordDictionary = new WordDictionary();
        wordDictionary.addWord("bad");
        wordDictionary.addWord("dad");
        wordDictionary.addWord("mad");
        wordDictionary.search("pad"); // return False
        wordDictionary.search("bad"); // return True
        wordDictionary.search(".ad"); // return True
        wordDictionary.search("b.."); // return True
        """
        wordDictionary = WordDictionary()
        
        # Add words
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        
        # Search for "pad" - should return False
        self.assertFalse(wordDictionary.search("pad"))
        
        # Search for "bad" - should return True
        self.assertTrue(wordDictionary.search("bad"))
        
        # Search for ".ad" - should return True (matches bad, dad, mad)
        self.assertTrue(wordDictionary.search(".ad"))
        
        # Search for "b.." - should return True (matches bad)
        self.assertTrue(wordDictionary.search("b.."))