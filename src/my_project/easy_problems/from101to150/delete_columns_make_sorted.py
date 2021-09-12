from typing import List 

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        temp: str = ""
        temp_list: List[str] = list()
        temp_list_ordered: List[str] = list()
        temp_ordered = None
        solution: int = 0
      
        for i in range(len(strs[0])):
            for word in strs:
                temp += word[i]
            temp_list.append(temp)
            temp = ""

        for word in temp_list:
            temp_ordered = [x for x in word]
            temp_ordered.sort()
            temp_ordered = "".join(temp_ordered)
            temp_list_ordered.append(temp_ordered)

        for i in range(len(temp_list)):
            if temp_list[i] != temp_list_ordered[i]:
                solution += 1

            
        return solution


solution = Solution()
print(solution.minDeletionSize(strs = ["zyx","wvu","tsr"]))

