from typing import List 

class SolutionTwo:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        len_tickets = len(tickets)
        ticket_copy = tickets.copy()
        ticket_copy.sort()
        answer = 0
        for i in range(len_tickets):
           
            if ticket_copy[i] < tickets[k]:
                answer += ticket_copy[i]
            else: 
                break
                
        answer += (len_tickets-i)*tickets[k]
        
        
        return answer
    
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        selected = tickets[k]
        count = 0
        for i,x in enumerate(tickets):
            if i < k:
                count += min(x,selected)
            elif i == k:
                count += selected
                
            else:
                if x < selected:
                    count += x
                else:
                    count += selected-1
                
        return count
    
solution = Solution()

print(solution.timeRequiredToBuy(tickets = [2,3,2], k = 2))

print(solution.timeRequiredToBuy(tickets = [5,1,1,1], k = 0))

print(solution.timeRequiredToBuy(tickets = [84,49,5,24,70,77,87,8], k = 3))

