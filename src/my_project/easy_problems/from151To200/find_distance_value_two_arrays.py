from typing import List 

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        answer: int = 0
        flag: bool = True 

        for num1 in arr1:
            flag = True 
            for num2 in arr2:

                if abs(num1 - num2) <= d:
                    flag = False 

            if flag: 
                answer += 1

        return answer 


solution = Solution()

print(solution.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))

print(solution.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))

print(solution.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))
