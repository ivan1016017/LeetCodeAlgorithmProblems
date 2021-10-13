from typing import List 


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        temp_dict = dict()
        flag: str = True

        for letter in s: 
            temp_dict[letter] = 0 

        for letter in s:
            temp_dict[letter] += 1

        for i in range(1,len(s)):
            if temp_dict[s[i-1]] !=  temp_dict[s[i]]:
                flag = False 
                return flag


        return flag 

solution = Solution()

print(solution.areOccurrencesEqual(s = "abacbc"))

print(solution.areOccurrencesEqual(s = "aaabb"))
