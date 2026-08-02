from typing import List
from collections import deque, defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """Topological sort (Kahn's BFS) over letters.

        Each adjacent pair of words gives at most one ordering fact: the first
        position where they differ tells us c1 comes before c2. Everything after
        that position is unconstrained, so we stop comparing there. The invalid
        case is a prefix violation - ["abc", "ab"] - since a proper prefix must
        sort first no matter what the alphabet is.

        Time O(C) where C is total characters, space O(1) - at most 26 nodes and
        26 * 26 edges.
        """

        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}

        for first, second in zip(words, words[1:]):
            for c1, c2 in zip(first, second):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
            else:
                # No differing character: second must not be a strict prefix
                if len(second) < len(first):
                    return ""

        q = deque([c for c in indegree if indegree[c] == 0])
        order = []

        while q:
            c = q.popleft()
            order.append(c)

            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        # A leftover letter means it sits on a cycle
        return "".join(order) if len(order) == len(adj) else ""


    def alienOrder_DFS(self, words: List[str]) -> str:
        """Same graph, post-order DFS with cycle detection.

        visiting[c] is True while c is on the current recursion stack (cycle) and
        False once it is fully processed. Post-order emits a letter only after all
        of its successors, so the reversed result is the topological order.
        """

        adj = defaultdict(set)
        letters = {c for word in words for c in word}

        for first, second in zip(words, words[1:]):
            for c1, c2 in zip(first, second):
                if c1 != c2:
                    adj[c1].add(c2)
                    break
            else:
                if len(second) < len(first):
                    return ""

        visiting = {}
        order = []

        def dfs(c: str) -> bool:
            """Returns True if a cycle is reached from c."""
            if c in visiting:
                return visiting[c]

            visiting[c] = True
            for nxt in adj[c]:
                if dfs(nxt):
                    return True

            visiting[c] = False
            order.append(c)
            return False

        for c in letters:
            if dfs(c):
                return ""

        return "".join(reversed(order))
