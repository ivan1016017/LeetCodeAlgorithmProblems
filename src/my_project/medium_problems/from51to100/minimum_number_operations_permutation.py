from typing import List

class SecondSolution:
    def reinitializePermutation(self, n: int) -> int:

        solution = list(range(n))
        check_list = list(range(n))
        solution = self.operation_permutation(solution)

        count: int = 1

        while check_list != solution:

            solution = self.operation_permutation(solution)
            count += 1




        return count

    def operation_permutation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        solution = [0 for x in range(n)]

        for i in range(n):
            if i % 2 == 0:
                solution[i] = nums[int(i/2)]
            else:
                solution[i] =  nums[int((n/2) + (i-1)/2)]
        return solution


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = int(n/2 + (1-1)/2)
        step = 1
        if perm == 1:
            return step
        else:
            while perm != 1:
                if perm%2 == 0:
                    perm = int(perm/2)
                else:
                    perm = int(n/2 + (perm-1)/2)
                step += 1
            return step


solution = Solution()

# print(solution.operation_permutation([0,1,2,3]))

# print(list(range(3)))

print([1,2,3] == [1,2,3])

print(solution.reinitializePermutation(4))