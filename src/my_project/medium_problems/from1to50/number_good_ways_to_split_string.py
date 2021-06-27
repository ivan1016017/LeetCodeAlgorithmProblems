from typing import List

class Solution:
    def numSplits(self, s: str) -> int:

        #initialize variables
        count = 0
        len_s = len(s)

        for i in range(len_s):
            if len(set(s[0:i+1])) == len(set(s[i+1:])):
                count += 1
        return count


class SecondSolution:
    def numSplits(self, s: str) -> int:
        uniqueCharsFromLeft = []
        tmp = set()
        uniqueChars = 0

        for ch in s:
            if ch not in tmp:
                tmp.add(ch)
                uniqueChars += 1
            uniqueCharsFromLeft.append(uniqueChars)

        uniqueCharsFromRight = 0
        tmp = set()
        res = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] not in tmp:
                tmp.add(s[i])
                uniqueCharsFromRight += 1

            if uniqueCharsFromLeft[i - 1] == uniqueCharsFromRight:
                res += 1

        print(uniqueCharsFromLeft)
        return res





class SampleSolution:

    def numSplits(self, s: str) -> int:

        uniqueCharsFromLeft = list()
        countLeft = 0
        temp = set()

        for item in s:
            if item not in temp:
                temp.add(item)
                countLeft += 1
            uniqueCharsFromLeft.append(countLeft)
        # print(uniqueCharsFromLeft)
        temp = set()
        countRight = 0
        solution  = 0
        for i in range(len(s)-1,0,-1):
            if s[i] not in temp:
                temp.add(s[i])
                countRight += 1

            if countRight == uniqueCharsFromLeft[i-1]:
                solution += 1


        return solution


solution = SampleSolution()

print(solution.numSplits("abcd"))



