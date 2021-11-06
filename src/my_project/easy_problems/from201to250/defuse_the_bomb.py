from typing import List 

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        len_code: int = len(code)
        solution: List[int] = list()
        solution = [ 0 for i in range(len_code)]
        count = 0
        if k > 0:
            for i in range(len_code):
                print(i)
                count = 0
                for l in range(i+1, i+1+k):
                    count += code[l%len_code]
                solution[i] = count 
        elif k < 0: 
            for i in range(len_code):
                count = 0
                for l in range(i-1, i-1+k,-1):
                    print(l)
                    count += code[l%len_code]
                solution[i] = count 
        else: 
            return solution 



        return solution

solution = Solution()

print(solution.decrypt(code = [5,7,1,4], k = 3))

print(solution.decrypt(code = [2,4,9,3], k = -2))
