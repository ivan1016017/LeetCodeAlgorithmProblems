class Solution:
    def partitionString(self, s: str) -> int:

        # 1-based positions: 0 means "character never seen"
        last_pos = [0] * 26
        partitions = 0
        partition_start = 0

        for i in range(len(s)):

            # last occurrence falls inside the open partition -> must cut
            if last_pos[ord(s[i]) - ord('a')] >= partition_start:
                partitions += 1
                partition_start = i + 1

            last_pos[ord(s[i]) - ord('a')] = i + 1

        return partitions