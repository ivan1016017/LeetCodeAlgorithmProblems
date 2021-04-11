from typing import List

if __name__ == '__main__':


    class firstSolution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:

            for i in range(len(numbers)-1):
                for j in range(i+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        return [i+1, j+1]
            return []


    class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            start = 0
            end = len(numbers) - 1
            sum = 0
            while start != end:
                sum = numbers[start] + numbers[end]
                if sum > target:
                    end -= 1
                elif sum < target:
                    start += 1
                else:
                    return [start + 1, end + 1]


    solution = firstSolution()
    print(solution.twoSum([2,3,4],6))