from typing import List 
import collections

class SecondSolution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max = -1
        len_s: int = len(s)
        count: int = 0
        
        for i in range(len_s):
            count = 0
            for j in range(i+1,len_s):
                if s[i] == s[j]: 
                    if count > max:
                        max = count 
                    count += 1
                else: 
                    count += 1
        
        return max
    
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dct=collections.defaultdict(list)
        for i,char in enumerate(s):
            dct[char].append(i)
        print(dct)
        max_count=-1
        for el in dct:
            if dct[el][-1]-dct[el][0]>max_count:
                max_count=dct[el][-1]-dct[el][0]
        return max_count-1
    
solution = Solution()

print(solution.maxLengthBetweenEqualCharacters(s = "aa"))

print(solution.maxLengthBetweenEqualCharacters(s = "abca"))

print(solution.maxLengthBetweenEqualCharacters(s = "cbzxy"))

print(solution.maxLengthBetweenEqualCharacters(s = "cabbac"))

print(solution.maxLengthBetweenEqualCharacters(s = "mgntdygtxrvxjnwksqhxuxtrv"))

print(len("mgntdygtxrvxjnwksqhxuxtrv"))

