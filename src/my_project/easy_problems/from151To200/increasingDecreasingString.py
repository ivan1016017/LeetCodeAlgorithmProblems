from typing import List 

class Solution:
    def sortString(self, s: str) -> str:
        vocabulary =  "abcdefghijklmnopqrstuvwxyz"
        dict_vocabulary = dict()
        for letter in vocabulary:
            dict_vocabulary[letter] = 0

        for i in s:
            dict_vocabulary[i] += 1

        answer = ""

        while len(answer) < len(s):

            for i in range(len(vocabulary)):
                if dict_vocabulary[vocabulary[i]] > 0:
                    answer += vocabulary[i]
                    dict_vocabulary[vocabulary[i]] -= 1

            for i in range(len(vocabulary)-1, -1, -1):
                if dict_vocabulary[vocabulary[i]] > 0:
                    answer += vocabulary[i]
                    dict_vocabulary[vocabulary[i]] -= 1

        return answer


solution = Solution()

print(solution.sortString(s = "aaaabbbbcccc")) 

print(solution.sortString(s = "rat")) 

print(solution.sortString(s = "leetcode")) 

print(solution.sortString(s = "ggggggg")) 

