from typing import List 
import re 

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # pattern = re.compile(r'[0-9][0-9]')
        # matches = pattern.finditer(s)
        # list_numbers: List[int] = list()
        # for num in matches:
        #     list_numbers.append(int(num.group(0)))
        # print(list_numbers)
        # for i in range(1,len(list_numbers)):
        #     if list_numbers[i-1] > list_numbers[i]:
        #         return False 
                
        # return True 

        list_words = s.split(' ')

        list_numbers = [int(word) for word in list_words if word.isnumeric()]

        for i in range(1, len(list_numbers)):
            if list_numbers[i-1] >= list_numbers[i]:
                return False 
        return True 

solution = Solution()

print(solution.areNumbersAscending( s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"))

print(solution.areNumbersAscending(  s = "hello world 5 x 5"))

print(solution.areNumbersAscending( s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))

print(solution.areNumbersAscending(  s = "4 5 11 26"))

