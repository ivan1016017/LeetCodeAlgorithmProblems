from typing import List
from collections import defaultdict, deque




class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """BFS over a generic-pattern graph.

        Build buckets keyed by patterns like 'h*t' so every word that differs
        by a single letter shares a bucket. BFS from beginWord finds the
        shortest transformation, counting words in the sequence.
        """

        if endWord not in wordList:
            return 0

        # Map each wildcard pattern -> list of words matching it.
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)

        # BFS. Level = number of words in the sequence so far (beginWord counts as 1).
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for neighbor in patterns[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                # Clear the bucket so it is not scanned again by another word.
                patterns[pattern] = []

        return 0
