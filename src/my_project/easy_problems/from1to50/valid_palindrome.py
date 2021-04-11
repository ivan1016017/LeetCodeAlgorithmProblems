import re

if __name__ == '__main__':
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            pattern = re.compile(r'[a-zA-Z]')
            matches = pattern.finditer(s)
            temp = ""
            for i in matches:
                temp += i.group(0)
            temp = temp.lower()
            print(temp)
            flag = True
            for i in range(len(temp)):
                if temp[i] != temp[len(temp)-1 -i]:
                    flag = False

            return flag


    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
    print(solution.isPalindrome("ab_a"))
