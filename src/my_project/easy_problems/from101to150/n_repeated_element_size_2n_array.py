from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        # initialize variables
        nums = sorted(nums)
        list_nums = list()
        len_nums = len(nums)
        target = len_nums//2
        count = 0
        temp_set = set()


        for number in nums:

            if number in temp_set:
                count += 1
            if number not in temp_set:
                temp_set.add(number)
                count = 1

            if count == target:
                return number


solution = Solution()

print(solution.repeatedNTimes(nums=[2,1,2,5,3,2]))