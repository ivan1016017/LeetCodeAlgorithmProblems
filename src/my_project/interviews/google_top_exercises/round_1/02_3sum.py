from typing import List 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = list()
        positives = list()
        negatives = list()
        num_zeroes = 0

        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0: 
                negatives.append(num)
            else: 
                num_zeroes += 1

        s_positives = set(positives)
        s_negatives = set(negatives)

        for i in range(len(positives)):
            for j in range(i+1, len(positives)):
                k = positives[i] + positives[j]
                if -k in s_negatives:
                    mi = min(positives[i], positives[j])
                    ma = max(positives[i], positives[j])
                    answer.append((-k, mi, ma))


        for i in range(len(negatives)):
            for j in range(i+1, len(negatives)):
                k = negatives[i] + negatives[j]
                if -k in s_positives:
                    mi = min(negatives[i], negatives[j])
                    ma = max(negatives[i], negatives[j])
                    answer.append((mi, ma, -k))

        if num_zeroes >= 1:
            for num in s_positives:
                if -num in s_negatives:
                    answer.append((-num, 0, num))

        if num_zeroes >= 3:
            answer.append((0,0,0))

        return list(set(answer))