from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        len_nums2 = len(nums2)
        len_nums1 = len(nums1)
        answer = [-1 for x in range(len_nums1)]
        for i in range(len_nums1):
            for j in range(len(nums2)): 
                if nums2[j] == nums1[i]: 
                    for k in range(j+1,len_nums2):
                        if nums2[k] > nums2[j]:
                            answer[i] = nums2[k]
                            break

        return answer
    

class SolutionTwo:
    def nextGreaterElementTwo(self, A: List[int], B: List[int]) -> List[int]:  
        stack = []
        diff = {}
        
        for pos, val in enumerate(B):
            
            while stack and stack[-1] < val:
                diff[stack.pop()] = val
            
            stack.append(val)
        
        for pos in range(len(A)):
            
            if A[pos] in diff:
                A[pos] = diff[A[pos]]
            else:
                A[pos] = -1
        
        return A
    
