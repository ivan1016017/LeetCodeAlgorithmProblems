from typing import List

class SecondSolution:
    def minOperations(self, boxes: str) -> List[int]:

        # initialize variables
        len_boxes = len(boxes)
        count = None
        solution = [0 for x in range(len_boxes)]

        for i in range(len_boxes):
            count = 0
            for j in range(len_boxes):
                if i != j:
                    if boxes[j] != "0":
                        count += abs(i-j)
            solution[i] = count
        return solution


class Solution():
    def minOperations(self, boxes):
        n = len(boxes)

        leftDist = [0] * n
        leftBallCnt = int(boxes[0])
        for i in range(1, n):
            leftDist[i] = leftDist[i - 1] + leftBallCnt
            leftBallCnt = leftBallCnt + int(boxes[i])

        rightDist = [0] * n
        rightBallCnt = int(boxes[n - 1])
        for i in range(n - 2, -1, -1):
            rightDist[i] = rightDist[i + 1] + rightBallCnt
            rightBallCnt = rightBallCnt + int(boxes[i])

        ans = [0] * n
        for i in range(n):
            ans[i] = leftDist[i] + rightDist[i]
        return ans

solution = Solution()

print(solution.minOperations(boxes = "001011"))

sample = "011"