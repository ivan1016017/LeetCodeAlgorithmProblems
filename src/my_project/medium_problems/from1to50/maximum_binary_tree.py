from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        if len(nums) == 0:
            return None
        index = 0
        max = nums[index]
        len_nums = len(nums)

        for i in range(1, len_nums):
            if max < nums[i]:
                max = nums[i]
                index = i
        # print(max, index)
        root = TreeNode(max)

        root.left = self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])

        return root

solution = Solution()

sample = [3,5,6]
solution.constructMaximumBinaryTree(sample)

print(solution.constructMaximumBinaryTree(sample).val)
print(solution.constructMaximumBinaryTree(sample).left.val)
print(solution.constructMaximumBinaryTree(sample).left.left.val)

print(sample[0:-1])
print(sample[0:])

