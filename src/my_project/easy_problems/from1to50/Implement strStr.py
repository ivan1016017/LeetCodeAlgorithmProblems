
if __name__ == '__main__':

    class Solution:
        def strStr(self, haystack: str, needle: str) -> int:
            index = -1
            len_needle = len(needle)
            flag = None

            if len(haystack) == 0 and len_needle == 0:
                return 0
            elif len(haystack) == 0 and len_needle == 0:
                return 0
            elif len(haystack) == 0 and len_needle != 0:
                return -1
            else:
                for i in range(len(haystack)):
                    flag = True
                    if haystack[i] == needle[0] and len(haystack[i:]) >= len_needle:
                        index = i
                        for j in range(len_needle):
                            if haystack[i+j] != needle[j]:
                                index = -1
                                flag = False
                                break
                        if flag == True:
                            return index

                return index

    temp_list = [1,2,3,4]
    print(temp_list[3:])

    solution = Solution()
    print(solution.strStr("aaaa","aa"))


