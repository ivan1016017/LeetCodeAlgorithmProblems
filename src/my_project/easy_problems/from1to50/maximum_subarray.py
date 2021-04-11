from typing import List
import math

if __name__ == '__main__':

    def max_subarray(vector: List[int]) -> int:
        n = len(vector)
        local_max = 0
        global_max = -math.inf

        for i in range(len(vector)):
            local_max = max(vector[i], vector[i]+local_max)
            if local_max > global_max:
                global_max = local_max

        return global_max


    list_sample = [4,-2,100,100]
    print(max_subarray(list_sample))