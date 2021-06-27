from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        # initialize variables
        count_str1 = ""
        count_str2 = ""

        for item in word1:
            count_str1 += item

        for item in word2:
            count_str2 += item


        return count_str1 == count_str2