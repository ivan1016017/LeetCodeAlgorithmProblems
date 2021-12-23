from typing import List 

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        common_list = nums1 + nums2 
        
        dict_nums1 = dict()
        dict_nums2 = dict()
        
        for i in range(len(common_list)):
            dict_nums1[common_list[i]] = 0
            dict_nums2[common_list[i]] = 0
            
        len_nums1: int = len(nums1)
        len_nums2: int = len(nums2)
            
        for i in range(len_nums1):
            dict_nums1[nums1[i]] += 1
            
        for i in range(len_nums2):
            dict_nums2[nums2[i]] += 1
            
            
        answer: list[int] = []
        
        if len_nums1 <= len_nums2:
            for key in dict_nums1.keys():

                answer += [key] * min(dict_nums1[key],dict_nums2[key])
        
        
        else:
            for key in dict_nums2.keys():
                
                answer += [key] * min(dict_nums1[key],dict_nums2[key])
            
        
        return answer
    
solution = Solution()

print(solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))

print(solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
    
    
