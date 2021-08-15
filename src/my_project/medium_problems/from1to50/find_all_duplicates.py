from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        solution = list()
        set_unique_elements = set()

        for item in nums:
            if item not in set_unique_elements:
                set_unique_elements.add(item)
                continue
            else:
                solution.append(item)

        return solution


solution = Solution()

print(solution.findDuplicates(nums = [4,3,2,7,8,2,3,1]))
print(solution.findDuplicates(nums = [1,1,2]))