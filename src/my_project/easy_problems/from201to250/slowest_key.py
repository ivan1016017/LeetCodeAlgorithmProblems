from typing import List 

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        len_release_times: int = len(releaseTimes)
        releaseTimes = [0] + releaseTimes
        time_duration: int = list()
        dict_time_duration = dict()
        answer = list()
        
        for i in range(len_release_times):
            dict_time_duration[releaseTimes[i+1]-releaseTimes[i]] = []
        
        for i in range(len_release_times):
            time_duration.append(releaseTimes[i+1]-releaseTimes[i])
            dict_time_duration[releaseTimes[i+1]-releaseTimes[i]] += [keysPressed[i]]
            
        max_release_time: int = max(time_duration)
        
                  
        answer = dict_time_duration[max_release_time]
        answer.sort(reverse=True)          
        
        
        return answer[0]
    
solution = Solution()

print(solution.slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd"))


print(solution.slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda"))

print(solution.slowestKey([19,22,28,29,66,81,93,97] ,"fnfaaxha"))

