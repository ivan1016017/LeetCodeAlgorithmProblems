from typing import List, Union, Collection, Mapping, Optional

class Solution:
    def isPalindrome(self, x: int) -> bool:

        str_x = str(x)
        return str_x == str_x[::-1]