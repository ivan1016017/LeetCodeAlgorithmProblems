from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.temp = list()
        self.temp_list = list()

    def rightSideView(self, root: TreeNode) -> List[int]:
        self.rightTreeNodeToList(root)
        return self.temp


    def rightTreeNodeToList(self, root: TreeNode):

        if root:
            self.temp.append(root.val)
            self.temp_list.append(None)


            if root.left:
                self.temp_list.append(root.left)
            if root.right:
                self.temp_list.append(root.right)



            self.rightTreeNodeToList(self.temp_list[-1])

solution = Solution()
sample = TreeNode(1,TreeNode(2, None, TreeNode(5)),TreeNode(3,None, TreeNode(4)))
sample_two = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(solution.rightSideView(sample_two))


class SecondSolution:

    def __init__(self):
        self.temp = list()

    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return root

        q = [root]

        nxt = []

        level = []

        res = []

        while q != []:
            for root in q:
                level.append(root.val)

                if root.left:
                    nxt.append(root.left)

                if root.right:
                    nxt.append(root.right)

            res.append(level[-1])

            level = []

            q = nxt
            nxt = []

        return res

second_solution = SecondSolution()
print(second_solution.rightSideView(sample_two))
