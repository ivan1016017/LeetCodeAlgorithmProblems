

if __name__ == '__main__':
    class Solution:
        def lengthOfLastWord(self, s: str) -> int:
            flag = False
            len_string = len(s)
            temp = 0
            if len_string == 0:
                return 0
            else:
                for i in range(len(s)):
                    flag = False
                    if s[i] == " ":
                        try:
                            s[i+1]
                        except:
                            return temp

                        for j in s[i:]:
                            if j != " ":
                                flag = True
                        if flag == False:
                            return temp
                        temp = 0
                        continue
                    temp += 1
                return temp



    solution = Solution()
    print(solution.lengthOfLastWord("Hello  World   "))