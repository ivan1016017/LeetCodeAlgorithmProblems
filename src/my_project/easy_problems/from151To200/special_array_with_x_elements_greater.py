from typing import List 

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        print(nums)
        len_nums: int = len(nums)

        for i in range(len_nums):
            if i+1 <= nums[i]:

                if i == len_nums -1:
                    return i +1 
                else: 
                    if i + 1 <= nums[i+1]:
                        continue
                    else: 
                        return i+1

        return -1


solution = Solution()


print(solution.specialArray(nums = [3,5]))

print(solution.specialArray(nums = [0,0]))

print(solution.specialArray(nums = [0,4,3,0,4]))

print(solution.specialArray(nums = [3,6,7,7,0]))


