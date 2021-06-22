from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        # initialize variables
        temp_list = list()
        solution = list()
        len_nums = len(nums)
        for i in range(len_nums//2):
            temp_list.append(nums[i*2] * [nums[(i*2) + 1]])



        for i in range(len(temp_list)):
            solution += temp_list[i]


        return solution


solution = Solution()
print(solution.decompressRLElist([1,2,3,4]))