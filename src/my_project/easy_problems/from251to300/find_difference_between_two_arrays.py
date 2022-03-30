from typing import List 

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        list_one = list()
        list_two = list()
        
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        
        num_total = nums1 + nums2
        
        dict1 = dict()
        dict2 = dict()
        
        
        for num in num_total:
            dict1[num] = 0
            dict2[num] = 0
            
        for num in nums1:
            dict1[num] += 1
        
        for num in nums2:
            dict2[num] += 1
            
        for num in nums2:
            if dict1[num] == 0:
                list_one.append(num)
                
        for num in nums1:
            if dict2[num] == 0:
                list_two.append(num)
                
        return [list_two, list_one]
    
    
    
from typing import List 

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        list_one = list()
        list_two = list()
        
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        
        num_total = nums1 + nums2
        
        dict1 = dict()
        dict2 = dict()
        
        
        for num in num_total:
            dict1[num] = 0
            dict2[num] = 0
            
        for num in nums1:
            dict1[num] += 1
        
        for num in nums2:
            dict2[num] += 1
            
        for num in nums2:
            if dict1[num] == 0:
                list_one.append(num)
                
        for num in nums1:
            if dict2[num] == 0:
                list_two.append(num)
                
        return [list_two, list_one]
    
    
class SolutionTwo:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        l1=set()
        l2 = set()
        nums1 = set(nums1)
        nums2 = set(nums2)
        for i in nums1:
            if i not in nums2:
                l1.add(i)
        for i in nums2:
            if i not in nums1:
                l2.add(i)
        return [l1,l2]