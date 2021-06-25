from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        # initialize variables
        temp_index = None
        count = 0

        if ruleKey == "type":
            temp_index = 0
        if ruleKey == "color":
            temp_index =1
        if ruleKey == 'name':
            temp_index = 2


        for item in items:
            if item[temp_index] == ruleValue:
                count += 1





        return count


solution = Solution()
print(solution.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))