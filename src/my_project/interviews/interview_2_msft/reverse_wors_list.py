from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def reverseWords(self, s: str) -> str:

        temp_list = s.split(' ')
        answer = list()

        for w in temp_list:
            temp = ''
            for i in range(len(w)):
                temp = w[i] + temp 

            answer.append(temp)

        return ' '.join(answer)


solution = Solution()

print(solution.reverseWords(s = "Let's take LeetCode contest"))
