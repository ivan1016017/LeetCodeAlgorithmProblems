from typing import List 

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if not score:
            return []
        
        newscore = sorted(score, reverse=True)
        
        dic = dict()
        
        l = len(newscore)
        
        dic[newscore[0]] = "Gold Medal"
        
        if l > 1:
            dic[newscore[1]] = "Silver Medal"
            
        if l > 2:
            dic[newscore[2]] = "Bronze Medal"
            
        for i in range(3, len(newscore)):
            dic[newscore[i]] = str(i+1)
            
        answer = [dic[k] for k in score]
        
        return answer 
    