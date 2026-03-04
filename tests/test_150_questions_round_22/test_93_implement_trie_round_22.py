import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_93_implement_trie import Trie, TrieNode


class ImplementTrieTestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
               [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        Output: [null, null, true, false, true, null, true]
        
        Explanation:
        Trie trie = new Trie();
        trie.insert("apple");
        trie.search("apple");   // return True
        trie.search("app");     // return False
        trie.startsWith("app"); // return True
        trie.insert("app");
        trie.search("app");     // return True
        """
        trie = Trie()
        
        # Insert "apple"
        trie.insert("apple")
        
        # Search for "apple" - should return True
        self.assertTrue(trie.search("apple"))
        
        # Search for "app" - should return False (prefix exists but not complete word)
        self.assertFalse(trie.search("app"))
        
        # Check if "app" is a prefix - should return True
        self.assertTrue(trie.startsWith("app"))
        
        # Insert "app"
        trie.insert("app")
        
        # Search for "app" again - should now return True
        self.assertTrue(trie.search("app"))