from typing import List


if __name__ == '__main__':
    class Solution:
        def majorityElement(self, nums: List[int]) -> int:

            temp_dict = dict()
            temp_set = set(nums)

            for i in range(len(nums)):

                if nums[i] not in temp_dict:
                    temp_dict[nums[i]] = 0
                if nums[i] in temp_dict:
                    temp_dict[nums[i]] += 1
                if temp_dict[nums[i]] > len(nums)//2:
                    return nums[i]

            print(temp_dict)


    solution = Solution()
    print(solution.majorityElement([2,2,1,1,1,2,2]))