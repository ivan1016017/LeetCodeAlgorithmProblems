from typing import List 

class Solution:
    def removeDuplicates(self, s: str) -> str:

        list_solution = []

        for letter in s:

            if not list_solution:
                list_solution.append(letter)

            elif list_solution and list_solution[-1] != letter: 
                list_solution.append(letter)

            else: 
                list_solution.pop()


        return ''.join(list_solution)


solution = Solution()

print(solution.removeDuplicates(s = "abbaca"))

print(solution.removeDuplicates(s = "azxxzy"))
