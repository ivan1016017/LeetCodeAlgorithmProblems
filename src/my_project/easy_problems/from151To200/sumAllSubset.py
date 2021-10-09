from typing import List 

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def power_set(lst):
            pw_set = [[]]

            for i in range(0,len(lst)):
                for j in range(0,len(pw_set)):
                    ele = pw_set[j].copy()
                    print(ele)
                    ele = ele + [lst[i]]
                    pw_set = pw_set + [ele]

            return pw_set

        def xor_sum(nums: List[int]) -> int:
            answer = nums[0]
            for i in range(1, len(nums)):
                answer = answer ^ nums[i]
            return answer 

        list_subsets = power_set(nums)

        answer = 0

        for subset in list_subsets[1:]:
            answer += xor_sum(subset)

        return answer


def power_set(lst):
    pw_set = [[]]

    for i in range(0,len(lst)):
        for j in range(0,len(pw_set)):
            ele = pw_set[j].copy()
            print(ele)
            ele = ele + [lst[i]]
            pw_set = pw_set + [ele]

    return pw_set


class SecondSolution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def xor_sum (subset,nums):
            if len(nums)==0:
                xor=0
                for i in subset:
                    xor=xor^i
                return xor
            else:
                return xor_sum(subset+[nums[0]],nums[1:])+ xor_sum(subset,nums[1:])
            
        
        return xor_sum([],nums)
        



print(power_set([1,2,3]))


solution = Solution()

print(solution.subsetXORSum([5,1,6]))

print(solution.subsetXORSum(nums = [3,4,5,6,7,8]))








