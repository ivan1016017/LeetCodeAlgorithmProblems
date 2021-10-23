from typing import List

if __name__ == '__main__':
    class Solution:
        def isValid(self, s: str) -> bool:
            temp_list = list()
            current = None
            list_parentheses = ["(","[","{"]
            for parenth in s:
                if parenth in list_parentheses:
                    temp_list.append(parenth)
                else:
                    if not temp_list:
                        return False
                    current = temp_list.pop()
                    if current == "(":
                        if parenth != ")":
                            return False
                    if current == "[":
                        if parenth != "]":
                            return False
                    if current == "{":
                        if parenth != "}":
                            return False
            if temp_list:
                return False
            return True

# this si to test the git functionalities


    solution = Solution()
    print(solution.isValid("(())"))



