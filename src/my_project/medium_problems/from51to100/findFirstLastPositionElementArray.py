from typing import List 

class FirstSolution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        len_nums: int = len(nums)
        answer: List[int] = [-1,-1]
        flag: bool = False
        

        
        for i in range(len_nums):
            
            if flag == False and nums[i] == target:
                flag = True
                answer[0] = i 
            elif flag == True and nums[i] != target:
                answer[1] = i-1
                return answer
            
        if flag == True:
            answer[1] = len_nums-1
            
        
        return answer
    
   
   
   
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        len_nums = len(nums)
        
        def first(nums, target):
            low = 0
            high = len_nums -1 
            answer = -1
            mid = 0
            
            while (low <= high):
                
                mid = (low + high) //2
                
                if nums[mid] > target:
                    high = mid -1
                elif nums[mid] < target:
                    low = mid + 1  
                    
                else:
                    answer = mid 
                    high = mid -1
                    
            return answer
            
        def last(nums, target):
            low = 0
            high = len_nums -1 
            answer = -1
            mid = 0
            
            while (low <= high):
                
                mid = (low + high) //2
                
                if nums[mid] > target:
                    high = mid -1
                elif nums[mid] < target:
                    low = mid + 1  
                    
                else:
                    answer = mid 
                    low = mid + 1
                    
            return answer
            
            
        
        return [first(nums,target), last(nums,target)]
    
solution = Solution()

print(solution.searchRange(nums = [5,7,7,8,8,10], target = 8))

print(solution.searchRange(nums = [5,7,7,8,8,10], target = 6))

print(solution.searchRange(nums = [], target = 0))

print(solution.searchRange(nums = [1], target = 1))


