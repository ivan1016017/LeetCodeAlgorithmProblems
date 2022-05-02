from typing import List 


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        answer = []
        temp = ""
        for i in range(ord(s[0]), ord(s[3])+1):
            for j in range(int(s[1]), int(s[4])+1):
                temp = chr(i)+str(j)
                answer.append(temp)
        return answer