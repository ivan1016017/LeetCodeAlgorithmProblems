# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.temp = TreeNode()
        self.solution = TreeNode()
        self.listTemp = list()

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.temp = self.solution
        self.changingTree(root)
        return self.listTemp[0]




    def changingTree(self, root:TreeNode):

        if root is not None:


            self.changingTree(root.left)
            self.temp.val = root.val
            self.listTemp.append(self.solution)
            self.temp.right = TreeNode()
            self.temp = self.temp.right
            self.changingTree(root.right)





sample = TreeNode()

temp = sample



for i in range(1,4):
    temp.right = TreeNode(i)
    temp = temp.right

# for i in range(0,4):
#     temp.val = i
#     temp.right = TreeNode()
#     temp = temp.right

# print(sample.val)
# print(sample.right.val)
# print(sample.right.right.val)
# print(sample.right.right.right.val)

class SecondSolution:
    def increasingBST(self, root):

        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)

        inorder(root)
        return ans.right

solution = SecondSolution()
a = TreeNode(5,TreeNode(1), TreeNode(7))
b = TreeNode(1, TreeNode(2))
print(solution.increasingBST(a).val)
print(solution.increasingBST(a).right.val)
print(solution.increasingBST(a).right.right.val)
