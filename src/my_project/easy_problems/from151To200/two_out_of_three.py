from typing import List 

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        temp = list()
        for num in nums1:
            if num not in temp:
                temp.append(num)
        nums1 = temp

        temp = []
        for num in nums2:
            if num not in temp:
                temp.append(num)
        nums2 = temp

        temp = []
        for num in nums3:
            if num not in temp:
                temp.append(num)
        nums3 = temp

        temp_dict = {}

        for num in nums1 + nums2 + nums3:
            temp_dict[num] = 0
        
        for num in nums1 + nums2 + nums3:
            temp_dict[num] += 1

        answer = list()

        for num in temp_dict.keys():
            if temp_dict[num] >= 2:
                answer.append(num)



        return answer

solution = Solution()

print(solution.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))

print(solution.twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]))

print(solution.twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]))
