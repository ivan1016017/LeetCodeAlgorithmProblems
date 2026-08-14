from typing import List, Union, Collection, Mapping, Optional

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            id_, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((rest,id_,log))
        letter_logs.sort(key=lambda x: (x[0],x[1]))

        return [origin for _ , _ , origin in letter_logs] + digit_logs