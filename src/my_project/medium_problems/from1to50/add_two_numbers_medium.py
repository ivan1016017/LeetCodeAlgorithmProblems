from typing import List

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         list_bin = list()
#         for i in s:
#
#         print("Hello")

class Solution:
    def lengthOfLongestSubstringSample(self, s):
        dic, res, start = {}, 0, 0
        for i in range(len(s)):
            if s[i] in dic:
                start = max(start, dic[s[i]] + 1)
            dic[s[i]] = i
            res = max(res, i - start+1)
        return res

if __name__ == '__main__':
    # solution = Solution()
    # solution.lengthOfLongestSubstring(3)
    # print("Hello World")
    # print("l" + "d")
    # print("abc"[1])

    string_value = "abcdaef"
    def largest_chain(s):
        temp_list = list()

        if len(s) ==1 or len(s) < 1:
            return temp_list.append(s[0])
        else:
            temp_list.append(s[0])
            for i in s[1:]:
                if i not in temp_list[-1]:
                    temp_list[-1] += i
                else:
                    return temp_list[-1]
            return temp_list[-1]

    def max_length_chain(s):

        max_length = list()
        if len(s) == 1:
            return 1
        else:
            for i in range(len(s)-1):


                max_length.append(len(largest_chain(s[i:])))
            try:
                max(max_length)
            except:
                return 0
            return max(max_length)

    # print(largest_chain(string_value[0:]))
    # print(largest_chain( string_value[1:]))
    # print(largest_chain(string_value[2:]))
    # print(max_length_chain(string_value))
    print(max_length_chain("abcdaef"))
    solution = Solution()
    print(solution.lengthOfLongestSubstringSample(string_value))