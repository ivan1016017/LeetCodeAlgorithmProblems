from typing import List 
from collections import defaultdict

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # left_dict = defaultdict(int)
        # right_dict = defaultdict(int)
        left_s = s[0:len(s)//2]
        right_s = s[len(s)//2:]
        count_left: int = 0
        count_right: int = 0
        

        vowels =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in range(len(s)//2):
            if left_s[i] in vowels:
                count_left += 1
            if right_s[i] in vowels:
                count_right += 1

        if count_left != count_right:
            return False 
        else: 
            return True 

        

        # for vowel in vowels:
        #     left_dict[vowel] = 0
        #     right_dict[vowel] = 0

        # for i in range(len(s)//2):
        #     left_dict[left_s[i]] += 1
        #     right_dict[right_s[i]] += 1


        # for vowel in vowels:
        #     if left_dict[vowel] != right_dict[vowel]:
        #         return False 

        return answer  


solution = Solution()

print(solution.halvesAreAlike(s = "book"))

print(solution.halvesAreAlike(s = "textbook"))

print(solution.halvesAreAlike(s = "MerryChristmas"))

print(solution.halvesAreAlike(s = "AbCdEfGh"))
