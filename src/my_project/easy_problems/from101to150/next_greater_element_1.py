from typing import List 

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        flag: bool = False
        
        for i in range(len(nums1)):
            flag = False

            for j in range(len(nums2)):

                if nums1[i] == nums2[j]:
                    print(i,j)

                    for l in range(j+1, len(nums2)):
                        print("flag")
                        if nums2[l] > nums1[i]:
                            nums1[i] = nums2[l]
                            flag = True
                            break 
                    if flag == False:
                        nums1[i] = -1

                    break
                    
        return nums1

solution = Solution()

print(solution.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))