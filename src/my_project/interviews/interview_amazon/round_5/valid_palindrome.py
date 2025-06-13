import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # to lowercase
        s = s.lower()

        # remove non-alphanumeric characters
        s = re.sub(pattern='[^a-zA-Z0-9]', repl='', string=s)

        # find palindrome
        len_s = len(s)

        for i in range(len_s//2):
            if s[i] != s[len_s - 1 - i]:
                return False 
            
        return True
    
