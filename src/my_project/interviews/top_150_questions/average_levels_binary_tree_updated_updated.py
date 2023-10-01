from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	
    __name_of_instance = 'SolutionOne'

    def __init__(self) -> None:
        if Solution.__name_of_instance != 'SolutionOne':
            raise Exception('This is a singleton class')
        else: 
            Solution.__name_of_instance = self 

    @staticmethod
    def get_instance() -> None: 
        print(Solution.__name_of_instance)
        
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        answer = list()
        while q:
            qlen = len(q)
            row = 0
            for i in range(qlen):
                node: Optional[TreeNode] = q.popleft()
                row += node.val 
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            answer.append(row/qlen)
        return answer

class SolutionTwo:
	def averageOfLevels(self, root: TreeNode) -> List[float]:
		if root is not None:
			output = []
			depth = 0
			def trav(node, depth):
				depth += 1
				if len(output) < depth:
					output.append([])
				output[depth - 1].append(node.val)
				if node.left is not None:
					trav(node.left, depth)
				if node.right is not None:
					trav(node.right, depth)
			trav(root, depth)
			return [sum(x)/len(x) for x in output]
		else:
			return []