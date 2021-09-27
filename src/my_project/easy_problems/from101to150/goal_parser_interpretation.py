from typing import List 

class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace('(al)', 'al')
        command = command.replace('()', 'o')
        return command


solution = Solution()

print(solution.interpret(command = "G()(al)"))