from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()
        t=[]
        i=len(deck)-1
        while True:
            t.insert(0,deck[i])
            if i==0:
                break
            t=[t[-1]]+t[:-1]
            i-=1
            print(t)
        return t



        return solution


    def changeOrder(self, deck: List[int]) -> List[int]:


        # initialize variable

        solution: list[int] = list()

        while len(deck)>=2:
            solution.append(deck.pop(0))
            deck.append(deck.pop(0))
            print(deck)

        solution.append(deck.pop())

        return solution


solution = Solution()
print(solution.deckRevealedIncreasing(deck =  [2,13,3,11,5,17,7]))
print(solution.deckRevealedIncreasing(deck =  [13,11,17]))
