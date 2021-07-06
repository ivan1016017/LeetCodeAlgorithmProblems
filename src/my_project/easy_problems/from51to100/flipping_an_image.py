from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        x_len = len(image)

        for i in range(x_len):
            image[i] = image[i][::-1]
            image[i] = [0 if x == 1 else 1 for x in image[i]]
        return image

solution = Solution()
print(solution.flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))


class SecondSolution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[0 if x==1 else 1 for x in row[::-1]] for row in image]
