import unittest
from src.my_project.interviews.top_150_questions_round_22\
    .ex_86_clone_graph import Solution, Node
from typing import Optional, List


class CloneGraphTestCase(unittest.TestCase):

    def build_graph(self, adj_list: List[List[int]]) -> Optional[Node]:
        """Helper function to build a graph from adjacency list"""
        if not adj_list:
            return None
        
        # Create all nodes first
        nodes = [Node(i + 1) for i in range(len(adj_list))]
        
        # Build connections
        for i, neighbors in enumerate(adj_list):
            for neighbor_val in neighbors:
                nodes[i].neighbors.append(nodes[neighbor_val - 1])
        
        return nodes[0] if nodes else None
    
    def graph_to_adj_list(self, node: Optional[Node]) -> List[List[int]]:
        """Helper function to convert graph back to adjacency list for comparison"""
        if not node:
            return []
        
        visited = {}
        adj_list = []
        
        def dfs(curr: Node):
            if curr in visited:
                return
            
            visited[curr] = len(visited)
            adj_list.append([])
            
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
        
        # First pass: assign indices
        dfs(node)
        
        # Second pass: build adjacency list
        visited.clear()
        adj_list.clear()
        
        def build_adj(curr: Node):
            if curr in visited:
                return
            
            visited[curr] = len(visited)
            neighbors_vals = [n.val for n in curr.neighbors]
            adj_list.append(sorted(neighbors_vals))
            
            for neighbor in curr.neighbors:
                build_adj(neighbor)
        
        build_adj(node)
        return adj_list
    
    def verify_deep_copy(self, original: Optional[Node], cloned: Optional[Node]) -> bool:
        """Verify that the clone is a deep copy (not sharing references)"""
        if original is None and cloned is None:
            return True
        if original is None or cloned is None:
            return False
        
        visited_original = set()
        visited_cloned = set()
        
        def dfs(orig: Node, clone: Node) -> bool:
            if orig is clone:  # Same reference = not a deep copy
                return False
            
            if orig.val != clone.val:
                return False
            
            if len(orig.neighbors) != len(clone.neighbors):
                return False
            
            visited_original.add(orig)
            visited_cloned.add(clone)
            
            # Check neighbors
            orig_neighbor_vals = sorted([n.val for n in orig.neighbors])
            clone_neighbor_vals = sorted([n.val for n in clone.neighbors])
            
            if orig_neighbor_vals != clone_neighbor_vals:
                return False
            
            # Recursively check unvisited neighbors
            for orig_n, clone_n in zip(
                sorted(orig.neighbors, key=lambda x: x.val),
                sorted(clone.neighbors, key=lambda x: x.val)
            ):
                if orig_n not in visited_original:
                    if not dfs(orig_n, clone_n):
                        return False
            
            return True
        
        return dfs(original, cloned)

    def test_example_1(self):
        """
        Example 1: Graph with 4 nodes
        adjList = [[2,4],[1,3],[2,4],[1,3]]
        """
        solution = Solution()
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)
        
        # Verify it's a deep copy
        self.assertTrue(self.verify_deep_copy(original, cloned))
        
        # Verify structure is the same
        cloned_adj_list = self.graph_to_adj_list(cloned)
        expected = [[2, 4], [1, 3], [2, 4], [1, 3]]
        self.assertEqual(cloned_adj_list, expected)

    def test_example_2(self):
        """
        Example 2: Single node with no neighbors
        adjList = [[]]
        """
        solution = Solution()
        adj_list = [[]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)
        
        # Verify it's a deep copy
        self.assertTrue(self.verify_deep_copy(original, cloned))
        
        # Verify structure
        self.assertIsNotNone(cloned)
        self.assertEqual(cloned.val, 1)
        self.assertEqual(len(cloned.neighbors), 0)

    def test_example_3(self):
        """
        Example 3: Empty graph
        adjList = []
        """
        solution = Solution()
        adj_list = []
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)
        
        # Both should be None
        self.assertIsNone(original)
        self.assertIsNone(cloned)

    def test_two_nodes(self):
        """Test simple graph with two connected nodes"""
        solution = Solution()
        adj_list = [[2], [1]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)
        
        self.assertTrue(self.verify_deep_copy(original, cloned))
        self.assertEqual(self.graph_to_adj_list(cloned), [[2], [1]])

