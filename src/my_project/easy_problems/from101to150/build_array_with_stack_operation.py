from typing import List 

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer: List[int] = list()

        for i in range(target[-1]):
            if i+1 in target:
                answer.append("Push")
            else: 
                answer.append("Push")
                answer.append("Pop")
        return answer 


solution = Solution()

print(solution.buildArray( target = [1,3], n = 3))


print(solution.buildArray(target = [1,2,3], n = 3))


print(solution.buildArray(target = [1,2], n = 4))


print(solution.buildArray(target = [2,3,4], n = 4))
