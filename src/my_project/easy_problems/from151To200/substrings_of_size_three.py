from typing import List 

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(2,len(s)):
            temp_string = s[i-2:i+1]
            temp_list = list()

            for j in temp_string:
                if j not in temp_list:
                    temp_list.append(j)
                
            if len(temp_list) == 3:
                count += 1


        return count



solution = Solution()

print(solution.countGoodSubstrings(s = "xyzzaz"))

print(solution.countGoodSubstrings(s = "aababcabc"))
