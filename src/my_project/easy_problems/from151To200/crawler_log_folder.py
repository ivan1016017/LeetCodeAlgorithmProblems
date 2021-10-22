from typing import List 

class Solution:
    def minOperations(self, logs: List[str]) -> int:

        count: int = 0

        for word_command in logs:
            if word_command == "./":
                count += 0
            elif word_command == "../":
                if count == 0:
                    count = 0
                else: 
                    count -= 1
            else: 
                count += 1

        return count 

solution = Solution()

print(solution.minOperations(logs = ["d1/","d2/","../","d21/","./"]))

print(solution.minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"]))

print(solution.minOperations(logs = ["d1/","../","../","../"]))

print(solution.minOperations(logs = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]))

