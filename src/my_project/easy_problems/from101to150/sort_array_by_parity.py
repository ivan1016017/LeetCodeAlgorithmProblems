from typing import List 

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        count: int = 0
        solution: list[int] = list()

        while len(nums) > 0:

            for item in nums:
                if item % 2 == 0 and count % 2 == 0:
                    nums.remove(item)
                    solution.append(item)
                    break
                if item % 2 != 0 and count % 2 != 0:
                    nums.remove(item)
                    solution.append(item)
                    break 
            count += 1
            
            

        return solution 


solution = Solution()

print(solution.sortArrayByParityII(nums = [4,2,5,7]))