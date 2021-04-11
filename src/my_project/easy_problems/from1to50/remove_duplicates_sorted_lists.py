from typing import List

if __name__ == '__main__':
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            j = 0
            len_nums = len(nums)
            if len_nums == 0 or len_nums ==1:
                return len_nums
            else:
                for i in range(len(nums)-1):
                    if nums[i] != nums[i+1]:
                        nums[j] = nums[i]
                        j += 1
                nums[j] = nums[len_nums -1]
                print(j+1)

                return nums




    solution = Solution()
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))