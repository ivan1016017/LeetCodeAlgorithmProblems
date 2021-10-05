from typing import List 

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        left_string: str = ""
        right_string: str = ""
        answer: str = ""
        
        count: int = 0
        flag: bool = False
        for letter in word: 
            count += 1
            if letter == ch:
                flag = True
                left_string = word[0:count]
                right_string = word[count:]
                break

        if not flag: 
            return word 

        for i in range(len(left_string)-1, -1, -1):
            answer += left_string[i]




        return answer + right_string


solution = Solution()

print(solution.reversePrefix(word = "abcdefd", ch = "d"))

print(solution.reversePrefix(word = "xyxzxe", ch = "z"))

print(solution.reversePrefix(word = "abcd", ch = "z"))



