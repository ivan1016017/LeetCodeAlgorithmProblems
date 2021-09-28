class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer: int = 0
        count_r: int = 0
        count_l: int = 0

        for word in s: 
            if word == "R":
                count_r += 1
            else: 
                count_l += 1

            if count_l == count_r:
                answer += 1
        return answer 


solution = Solution()

print(solution.balancedStringSplit( s = "RLRRRLLRLL"))