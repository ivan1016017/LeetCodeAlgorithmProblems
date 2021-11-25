class Solution:
    def maxPower(self, s: str) -> int:
        
        # initiolize variables
        len_s: int = len(s)
        max: int  = 0
        count: int = 0
        
        # compute the maximum length of the substring with only one character
        for i in range(len_s):
            count = 1
            for j in range(i+1, len_s):
                if s[i] == s[j]:
                    count += 1
                else: 
                    break
            
            
            if count > max: 
                max = count
                            
        return max
    
    
solution= Solution()

print(solution.maxPower(s = "leetcode"))

print(solution.maxPower(s = "abbcccddddeeeeedcba"))

print(solution.maxPower(s = "triplepillooooow"))

print(solution.maxPower(s = "hooraaaaaaaaaaay"))

print(solution.maxPower(s = "tourist"))

