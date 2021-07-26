from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:



        return self.allocate(preorder, 0, len(preorder)-1)

    def allocate(self, temp: List[int], low: int, high: int) -> TreeNode:

        if low > high:
            return
        node = TreeNode(temp[low])
        current_value = high

        for i in range(low, high+1):
            if temp[i] > temp[low]:
                current_value = i -1
                break
        node.left = self.allocate(temp, low+1, current_value)
        node.right = self.allocate(temp, current_value+1, high)

        return node


sample = [1]
print(sample.pop(0))
print(sample.pop(0))