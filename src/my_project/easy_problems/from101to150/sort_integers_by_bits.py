from typing import List 

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        arr.sort()

        def count_number_bits(num: int) -> int:

            quotient = None 
            count = 0
            reminder = 0
            while quotient != 0:
                quotient = num // 2
                reminder = num % 2
                count += reminder 
                num = quotient

            return count 

        arr.sort(key= lambda x: count_number_bits(x))

        return arr 

solution = Solution()

print(solution.sortByBits(arr = [0,1,2,3,4,5,6,7,8]))

print(solution.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]))

print(solution.sortByBits(arr = [10000,10000]))

print(solution.sortByBits(arr = [2,3,5,7,11,13,17,19]))

print(solution.sortByBits(arr = [10,100,1000,10000]))

