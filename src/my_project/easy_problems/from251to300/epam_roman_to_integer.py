
class Solution:
    def romanToInt(self, s: str) -> int:
        
        answer = 0
        len_s = len(s)
        
        roman_dict = {"I":1, "V":5, "X":10, "L":50,"C":100,"D":500,"M":1000}
        
        answer += roman_dict[s[len_s-1]]
        
        for i in range(len_s-1):
            
            if roman_dict[s[len_s-2-i]] < roman_dict[s[len_s -1-i]]:
                answer -= roman_dict[s[len_s-2-i]]
            elif roman_dict[s[len_s-2-i]] >= roman_dict[s[len_s -1-i]]:
                answer += roman_dict[s[len_s-2-i]]
                
                
        return answer 