import unittest
from src.my_project.interviews.top_150_questions_round_23\
.ex_12_insert_delete_get_random import RandomizedSet

class InsertAndDeleteGetRandomTestCase(unittest.TestCase):

    def test_first_case(self):
        randomized_set = RandomizedSet()
        self.assertTrue(randomized_set.insert(1))   # Inserts 1, returns true
        self.assertFalse(randomized_set.remove(2))  # 2 not present, returns false
        self.assertTrue(randomized_set.insert(2))   # Inserts 2, returns true
        self.assertIn(randomized_set.getRandom(), [1, 2])  # getRandom returns 1 or 2
        self.assertTrue(randomized_set.remove(1))   # Removes 1, returns true
        self.assertFalse(randomized_set.insert(2))  # 2 already present, returns false
        self.assertEqual(randomized_set.getRandom(), 2)    # Only 2 in set

    def test_insert_duplicate(self):
        randomized_set = RandomizedSet()
        self.assertTrue(randomized_set.insert(5))
        self.assertFalse(randomized_set.insert(5))  # duplicate

    def test_remove_nonexistent(self):
        randomized_set = RandomizedSet()
        self.assertFalse(randomized_set.remove(99))

    def test_remove_existing(self):
        randomized_set = RandomizedSet()
        randomized_set.insert(10)
        self.assertTrue(randomized_set.remove(10))
        self.assertFalse(randomized_set.remove(10))  # already removed

    def test_get_random_single_element(self):
        randomized_set = RandomizedSet()
        randomized_set.insert(42)
        self.assertEqual(randomized_set.getRandom(), 42)
