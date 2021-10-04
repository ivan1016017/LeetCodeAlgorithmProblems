from typing import List 

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        set1 = set(nums1)
        set2 = set(nums2)
        answer =  list()
        for num in set1:
            if num in set2:
                answer.append(num)



        return answer 


solution = Solution()

print(solution.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))

print(solution.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
