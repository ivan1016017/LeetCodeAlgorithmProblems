from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # initialize variables
        odd_list = list()
        even_list = list()

        for number in nums:
            if number % 2 == 1:
                odd_list.append(number)
            else:
                even_list.append(number)

        return even_list + odd_list

solution = Solution()
print(solution.sortArrayByParity(nums = [3,1,2,4]))