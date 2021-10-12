from typing import List 

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        count: int = 0
        number_lines: int = 1
        print(len(widths))
        for letter in s:
            if count + widths[(ord(letter)%97)] <= 100:
                count += widths[(ord(letter)%97)]
            else: 
                count = widths[(ord(letter)%97)]
                number_lines += 1

        result = [ number_lines, count] 


        return result 


solution = Solution()

print(solution.numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"))

print(solution.numberOfLines( widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))


